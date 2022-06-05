import subprocess
import os
import time


def scan_aps(interface, seconds):
    """
    Scan access points and stores results in a csv file.
    """
    parent_dir = os.getcwd()
    directory = 'results/'
    path = os.path.join(parent_dir, directory)
    fname = f'results_{time.time_ns()}'
    fpath = f'{path}{fname}'

    if not os.path.isdir(path):
        os.mkdir(path)

    if not os.path.isdir(fpath):
        os.mkdir(fpath)

    fpath = f'{path}{fname}/{fname}'

    try:
        subprocess.run(['airodump-ng', '-w', fpath, '--output-format',
                       'csv', interface], stdout=subprocess.DEVNULL, timeout=seconds)
    except subprocess.TimeoutExpired:
        pass

    try:
        washpath = f'{path}{fname}/wash'
        os.system(f'touch {washpath}')
        f = open(washpath, 'w')
        subprocess.run(['wash', '-i', interface, '-j', '-s'], stdout=f, timeout=seconds)
    except subprocess.TimeoutExpired:
        pass

    return f'{fpath}-01.csv', washpath
