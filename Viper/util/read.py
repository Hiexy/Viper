import csv
import json


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

def add_wps(ap_list, wash_path):
    with open(wash_path, 'r') as f:
        aps = f.read().split('\n')[:-1]
    
    wash_ap = []
    for i in aps:
        wash_ap.append(json.loads(i))
    
    for i in wash_ap:
        for j in ap_list:
            if i['bssid'].lower() == j['BSSID'].lower():
                j['WPS'] = float(i['wps_state'])
    
    return ap_list
    

