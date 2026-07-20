#!/usr/bin/env python3
"""
Chapter_09_NetworkX_Anomaly_Hunt.py
================================================================
OT Communication Graph Anomaly Detection using NetworkX
================================================================

Description:
    Builds directed communication graphs from Zeek Modbus (or other
    ICS protocol) logs and identifies structural anomalies that may
    indicate adversary activity. Compares a baseline graph (historical
    "known good" traffic) against recent traffic to detect new edges
    (new communication pairs), weight changes (volume anomalies),
    and outlier nodes (devices with unusual connectivity patterns).

Use Case:
    Supports Hunt-ICS-002 (Covert Channels in Modbus Traffic) and
    Hunt-ICS-003 (Passive Reconnaissance) by providing graph-based
    analysis that identifies structural deviations invisible to
    individual connection-level queries.

Prerequisites:
    - Python 3.8+
    - pip install networkx pandas matplotlib (optional: scikit-learn)
    - Zeek conn.log or Modbus log exports (TSV format)
    - Alternatively, CSV exports from Sentinel KQL queries

Data Sources:
    - Zeek conn.log (TSV) — for general network communication graphs
    - Zeek modbus.log (TSV) — for Modbus-specific protocol graphs
    - Sentinel KQL export (CSV) — query results from Chapter 7/9 queries

Reference: Chapter 9 — The OT Threat Hunting Mindset

Usage:
    python Chapter_09_NetworkX_Anomaly_Hunt.py \\
        --baseline baseline_modbus.log \\
        --recent recent_modbus.log \\
        --output hunt_results/

    python Chapter_09_NetworkX_Anomaly_Hunt.py \\
        --baseline baseline.csv --baseline-format csv \\
        --recent recent.csv --recent-format csv \\
        --output hunt_results/
================================================================
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

try:
    import networkx as nx
except ImportError:
    print("ERROR: NetworkX required. Install: pip install networkx")
    sys.exit(1)

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend for server use
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


# ================================================================
# Data Loading
# ================================================================

def load_zeek_log(filepath: str) -> List[Dict]:
    """Load a Zeek TSV log file, skipping comment/header lines."""
    records = []
    fields = []

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#fields'):
                fields = line.split('\t')[1:]
            elif line.startswith('#') or not line:
                continue
            elif fields:
                values = line.split('\t')
                record = {}
                for i, field in enumerate(fields):
                    if i < len(values):
                        record[field] = values[i] if values[i] != '-' else None
                records.append(record)

    return records


def load_csv_file(filepath: str) -> List[Dict]:
    """Load a CSV file (e.g., Sentinel KQL export)."""
    records = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(dict(row))
    return records


def extract_edges(records: List[Dict],
                  src_field: str = 'id.orig_h',
                  dst_field: str = 'id.resp_h',
                  weight_field: Optional[str] = None) -> List[Tuple[str, str, float]]:
    """
    Extract directed edges from log records.

    Returns list of (src, dst, weight) tuples.
    Weight defaults to count of connections if no weight_field specified.
    """
    edge_counts: Dict[Tuple[str, str], float] = defaultdict(float)

    for record in records:
        src = record.get(src_field)
        dst = record.get(dst_field)

        if not src or not dst:
            continue

        if weight_field and record.get(weight_field):
            try:
                edge_counts[(src, dst)] += float(record[weight_field])
            except (ValueError, TypeError):
                edge_counts[(src, dst)] += 1.0
        else:
            edge_counts[(src, dst)] += 1.0

    return [(src, dst, weight) for (src, dst), weight in edge_counts.items()]


# ================================================================
# Graph Construction
# ================================================================

def build_graph(edges: List[Tuple[str, str, float]],
                label: str = "OT Communication Graph") -> nx.DiGraph:
    """Build a directed graph from edges with weights."""
    G = nx.DiGraph(label=label)

    for src, dst, weight in edges:
        if G.has_edge(src, dst):
            G[src][dst]['weight'] += weight
        else:
            G.add_edge(src, dst, weight=weight)

    return G


# ================================================================
# Anomaly Detection
# ================================================================

def find_new_edges(baseline: nx.DiGraph,
                   recent: nx.DiGraph) -> List[Dict]:
    """
    Identify edges present in recent graph but not in baseline.
    New communication pairs may indicate adversary lateral movement,
    reconnaissance, or covert channel establishment.
    """
    new_edges = []
    baseline_edges = set(baseline.edges())

    for src, dst, data in recent.edges(data=True):
        if (src, dst) not in baseline_edges:
            new_edges.append({
                'source': src,
                'destination': dst,
                'weight': data.get('weight', 0),
                'anomaly_type': 'NEW_EDGE',
                'description': f'New communication pair: {src} -> {dst} '
                               f'(not present in baseline)',
                'hunt_relevance': 'Hunt-ICS-002, Hunt-ICS-003'
            })

    return sorted(new_edges, key=lambda x: x['weight'], reverse=True)


def find_weight_anomalies(baseline: nx.DiGraph,
                          recent: nx.DiGraph,
                          threshold_multiplier: float = 3.0) -> List[Dict]:
    """
    Identify edges with significant weight changes between baseline
    and recent traffic. Large increases may indicate data exfiltration
    or scanning. Large decreases may indicate communication disruption.
    """
    anomalies = []

    for src, dst, recent_data in recent.edges(data=True):
        if baseline.has_edge(src, dst):
            baseline_weight = baseline[src][dst].get('weight', 0)
            recent_weight = recent_data.get('weight', 0)

            if baseline_weight > 0:
                ratio = recent_weight / baseline_weight

                if ratio > threshold_multiplier:
                    anomalies.append({
                        'source': src,
                        'destination': dst,
                        'baseline_weight': baseline_weight,
                        'recent_weight': recent_weight,
                        'ratio': round(ratio, 2),
                        'anomaly_type': 'VOLUME_INCREASE',
                        'description': f'Traffic volume increased {ratio:.1f}x '
                                       f'from baseline ({baseline_weight:.0f} -> '
                                       f'{recent_weight:.0f})',
                        'hunt_relevance': 'Hunt-ICS-002'
                    })
                elif ratio < (1 / threshold_multiplier):
                    anomalies.append({
                        'source': src,
                        'destination': dst,
                        'baseline_weight': baseline_weight,
                        'recent_weight': recent_weight,
                        'ratio': round(ratio, 2),
                        'anomaly_type': 'VOLUME_DECREASE',
                        'description': f'Traffic volume decreased to {ratio:.1%} '
                                       f'of baseline ({baseline_weight:.0f} -> '
                                       f'{recent_weight:.0f})',
                        'hunt_relevance': 'Hunt-ICS-002'
                    })

    return sorted(anomalies, key=lambda x: abs(x['ratio'] - 1), reverse=True)


def find_node_anomalies(baseline: nx.DiGraph,
                        recent: nx.DiGraph) -> List[Dict]:
    """
    Identify nodes with anomalous connectivity patterns:
    - New nodes not in baseline
    - Nodes with significantly changed degree (in/out connections)
    - Nodes that changed from primarily receiving to primarily sending
      (or vice versa) which may indicate role change or compromise
    """
    anomalies = []

    # New nodes
    baseline_nodes = set(baseline.nodes())
    recent_nodes = set(recent.nodes())
    new_nodes = recent_nodes - baseline_nodes

    for node in new_nodes:
        in_deg = recent.in_degree(node)
        out_deg = recent.out_degree(node)
        anomalies.append({
            'node': node,
            'in_degree': in_deg,
            'out_degree': out_deg,
            'anomaly_type': 'NEW_NODE',
            'description': f'New device detected: {node} '
                           f'(in:{in_deg}, out:{out_deg})',
            'hunt_relevance': 'Hunt-ICS-003'
        })

    # Degree change analysis for existing nodes
    for node in baseline_nodes & recent_nodes:
        b_in = baseline.in_degree(node)
        b_out = baseline.out_degree(node)
        r_in = recent.in_degree(node)
        r_out = recent.out_degree(node)

        # Significant out-degree increase (more destinations contacted)
        if b_out > 0 and r_out > b_out * 2:
            anomalies.append({
                'node': node,
                'baseline_out_degree': b_out,
                'recent_out_degree': r_out,
                'anomaly_type': 'DEGREE_INCREASE',
                'description': f'Node {node} contacting {r_out} destinations '
                               f'(baseline: {b_out}) — potential scanning',
                'hunt_relevance': 'Hunt-ICS-003'
            })

        # Role reversal: device that was primarily a receiver now sending
        if b_in > b_out * 2 and r_out > r_in:
            anomalies.append({
                'node': node,
                'baseline_ratio': f'in:{b_in}/out:{b_out}',
                'recent_ratio': f'in:{r_in}/out:{r_out}',
                'anomaly_type': 'ROLE_CHANGE',
                'description': f'Node {node} changed from receiver to sender '
                               f'(baseline in/out: {b_in}/{b_out}, '
                               f'recent: {r_in}/{r_out})',
                'hunt_relevance': 'Hunt-ICS-002'
            })

    return anomalies


def compute_centrality_anomalies(baseline: nx.DiGraph,
                                 recent: nx.DiGraph,
                                 top_n: int = 10) -> List[Dict]:
    """
    Identify nodes whose centrality changed significantly.
    A device that becomes more central in the communication graph
    may have been compromised and is being used as a pivot point.
    """
    anomalies = []

    try:
        b_centrality = nx.betweenness_centrality(baseline, weight='weight')
        r_centrality = nx.betweenness_centrality(recent, weight='weight')
    except Exception:
        return anomalies

    for node in set(b_centrality.keys()) & set(r_centrality.keys()):
        b_cent = b_centrality.get(node, 0)
        r_cent = r_centrality.get(node, 0)

        if b_cent > 0 and r_cent > b_cent * 2:
            anomalies.append({
                'node': node,
                'baseline_centrality': round(b_cent, 4),
                'recent_centrality': round(r_cent, 4),
                'change_ratio': round(r_cent / b_cent, 2) if b_cent > 0 else float('inf'),
                'anomaly_type': 'CENTRALITY_INCREASE',
                'description': f'Node {node} became significantly more central '
                               f'in the communication graph — potential pivot point',
                'hunt_relevance': 'Hunt-ICS-003'
            })

    return sorted(anomalies,
                  key=lambda x: x.get('change_ratio', 0),
                  reverse=True)[:top_n]


# ================================================================
# Reporting
# ================================================================

def generate_report(new_edges: List[Dict],
                    weight_anomalies: List[Dict],
                    node_anomalies: List[Dict],
                    centrality_anomalies: List[Dict],
                    baseline_stats: Dict,
                    recent_stats: Dict,
                    output_dir: str) -> str:
    """Generate a JSON hunt report with all findings."""

    report = {
        'hunt_id': 'Hunt-ICS-NetworkX',
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'description': 'OT Communication Graph Anomaly Detection',
        'reference': 'Chapter 9 — The OT Threat Hunting Mindset',
        'graph_statistics': {
            'baseline': baseline_stats,
            'recent': recent_stats
        },
        'findings': {
            'new_edges': {
                'count': len(new_edges),
                'severity': 'High' if len(new_edges) > 5 else 'Medium' if new_edges else 'None',
                'details': new_edges
            },
            'weight_anomalies': {
                'count': len(weight_anomalies),
                'severity': 'High' if any(a['ratio'] > 10 for a in weight_anomalies) else 'Medium' if weight_anomalies else 'None',
                'details': weight_anomalies
            },
            'node_anomalies': {
                'count': len(node_anomalies),
                'severity': 'High' if any(a['anomaly_type'] == 'NEW_NODE' for a in node_anomalies) else 'Medium' if node_anomalies else 'None',
                'details': node_anomalies
            },
            'centrality_anomalies': {
                'count': len(centrality_anomalies),
                'severity': 'Medium' if centrality_anomalies else 'None',
                'details': centrality_anomalies
            }
        },
        'summary': {
            'total_findings': (len(new_edges) + len(weight_anomalies) +
                               len(node_anomalies) + len(centrality_anomalies)),
            'highest_severity': 'Critical' if len(new_edges) > 10 else
                               'High' if new_edges or any(a.get('ratio', 0) > 10 for a in weight_anomalies) else
                               'Medium' if (weight_anomalies or node_anomalies) else 'None',
            'recommended_actions': []
        }
    }

    # Generate recommendations based on findings
    actions = report['summary']['recommended_actions']
    if new_edges:
        actions.append(
            f'Investigate {len(new_edges)} new communication pairs not present '
            f'in the baseline. Prioritise edges targeting crown jewel assets.'
        )
    if weight_anomalies:
        actions.append(
            f'Review {len(weight_anomalies)} connections with significant '
            f'volume changes. Large increases may indicate data exfiltration.'
        )
    if any(a['anomaly_type'] == 'NEW_NODE' for a in node_anomalies):
        new_node_count = sum(1 for a in node_anomalies if a['anomaly_type'] == 'NEW_NODE')
        actions.append(
            f'{new_node_count} new devices detected on the OT network. '
            f'Verify each against the OT_AssetRegister and investigate any '
            f'unrecognised devices.'
        )
    if centrality_anomalies:
        actions.append(
            f'{len(centrality_anomalies)} nodes show increased centrality — '
            f'may indicate use as pivot points. Correlate with EDR telemetry.'
        )
    if not actions:
        actions.append('No anomalies detected. Update baseline with current data.')

    # Write report
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, 'hunt_networkx_report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)

    return report_path


def generate_graph_visualisation(baseline: nx.DiGraph,
                                 recent: nx.DiGraph,
                                 new_edges: List[Dict],
                                 output_dir: str) -> Optional[str]:
    """Generate a visual comparison of baseline vs recent graphs."""
    if not HAS_MATPLOTLIB:
        return None

    fig, axes = plt.subplots(1, 2, figsize=(20, 10))

    # Baseline graph
    pos = nx.spring_layout(baseline, k=2, iterations=50, seed=42)
    nx.draw_networkx(baseline, pos, ax=axes[0],
                     node_color='#2196F3', node_size=300,
                     edge_color='#90CAF9', width=1,
                     font_size=7, arrows=True, alpha=0.8)
    axes[0].set_title(f'Baseline Graph ({baseline.number_of_nodes()} nodes, '
                      f'{baseline.number_of_edges()} edges)',
                      fontsize=12, fontweight='bold')

    # Recent graph with anomalies highlighted
    all_nodes = set(baseline.nodes()) | set(recent.nodes())
    pos_recent = nx.spring_layout(recent, k=2, iterations=50, seed=42)

    new_edge_set = set((e['source'], e['destination']) for e in new_edges)
    normal_edges = [(u, v) for u, v in recent.edges() if (u, v) not in new_edge_set]
    anomaly_edges = [(u, v) for u, v in recent.edges() if (u, v) in new_edge_set]

    new_node_set = set(recent.nodes()) - set(baseline.nodes())
    normal_nodes = [n for n in recent.nodes() if n not in new_node_set]
    new_nodes = [n for n in recent.nodes() if n in new_node_set]

    nx.draw_networkx_nodes(recent, pos_recent, nodelist=normal_nodes,
                           ax=axes[1], node_color='#2196F3', node_size=300, alpha=0.8)
    if new_nodes:
        nx.draw_networkx_nodes(recent, pos_recent, nodelist=new_nodes,
                               ax=axes[1], node_color='#F44336', node_size=400, alpha=0.9)
    nx.draw_networkx_edges(recent, pos_recent, edgelist=normal_edges,
                           ax=axes[1], edge_color='#90CAF9', width=1, alpha=0.6)
    if anomaly_edges:
        nx.draw_networkx_edges(recent, pos_recent, edgelist=anomaly_edges,
                               ax=axes[1], edge_color='#F44336', width=2.5, alpha=0.9)
    nx.draw_networkx_labels(recent, pos_recent, ax=axes[1], font_size=7)

    axes[1].set_title(f'Recent Graph ({recent.number_of_nodes()} nodes, '
                      f'{recent.number_of_edges()} edges) — '
                      f'Red = Anomalies',
                      fontsize=12, fontweight='bold')

    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    viz_path = os.path.join(output_dir, 'hunt_networkx_graph.png')
    plt.savefig(viz_path, dpi=150, bbox_inches='tight')
    plt.close()

    return viz_path


def get_graph_stats(G: nx.DiGraph) -> Dict:
    """Compute summary statistics for a graph."""
    return {
        'nodes': G.number_of_nodes(),
        'edges': G.number_of_edges(),
        'density': round(nx.density(G), 4),
        'avg_in_degree': round(sum(d for _, d in G.in_degree()) / max(G.number_of_nodes(), 1), 2),
        'avg_out_degree': round(sum(d for _, d in G.out_degree()) / max(G.number_of_nodes(), 1), 2),
        'strongly_connected_components': nx.number_strongly_connected_components(G),
        'weakly_connected_components': nx.number_weakly_connected_components(G),
    }


# ================================================================
# Main Execution
# ================================================================

def main():
    parser = argparse.ArgumentParser(
        description='OT Communication Graph Anomaly Detection (Chapter 9)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Zeek Modbus logs (TSV format)
  python Chapter_09_NetworkX_Anomaly_Hunt.py \\
      --baseline /logs/baseline_modbus.log \\
      --recent /logs/recent_modbus.log \\
      --output ./hunt_results/

  # Sentinel KQL exports (CSV format)
  python Chapter_09_NetworkX_Anomaly_Hunt.py \\
      --baseline baseline.csv --baseline-format csv \\
      --recent recent.csv --recent-format csv \\
      --src-field SrcIpAddr --dst-field DstIpAddr \\
      --output ./hunt_results/

  # With custom anomaly threshold
  python Chapter_09_NetworkX_Anomaly_Hunt.py \\
      --baseline baseline.log --recent recent.log \\
      --threshold 5.0 --output ./hunt_results/
        """
    )

    parser.add_argument('--baseline', required=True,
                        help='Path to baseline log file')
    parser.add_argument('--recent', required=True,
                        help='Path to recent log file')
    parser.add_argument('--baseline-format', choices=['zeek', 'csv'], default='zeek',
                        help='Baseline file format (default: zeek)')
    parser.add_argument('--recent-format', choices=['zeek', 'csv'], default='zeek',
                        help='Recent file format (default: zeek)')
    parser.add_argument('--src-field', default='id.orig_h',
                        help='Source IP field name (default: id.orig_h)')
    parser.add_argument('--dst-field', default='id.resp_h',
                        help='Destination IP field name (default: id.resp_h)')
    parser.add_argument('--weight-field', default=None,
                        help='Optional weight field (default: connection count)')
    parser.add_argument('--threshold', type=float, default=3.0,
                        help='Volume anomaly threshold multiplier (default: 3.0)')
    parser.add_argument('--output', default='./hunt_results',
                        help='Output directory for results')
    parser.add_argument('--no-viz', action='store_true',
                        help='Skip graph visualisation')

    args = parser.parse_args()

    print("=" * 64)
    print("OT Communication Graph Anomaly Detection")
    print("Chapter 9 — The OT Threat Hunting Mindset")
    print("=" * 64)

    # Load data
    print(f"\n[1/6] Loading baseline data: {args.baseline}")
    if args.baseline_format == 'csv':
        baseline_records = load_csv_file(args.baseline)
    else:
        baseline_records = load_zeek_log(args.baseline)
    print(f"       Loaded {len(baseline_records)} baseline records")

    print(f"[2/6] Loading recent data: {args.recent}")
    if args.recent_format == 'csv':
        recent_records = load_csv_file(args.recent)
    else:
        recent_records = load_zeek_log(args.recent)
    print(f"       Loaded {len(recent_records)} recent records")

    # Build graphs
    print("[3/6] Building communication graphs...")
    baseline_edges = extract_edges(baseline_records, args.src_field,
                                   args.dst_field, args.weight_field)
    recent_edges = extract_edges(recent_records, args.src_field,
                                 args.dst_field, args.weight_field)

    baseline_graph = build_graph(baseline_edges, "Baseline")
    recent_graph = build_graph(recent_edges, "Recent")

    baseline_stats = get_graph_stats(baseline_graph)
    recent_stats = get_graph_stats(recent_graph)

    print(f"       Baseline: {baseline_stats['nodes']} nodes, "
          f"{baseline_stats['edges']} edges")
    print(f"       Recent:   {recent_stats['nodes']} nodes, "
          f"{recent_stats['edges']} edges")

    # Detect anomalies
    print("[4/6] Detecting anomalies...")
    new_edges = find_new_edges(baseline_graph, recent_graph)
    weight_anomalies = find_weight_anomalies(baseline_graph, recent_graph,
                                              args.threshold)
    node_anomalies = find_node_anomalies(baseline_graph, recent_graph)
    centrality_anomalies = compute_centrality_anomalies(baseline_graph,
                                                         recent_graph)

    print(f"       New edges:            {len(new_edges)}")
    print(f"       Weight anomalies:     {len(weight_anomalies)}")
    print(f"       Node anomalies:       {len(node_anomalies)}")
    print(f"       Centrality anomalies: {len(centrality_anomalies)}")

    # Generate report
    print(f"[5/6] Generating report to {args.output}/")
    report_path = generate_report(new_edges, weight_anomalies,
                                   node_anomalies, centrality_anomalies,
                                   baseline_stats, recent_stats,
                                   args.output)
    print(f"       Report: {report_path}")

    # Generate visualisation
    if not args.no_viz and HAS_MATPLOTLIB:
        print("[6/6] Generating graph visualisation...")
        viz_path = generate_graph_visualisation(baseline_graph, recent_graph,
                                                 new_edges, args.output)
        if viz_path:
            print(f"       Visualisation: {viz_path}")
    else:
        print("[6/6] Skipping visualisation "
              f"{'(--no-viz flag)' if args.no_viz else '(matplotlib not installed)'}")

    # Summary
    total = (len(new_edges) + len(weight_anomalies) +
             len(node_anomalies) + len(centrality_anomalies))
    print(f"\n{'=' * 64}")
    print(f"HUNT COMPLETE — {total} total anomalies detected")
    if total > 0:
        print(f"Review {report_path} for details and recommended actions.")
    else:
        print("No anomalies detected. Consider updating baseline with current data.")
    print(f"{'=' * 64}")


if __name__ == '__main__':
    main()
