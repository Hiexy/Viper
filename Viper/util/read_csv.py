import csv
import os

def read_csv(path):

    if not os.path.isdir(path.split('.')[0]):
        os.mkdir(path.split('.')[0])
    apfile = '/AP.'.join(_ for _ in path.split('.'))
    stationsfile = '/Station.'.join(_ for _ in path.split('.'))

    with open(path, 'r') as f:
        lines = f.read()

    with open(apfile, 'w') as f:
        for i in lines.split('\n\n')[0].split('\n')[1:]:
            f.write(i + '\n')
    
    with open(stationsfile, 'w') as f:
        for i in lines.split('\n\n')[1].split('\n'):
            f.write(i + '\n')
    

    reader = csv.DictReader(open(apfile, 'r'))

    ap_list = []

    for line in reader:
        ap_list.append(line)

    reader = csv.DictReader(open(stationsfile, 'r'))

    station_list = []

    for line in reader:
        station_list.append(line)

    return ap_list, station_list