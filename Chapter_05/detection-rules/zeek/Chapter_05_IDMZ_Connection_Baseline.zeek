##! Chapter_05_IDMZ_Connection_Baseline.zeek
##!
##! UC-ICS-012 Companion: IDMZ Connection Pair Baseline Script
##! ================================================================
##! Description: Establishes and monitors connection pair baselines at 
##!   the IDMZ boundary. During the learning phase, records all unique 
##!   source-destination-port-protocol combinations observed. After the 
##!   learning phase, generates notices for any new connection pair not 
##!   in the established baseline.
##!
##! Book Reference: Chapter 5 — Defensible Architecture and Segmentation
##! ATT&CK for ICS: T0886 (Remote Services), T0822 (External Remote Services)
##! Data Source: Network traffic at IDMZ boundary (Zeek sensor on TAP/SPAN)
##!
##! Deployment:
##!   1. Deploy on Zeek sensor monitoring IDMZ boundary traffic
##!   2. Set learning_phase to T (true) for initial baseline period (7-30 days)
##!   3. After baseline period, set learning_phase to F (false)
##!   4. New connection pairs will generate Notice::IDMZ_NewConnectionPair
##!   5. Feed notices to SIEM via Zeek notice.log → Sentinel ingestion
##!
##! Prerequisites:
##!   - Zeek deployed on IDMZ TAP or SPAN port
##!   - Network ranges configured below for OT, IT, and IDMZ subnets
##!
##! Usage:
##!   zeek -r trace.pcap Chapter_05_IDMZ_Connection_Baseline.zeek
##!   # or in site/local.zeek:
##!   @load ./Chapter_05_IDMZ_Connection_Baseline
##! ================================================================

@load base/frameworks/notice

module IDMZ_Baseline;

export {
    ## Notice type for new connection pairs observed after baseline
    redef enum Notice::Type += {
        IDMZ_NewConnectionPair,
        IDMZ_NewProtocol,
        IDMZ_NewSourceToOT,
    };

    ## OT network subnet(s) — adjust for your environment
    const ot_nets: set[subnet] = {
        10.1.0.0/16,
    } &redef;

    ## IT/Enterprise network subnet(s)
    const it_nets: set[subnet] = {
        10.0.0.0/16,
    } &redef;

    ## IDMZ subnet(s)
    const idmz_nets: set[subnet] = {
        10.2.0.0/24,
    } &redef;

    ## Learning phase: set to T during initial baselining, F for detection
    const learning_phase: bool = T &redef;

    ## Path to baseline file (persists across restarts)
    const baseline_file = "idmz_connection_baseline.dat" &redef;

    ## Logging for baseline entries
    type BaselineEntry: record {
        src_ip:     addr;
        dst_ip:     addr;
        dst_port:   port;
        proto:      string;
        first_seen: time;
        last_seen:  time;
        count:      count;
    };
}

## In-memory baseline of known connection pairs
## Key: "src_ip|dst_ip|dst_port|proto"
global connection_baseline: table[string] of BaselineEntry;

## Track unique source IPs seen accessing OT
global known_ot_sources: set[addr];

## Track unique protocols seen crossing IDMZ
global known_protocols: set[string];

## Generate a baseline key from connection parameters
function make_key(src: addr, dst: addr, p: port, proto: string): string
    {
    return fmt("%s|%s|%s|%s", src, dst, p, proto);
    }

## Determine if an address is in the OT network
function is_ot(a: addr): bool
    {
    for ( net in ot_nets )
        if ( a in net )
            return T;
    return F;
    }

## Determine if an address is in the IT network
function is_it(a: addr): bool
    {
    for ( net in it_nets )
        if ( a in net )
            return T;
    return F;
    }

## Determine if an address is in the IDMZ
function is_idmz(a: addr): bool
    {
    for ( net in idmz_nets )
        if ( a in net )
            return T;
    return F;
    }

## Determine if this connection crosses the IDMZ boundary
function crosses_idmz(orig: addr, resp: addr): bool
    {
    # IT to OT (through IDMZ)
    if ( is_it(orig) && is_ot(resp) )
        return T;
    # OT to IT (through IDMZ)
    if ( is_ot(orig) && is_it(resp) )
        return T;
    # IT to IDMZ
    if ( is_it(orig) && is_idmz(resp) )
        return T;
    # IDMZ to OT
    if ( is_idmz(orig) && is_ot(resp) )
        return T;
    # OT to IDMZ
    if ( is_ot(orig) && is_idmz(resp) )
        return T;
    return F;
    }

event connection_state_remove(c: connection)
    {
    # Only process connections that cross the IDMZ boundary
    if ( ! crosses_idmz(c$id$orig_h, c$id$resp_h) )
        return;

    local proto_str = fmt("%s", get_port_transport_proto(c$id$resp_p));
    local key = make_key(c$id$orig_h, c$id$resp_h, c$id$resp_p, proto_str);

    if ( learning_phase )
        {
        # Learning mode: record new connection pairs
        if ( key !in connection_baseline )
            {
            connection_baseline[key] = BaselineEntry(
                $src_ip = c$id$orig_h,
                $dst_ip = c$id$resp_h,
                $dst_port = c$id$resp_p,
                $proto = proto_str,
                $first_seen = network_time(),
                $last_seen = network_time(),
                $count = 1
            );
            }
        else
            {
            connection_baseline[key]$last_seen = network_time();
            ++connection_baseline[key]$count;
            }

        # Track sources accessing OT
        if ( is_ot(c$id$resp_h) )
            add known_ot_sources[c$id$orig_h];

        # Track protocols
        add known_protocols[proto_str];
        }
    else
        {
        # Detection mode: alert on new connection pairs
        if ( key !in connection_baseline )
            {
            # New connection pair not in baseline
            NOTICE([
                $note = IDMZ_NewConnectionPair,
                $conn = c,
                $msg = fmt("New IDMZ connection pair: %s -> %s:%s (%s) not in baseline",
                    c$id$orig_h, c$id$resp_h, c$id$resp_p, proto_str),
                $sub = fmt("src=%s dst=%s port=%s proto=%s",
                    c$id$orig_h, c$id$resp_h, c$id$resp_p, proto_str),
                $identifier = key
            ]);
            }

        # Alert on new source accessing OT
        if ( is_ot(c$id$resp_h) && c$id$orig_h !in known_ot_sources )
            {
            NOTICE([
                $note = IDMZ_NewSourceToOT,
                $conn = c,
                $msg = fmt("New source %s accessing OT asset %s — not in baseline",
                    c$id$orig_h, c$id$resp_h),
                $sub = fmt("new_source=%s ot_dest=%s port=%s",
                    c$id$orig_h, c$id$resp_h, c$id$resp_p),
                $identifier = fmt("new_src_%s", c$id$orig_h)
            ]);
            }

        # Alert on new protocol crossing IDMZ
        if ( proto_str !in known_protocols )
            {
            NOTICE([
                $note = IDMZ_NewProtocol,
                $conn = c,
                $msg = fmt("New protocol '%s' observed crossing IDMZ boundary: %s -> %s",
                    proto_str, c$id$orig_h, c$id$resp_h),
                $sub = fmt("protocol=%s src=%s dst=%s",
                    proto_str, c$id$orig_h, c$id$resp_h),
                $identifier = fmt("new_proto_%s", proto_str)
            ]);
            }
        }
    }

## Log baseline statistics periodically
event zeek_done()
    {
    if ( learning_phase )
        print fmt("IDMZ Baseline Learning Complete: %d unique connection pairs, %d OT sources, %d protocols",
            |connection_baseline|, |known_ot_sources|, |known_protocols|);
    }
