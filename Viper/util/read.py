import csv
import os


def read_csv(path, directory):
    apfile = directory + '/AP.csv'
    stationsfile = directory + '/Station.csv'

    with open(path, 'r') as f:
        lines = f.read()

    with open(apfile, 'w') as f:
        flag = False
        for i in lines.split('\n\n')[0].split('\n')[1:]:
            if not flag:
                f.write(i.replace(' ', '') + '\n')
                flag = True
            f.write(i + '\n')

    with open(stationsfile, 'w') as f:
        flag = False
        for i in lines.split('\n\n')[1].split('\n'):
            if not flag:
                f.write(i.replace(' ', '') + '\n')
                flag = True
            f.write(i + '\n')

    reader = csv.DictReader(open(apfile, 'r'))

    ap_list = []

    for line in reader:
        ap_list.append(line)

    reader = csv.DictReader(open(stationsfile, 'r'))

    station_list = []

    for line in reader:
        station_list.append(line)

    for i in ap_list:
        for key in i:
            if key == 'ESSID':
                pass
            i[key].replace(' ', '')

    for i in station_list:
        for key in i:
            if key == 'Probes':
                pass
            if isinstance(i, str):
                i[key].replace(' ', '')

    return ap_list, station_list
