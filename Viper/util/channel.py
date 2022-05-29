import subprocess


def change_channel(interface, channel):
    """
    Set interface to a specific channel
    """
    subprocess.run(['iwconfig', interface, 'channel', channel],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
