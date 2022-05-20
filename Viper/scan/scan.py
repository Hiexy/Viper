import subprocess
import os

def scan_aps(interface, time):
    """
    Run a scan to show all available access points.
    """
    subprocess.run(['timeout',time,'airodump-ng','-w','results','--output-format','csv',interface]) 
    

def scan_ap(interface, ap):
    """
    Scan a specific access point and return more results.
    """
    async with airmon(interface) as mon:
    # Re-set the interface in monitor mode as in 
    # previous execution it would have been cleaned up
        async with pyrcrack.AirodumpNg() as pdump:
            async for result in pdump(mon.monitor_interface, **ap.airodump):
                break
    
    return result