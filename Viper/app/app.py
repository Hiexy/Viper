from flask import Flask,render_template,request,redirect
from flask_assets import Environment,Bundle, assets
from webassets import bundle
import os
import requests, json
import mysql.connector
from jsql import render, sql
from pprint import pprint
from sqlalchemy import create_engine
from werkzeug.datastructures import ContentRange
from werkzeug.utils import redirect

app = Flask(__name__)


bundle = {
    "bootstrap.css":Bundle('css/bootstrap.css',output = 'gen/bootstrap.css'),
    "theme.css":Bundle('css/theme.css',output = 'gen/theme.css'),
}

assets = Environment(app)
assets.register(bundle)
DATABASE_NAME = "senproj" #os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = "" #os.getenv("DATABASE_PASSWORD")
DATABASE_USER = "root" #os.getenv("DATABASE_USER")
DATABASE_HOST = "127.0.0.1" #os.getenv("DATABASE_HOST")

engine = create_engine(f'mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}')

def database_query():


    #sql is from jsql which is a tool developed by CTO of noon, to handle alot of sql related security checks, like sql injection and more.
    # it takes connection object, sql query, and paramaters if any.
    # it is followed by one of these:
    # .scalar() to return a single value.
    # .dict() to return a single row.
    # .dicts() to return a list of rows.
    # .lastrowid returns the last row id that was created.
    # and more but I didn't need them yet.
    # product="""     
    #     INSERT INTO paper_bags_products VALUES (data['ptype'],data['weight'],data['quantity'], data['dimension'],data['normn'],data['normf'],data['pantn'],data['pantf'],data['metn'],data['metf'],data['heat'],data['tajleed'],data['handle'],data['base']
    # """
    # if you want to insert a paramater just use ":" followed by the paramater name you specified in the paramaters section.
    # WHERE token = :token  <-- here
    # here --> ,token="hello").scalar()



    return


@app.route('/login',methods=['GET','POST'])
def login_user():
    if request.form:

        conn = engine.connect()
        transaction = conn.begin()
      
        data = request.form
        print(data)
        available = sql(conn,'''
        SELECT
            *
        FROM
            `cred`
        WHERE
            username = :username AND password = :password
        ''', **data).dict()
        
        if available:
            return redirect(f'/scanning')
        
        print(available)
        conn.close()
    return render_template('loginpage.html')


@app.route('/scanning',methods=['GET','POST'])
def scan_me():
    networks=[ {'WPS':'2.0','BSSID': '18:3C:B7:1F:2E:D2', 'Firsttimeseen': ' 2022-05-29 16:04:35', 'Lasttimeseen': ' 2022-05-29 16:04:35', 'channel': ' 13', 'Speed': ' 130',
 'Privacy': ' WPA2', 'Cipher': ' CCMP', 'Authentication': 'PSK', 'Power': ' -73', '#beacons': '        1', '#IV': '        0', 'LANIP': '   0.  0.  0.  0', 'ID-length': '  20', 'ESSID': ' Umniah-evo-Home-2ED2',
 'Key': ' '}, {'WPS':'2.0','BSSID': 'EC:89:14:29:C9:B2', 'Firsttimeseen': ' 2022-05-29 16:04:44', 'Lasttimeseen': ' 2022-05-29 16:04:44', 'channel': '  7', 'Speed': ' 270', 'Privacy': ' WPA2',
 'Cipher': ' CCMP', 'Authentication': ' PSK', 'Power': ' -71', '#beacons': '        2', '#IV': '        0', 'LANIP': '   0.  0.  0.  0', 'ID-length': '  20', 'ESSID': ' Umniah-evo-Home-C9B2', 'Key': ' '},
 {'BSSID': '6C:A4:D1:EB:98:C8', 'Firsttimeseen': ' 2022-05-29 16:0 4:34', 'Lasttimeseen': ' 2022-05-29 16:04:44', 'channel': '  1', 'Speed': ' 130', 'Privacy': ' WPA2 WPA', 'Cipher': ' CCMP', 'Authentication': ' PSK',
 'Power': ' -66', '#beacons': '        4', '#IV': '        0', 'LANIP': '   0.  0.  0.  0', 'ID-length': '   9', 'ESSID': ' fh_eb98c8', 'Key': ' '}, {'WPS':'2.0','BSSID': 'E8:01:8D:47:22:F8', 'Firsttimeseen': ' 2022-05-29 16:04:34',
 'Lasttimeseen': ' 2022-05-29 16:04:44', 'channel': '  1', 'Speed': ' 405', 'Privacy': ' WPA2 WPA', 'Cipher': ' CCMP', 'Authentication': ' PSK', 'Power': ' -66', '#beacons': '        5', '#IV': '        6',
 'LANIP': '   0.  0.  0.  0', 'ID-length': '  17', 'ESSID': ' Umniah Fiber_22f8', 'Key': ' '}, {'WPS':'2.0 PBC, KPAD','BSSID': 'C8:EA:F8:86:FA:4D', 'Firsttimeseen': ' 2022-05-29 16:04:34', 'Lasttimeseen': ' 2022-05-29 16:04:34',
 'channel': '  1', 'Speed': ' 130', 'Privacy': ' WPA2', 'Cipher': ' CCMP', 'Authentication': ' PSK', 'Power': ' -65', '#beacons': '        3', '#IV': '        0', 'LANIP': '   0.  0.  0.  0', 'ID-length': '  11',
 'ESSID': ' Airbox-FA4D', 'Key': ' '}, {'WPS':'2.0 LAB','BSSID': 'E8:01:8D:46:29:10', 'Firsttimeseen': ' 2022-05-29 16:04:34','Lasttimeseen': ' 2022-05-29 16:04:34', 'channel': '  1', 'Speed': ' 195', 'Privacy': ' WPA2 WPA',
 'Cipher': ' CCMP', 'Authentication': ' PSK', 'Power': ' -61', '#beacons': '        1', '#IV': '        0', 'LANIP': '   0.  0.  0.  0', 'ID-length': '  12', 'ESSID': ' 04FAT_462910', 'Key': ' '}, {'BSSID': '62:02:71:D7:A0:3C',
 'Firsttimeseen': ' 2022-05-29 16:04:39', 'Lasttimeseen': ' 2022-05-29 16:04:40', 'channel': '  4', 'Speed': ' 130', 'Privacy': 'WPA', 'Cipher': ' CCMP', 'Authentication': ' MGT', 'Power': ' -58', '#beacons': '        2',
 '#IV': '        0', 'LANIP': '   0.  0.  0.  0', 'ID-length': '   1', 'ESSID': '   TEST', 'Key': ' '}, {'WPS':'2.0 ETH, LAB','BSSID': 'E0:1F:ED:55:73:08', 'Firsttimeseen': ' 2022-05-29 16:04:34', 'Lasttimeseen': ' 2022-05-29 16:04:44',
 'channel': '  1', 'Speed': ' 130', 'Privacy': ' WPA2', 'Cipher': ' CCMP', 'Authentication': ' PSK', 'Power': ' -52', '#beacons': '        4', '#IV': '        1', 'LANIP': '   0.  0.  0.  0', 'ID-length': '  16',
 'ESSID': ' OrangeFiber-7308', 'Key': ' '},  {'WPS':'2.0 LAB','BSSID': 'E4:C3:2A:91:BB:D7', 'Firsttimeseen': ' 2022-05-29 16:04:39', 'Lasttimeseen': ' 2022-05-29 16:04:40',
 'channel': '  4', 'Speed': ' 195', 'Privacy': ' WPA2', 'Cipher': ' CCMP', 'Authentication': ' PSK', 'Power': ' -14', '#beacons': '        3', '#IV': '        1', 'LANIP': '   0.  0.  0.  0', 'ID-length': '  12',
 'ESSID': ' TP-Link_BBD7', 'Key': ' '}]


 
    return render_template('scanning.html',networks=networks)


@app.route('/attacking',methods=['GET','POST'])
def attack_me():
    stations=[{'StationMAC': '16:37:82:15:E6:E2', 'Firsttimeseen': ' 2022-05-26 08:56:17', 'Lasttimeseen': ' 2022-05-26 08:56:17', 'Power': ' -66', '#packets': '        2', 'BSSID': 'TEST', 'ProbedESSIDs': ''}]
    return render_template('attacking.html',stations=stations)


@app.route('/results',methods=['GET','POST'])
def results():
    network={'BSSID': '62:02:71:D7:A0:3C', 'Firsttimeseen': ' 2022-05-29 16:04:39', 'Lasttimeseen': ' 2022-05-29 16:04:40', 'channel': '  4', 'Speed': ' 130', 'Privacy': 'WPA', 'Cipher': ' CCMP', 'Authentication': ' MGT', 'Power': ' -58', '#beacons': '        2','#IV': '        0', 'LANIP': '   0.  0.  0.  0', 'ID-length': '   1', 'ESSID': '   TEST', 'Key': ' '}
    return render_template('results.html',network=network)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
