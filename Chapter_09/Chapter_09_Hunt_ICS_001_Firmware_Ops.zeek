# Hunt-ICS-001-Zeek: Modbus Firmware Operation Detection
# Generates notice events for firmware-related Modbus function codes
# Deploy alongside existing ICSNPP Modbus parser

@load base/frameworks/notice
@load base/protocols/modbus

module HuntFirmwareOps;

export {
    redef enum Notice::Type += {
        Modbus_Firmware_Operation,
    };

    # Function codes associated with firmware operations
    const firmware_func_codes: set[count] = {
        43, # Read/Write Device Identification (MEI)
        23, # Read/Write Multiple Registers (bulk transfer indicator)
    } &redef;

    # Track operations per source-destination pair
    global firmware_op_tracker: table[addr, addr] of count
        &create_expire=1hr &default=0;
}

event modbus_message(c: connection, headers: ModbusHeaders, is_orig: bool) &priority=3
{
    if ( is_orig && headers$function_code in firmware_func_codes )
    {
        local src = c$id$orig_h;
        local dst = c$id$resp_h;
        ++firmware_op_tracker[src, dst];

        NOTICE([
            $note=Modbus_Firmware_Operation,
            $conn=c,
            $msg=fmt("Modbus firmware-related operation: FC %d from %s to %s (count: %d)",
                headers$function_code, src, dst, firmware_op_tracker[src, dst]),
            $sub=fmt("FC=%d", headers$function_code),
            $identifier=fmt("%s-%s-firmware", src, dst)
        ]);
    }
}
