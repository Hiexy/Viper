import os

def create_rogue_ap(interface, essid, channel):
    os.system(f'airbase-ng -e "{essid}" -c {channel} {interface} &')