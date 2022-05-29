from asyncio import subprocess
from Viper.util.channel import change_channel

import subprocess


def fake_auth(interface, ap_mac, essid, mac, channel):
    change_channel(interface, channel)
    subprocess.run(['aireplay-ng', '-1', '0', '-e', f'"{essid}"',
                   '-a', ap_mac, '-h', mac, interface])
