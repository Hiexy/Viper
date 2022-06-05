from turtle import st
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from Viper.attack.wep import wep_crack, wep_crack_no_ivs
from Viper.attack.wpa import wpa_crack
from . import viper
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        try:
            time_s = int(request.form.get('time'))
        except:
            flash('Input is not a number!')
            return render_template("home.html", user=current_user)

        viper.scan(time_s)
        networks = viper.ap
        # print(networks)
        return render_template('scanning.html', networks=networks)

    if viper.ap:
        networks = viper.ap
        return render_template('scanning.html', networks=networks)

    return render_template('scanning.html')


@views.route('/attack', methods=['GET', 'POST'])
def attack():
    if request.method == 'POST':
        bssid = request.form.get('BSSID')
        if not bssid:
            return render_template('attacking.html')

        for i in viper.ap:
            if bssid.lower() in i['BSSID'].lower():
                ap = i
                break

        stations = []
        for i in viper.stations:
            if bssid.lower() in i['BSSID'].lower():
                stations.append(i)

        attacks = ''

        # if ap['WPS']:
        #     attacks += 'WPS,'

        if 'WEP' in ap['Privacy']:
            attacks += 'IVs, Dictionary Attack'
            method = 'wep'

        if 'WPA' in ap['Privacy']:
            attacks += 'aircrack-ng, COWPATTY'
            method = 'wpa'

        if 'MGT' in ap['Authentication']:
            attacks = 'ASLEAP, eapmd5crack'
            method = 'mgt'

        return render_template('attacking.html', stations=stations, network=ap, attacks=attacks, method=method)

    return render_template('attacking.html')


@views.route('/attack/wep', methods=['POST'])
def attack_wep():
    bssid = request.form.get('BSSID')
    station = request.form.get('stationMAC')
    seconds = int(request.form.get('time'))
    dictionary = request.form.get('dictionary')

    if dictionary == 'rockyou':
        dictionary = '/home/kali/Documents/Viper/wordlists/rockyou.txt'
    elif dictionary == 'numbers':
        dictionary = '/home/kali/Documents/Viper/wordlists/jordanian_numbers'

    orignial_time = seconds
    for i in viper.ap:
        if bssid.lower() in i['BSSID'].lower():
            ap = i
            break

    print(ap)
    ctr = 1
    while ctr < 4:
        seconds = orignial_time * ctr
        print(f'Running WEP Crack IVs {ctr}')
        print(viper.interface, bssid, station,
              ap['channel'], viper.directory, seconds, ctr)
        password = wep_crack(viper.interface, bssid, station,
                             ap['channel'], viper.directory, seconds, ctr)
        if password:
            method = 'IVs'
            return redirect(f"/results?BSSID={bssid}&method={method}&password={password}")
        else:
            ctr += 1
    print(f'Running WEP Crack dictionary')
    password = wep_crack_no_ivs(f'{viper.directory}/wep', dictionary)
    if password:
        method = 'Dictionary Attack'
        return redirect(f"/results?BSSID={bssid}&method={method}&password={password}")

    else:
        flash('Password not found.', category='error')
        return redirect("/")


@views.route('/attack/wpa', methods=['POST'])
def attack_wpa():
    bssid = request.form.get('BSSID')
    station = request.form.get('stationMAC')
    seconds = int(request.form.get('time'))
    dictionary = request.form.get('dictionary')
    deauths = request.form.get('deauth')

    if dictionary == 'rockyou':
        dictionary = '/home/kali/Documents/Viper/wordlists/rockyou.txt'
    elif dictionary == 'numbers':
        dictionary = '/home/kali/Documents/Viper/wordlists/jordanian_numbers'
    
    for i in viper.ap:
        if bssid.lower() in i['BSSID'].lower():
            ap = i
            break
    
    print(viper.interface, deauths, bssid, station, ap['channel'], viper.directory, dictionary, seconds)
    password = wpa_crack(viper.interface, deauths, bssid, station, ap['channel'], viper.directory, dictionary, seconds)

    if password:
        method = 'aircrack-ng'
        return redirect(f"/results?BSSID={bssid}&method={method}&password={password}")

    else:
        flash('Password not found.', category='error')
        return redirect(f"/")

@views.route('/results', methods=['GET', 'POST'])
def results():
    bssid = request.args.get('BSSID')
    method = request.args.get('method')
    password = request.args.get('password')
    if bssid:
        for i in viper.ap:
            if bssid.lower() in i['BSSID'].lower():
                ap = i
                break
        if password:
            return render_template('results.html', network=ap, method=method, password=password)
        else:
            return render_template('results.html', network=ap, method='All methods failed', password='Password Not Cracked')
    return 'No AP attacked, please retry'
