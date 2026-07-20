# Chapter_09_Zeek_Hunting.zeek
# ================================================================
# OT/ICS Threat Hunting Scripts for Zeek
# ================================================================
# Description: Zeek scripts for local hunting operations supporting
#   Chapter 9 hunting scenarios. Deploy alongside existing ICSNPP
#   parsers on Zeek sensors monitoring OT network segments.
#
# Prerequisites:
#   - Zeek 5.0+ with CISA ICSNPP parsers installed
#   - Deployed on SPAN/TAP monitoring OT network traffic
#   - Network access to industrial protocol traffic (Modbus, ENIP, S7)
#
# Reference: Chapter 9 — The OT Threat Hunting Mindset
# ================================================================

@load base/frameworks/notice
@load base/frameworks/sumstats
@load base/protocols/modbus

module OTHunting;

export {
    redef enum Notice::Type += {
        ## Firmware-related Modbus function codes detected
        Modbus_Firmware_Operation,
        ## Unusual register access outside known baseline
        Modbus_Register_Anomaly,
        ## Single source sending many different function codes (scan)
        Modbus_Function_Code_Scan,
        ## New communication pair not in baseline
        New_OT_Communication_Pair,
        ## EtherNet/IP device discovery detected
        ENIP_Device_Discovery,
        ## High volume of failed Modbus requests (potential DoS or error)
        Modbus_High_Error_Rate,
    };

    ## ---------------------------------------------------------------
    ## Configuration options — adjust to your environment
    ## ---------------------------------------------------------------

    ## Function codes associated with firmware operations
    const firmware_func_codes: set[count] = {
        43,     # Read/Write Device Identification (MEI)
        23,     # Read/Write Multiple Registers (bulk transfer)
    } &redef;

    ## Known engineering workstation IPs (populate from asset register)
    ## Alerts are still generated but severity context changes
    const known_engineering_ips: set[addr] = {} &redef;

    ## Threshold: unique function codes from single source to flag as scan
    const func_code_scan_threshold: count = 5 &redef;

    ## Tracking window for function code scans
    const scan_tracking_window = 10min &redef;

    ## ---------------------------------------------------------------
    ## Internal tracking tables
    ## ---------------------------------------------------------------

    ## Track firmware operations per source-destination pair
    global firmware_ops: table[addr, addr] of count
        &create_expire=1hr &default=0;

    ## Track unique function codes per source-destination pair for scan detection
    global func_code_tracker: table[addr, addr] of set[count]
        &create_expire=10min;

    ## Track known communication pairs (loaded from baseline file)
    global known_comm_pairs: set[addr, addr] &redef;

    ## Track Modbus errors per source-destination
    global modbus_errors: table[addr, addr] of count
        &create_expire=10min &default=0;
}

# ================================================================
# Hunt-ICS-001: Firmware Operation Detection
# ================================================================
# Generates notice events for firmware-related Modbus function codes.
# Correlate with maintenance windows for triage.
# ================================================================

event modbus_message(c: connection, headers: ModbusHeaders, is_orig: bool) &priority=5
{
    if ( ! is_orig )
        return;

    local src = c$id$orig_h;
    local dst = c$id$resp_h;
    local fc = headers$function_code;

    # --- Firmware operation detection ---
    if ( fc in firmware_func_codes )
    {
        ++firmware_ops[src, dst];

        local eng_context = src in known_engineering_ips
            ? "known_engineering_workstation"
            : "UNKNOWN_SOURCE";

        NOTICE([
            $note=Modbus_Firmware_Operation,
            $conn=c,
            $msg=fmt("Modbus firmware operation: FC %d from %s (%s) to %s (count: %d)",
                     fc, src, eng_context, dst, firmware_ops[src, dst]),
            $sub=fmt("hunt_id=Hunt-ICS-001 fc=%d source_type=%s count=%d",
                     fc, eng_context, firmware_ops[src, dst]),
            $identifier=fmt("%s-%s-firmware", src, dst)
        ]);
    }

    # --- Function code scan detection ---
    if ( [src, dst] !in func_code_tracker )
        func_code_tracker[src, dst] = set();

    add func_code_tracker[src, dst][fc];

    if ( |func_code_tracker[src, dst]| >= func_code_scan_threshold )
    {
        local fc_list = "";
        for ( f in func_code_tracker[src, dst] )
            fc_list = fmt("%s%s%d", fc_list, |fc_list| > 0 ? "," : "", f);

        NOTICE([
            $note=Modbus_Function_Code_Scan,
            $conn=c,
            $msg=fmt("Modbus function code scan: %d unique FCs from %s to %s [%s]",
                     |func_code_tracker[src, dst]|, src, dst, fc_list),
            $sub=fmt("hunt_id=Hunt-ICS-003 unique_fcs=%d codes=%s",
                     |func_code_tracker[src, dst]|, fc_list),
            $identifier=fmt("%s-%s-fcscan", src, dst)
        ]);
    }
}

# ================================================================
# Hunt-ICS-002: New Communication Pair Detection
# ================================================================
# Identifies OT communication pairs not present in the known
# baseline. Requires known_comm_pairs to be populated.
# ================================================================

event new_connection(c: connection) &priority=3
{
    local src = c$id$orig_h;
    local dst = c$id$resp_h;

    # Only check if we have a loaded baseline
    if ( |known_comm_pairs| > 0 && [src, dst] !in known_comm_pairs )
    {
        NOTICE([
            $note=New_OT_Communication_Pair,
            $conn=c,
            $msg=fmt("New OT communication pair detected: %s -> %s (port %d)",
                     src, dst, c$id$resp_p),
            $sub=fmt("hunt_id=Hunt-ICS-002 dst_port=%d proto=%s",
                     c$id$resp_p, get_port_transport_proto(c$id$resp_p)),
            $identifier=fmt("%s-%s-newpair", src, dst)
        ]);
    }
}

# ================================================================
# Hunt-ICS-003: Modbus Error Rate Monitoring
# ================================================================
# High error rates on Modbus connections may indicate scanning,
# fuzzing, or interaction with misconfigured/compromised devices.
# ================================================================

event modbus_exception(c: connection, headers: ModbusHeaders, code: count) &priority=3
{
    local src = c$id$orig_h;
    local dst = c$id$resp_h;
    ++modbus_errors[src, dst];

    if ( modbus_errors[src, dst] >= 20 )
    {
        NOTICE([
            $note=Modbus_High_Error_Rate,
            $conn=c,
            $msg=fmt("High Modbus error rate: %d exceptions from %s to %s (latest code: %d)",
                     modbus_errors[src, dst], src, dst, code),
            $sub=fmt("hunt_id=Hunt-ICS-003 error_count=%d exception_code=%d",
                     modbus_errors[src, dst], code),
            $identifier=fmt("%s-%s-errors", src, dst)
        ]);
    }
}

# ================================================================
# Baseline Loading
# ================================================================
# Load known communication pairs from a baseline file.
# File format: one line per pair, "src_ip\tdst_ip"
# Generate the baseline file from Chapter 7 communication mapping.
# ================================================================

event zeek_init()
{
    # Uncomment and adjust path to load baseline from file:
    # Input::add_table([
    #     $source="/opt/zeek/share/zeek/site/ot_baselines/known_comm_pairs.dat",
    #     $name="known_ot_pairs",
    #     $idx=OTHunting::known_comm_pairs,
    #     $mode=Input::REREAD
    # ]);

    Log::print(fmt("OTHunting: Module loaded. Firmware FCs monitored: %d, " +
                   "FC scan threshold: %d, Known engineering IPs: %d, " +
                   "Known comm pairs: %d",
                   |firmware_func_codes|, func_code_scan_threshold,
                   |known_engineering_ips|, |known_comm_pairs|));
}
