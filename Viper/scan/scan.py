import pyrcrack

def scan_aps(interface):
    """
    Run a scan to show all available access points.
    """
    airmon = pyrcrack.AirmonNg()
    async with airmon("wlp3s0") as mon:
        async with pyrcrack.AirodumpNg() as pdump:
            async for aps in pdump(mon.monitor_interface):
                break # So notebook execution doesn't get stuck here 
    
    return aps

def scan_ap(interface, ap):
    """
    Scan a specific access point and return more results.
    """
    async with airmon("wlp3s0") as mon:
    # Re-set the interface in monitor mode as in 
    # previous execution it would have been cleaned up
        async with pyrcrack.AirodumpNg() as pdump:
            async for result in pdump(mon.monitor_interface, **ap.airodump):
                break
    
    return result