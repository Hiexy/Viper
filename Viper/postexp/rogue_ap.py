import subprocess

def create_rogue_ap(interface, essid, channel):
    subprocess.Popen(['airbase-ng', '-e', essid, '-c', channel, interface])