from viper.scan.scan import scan_aps, scan_ap

import subprocess
import re

class Viper:
    def __init__(self):
        self.interface = self.init_interface()

    def init_interface(self):
        """
        Initiate wireless network interface for monitor mode.
        """
        subprocess.run(['airmon-ng','check','kill'])
        output = subprocess.run('iwconfig',capture_output=True).stdout.decode()
        interface = output.split()[0]

        mode = re.findall('Mode:\w*', output)[0].split('Mode:')[1]

        if mode.lower() == 'managed': 
            subprocess.run(['airmon-ng','start',interface])
        
        output = subprocess.run('iwconfig',capture_output=True).stdout.decode()
        interface = output.split()[0]

        return interface

        
    
    def scan(self):
        """
        Scan all available access points and return all available information.
        """
        aps = scan_aps(self.interface)
        for ap in aps:
            result_ap = scan_ap(self.interface, ap)
            print(result_ap.asdict())
        