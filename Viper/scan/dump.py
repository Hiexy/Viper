import subprocess


def airodump(interface, ap_mac_address, channel, pcapfile4way, seconds):
    print(interface, ap_mac_address, channel, pcapfile4way, seconds)
    print('Starting airodump')
    try:
        command = subprocess.run(['airodump-ng', '--bssid', ap_mac_address, '--write',
                        f'{pcapfile4way}', '--output-format', 'pcap', '-c', channel, interface], timeout=seconds)
        print(command.args)
    except subprocess.TimeoutExpired:
        pass
