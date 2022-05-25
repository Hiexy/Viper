from Viper.scan.scan import scan_aps
from Viper.util.read_csv import read_csv

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

        try:
            interface = output.split()[0]
        except:
            raise Exception('No Wireless interface.')
        
        mode = re.findall('Mode:\w*', output)[0].split('Mode:')[1]

        if mode.lower() == 'managed' or mode.lower() == 'auto': 
            subprocess.run(['airmon-ng','start',interface], stdout=subprocess.DEVNULL)
        
        output = subprocess.run('iwconfig',capture_output=True).stdout.decode()
        interface = output.split()[0]

        return interface

        
    
    def scan(self, seconds):
        """
        Scan all available access points and return all available information.
        """
        path = scan_aps(self.interface, seconds)
        ap_list, station_list = read_csv(path)