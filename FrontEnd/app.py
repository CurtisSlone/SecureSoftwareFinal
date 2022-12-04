"""
File: app.py
Author: Curtis Slone
Date: 11 Nov 2022
Description: FrontEnd app that allows x509 authenticated users to view temperature and humidity data ingested from various industrial sensors 
and allows authenticated administrators to update sensor information
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
import ssl
import sys
from mod.PreLoad import *
from datetime import datetime
from mod.CertIngest import *
from mod.PrivKeyIngest import *
app = Flask(__name__)
preload = PreLoad()
dnList = preload.getDNListing()
#################
### ROUTES 
#################
@app.route('/')
def home():
    """Return Homepage"""
    return render_template('home.html', list=dnList)
@app.route('/auth', methods=['POST'])
def auth():
    """
   Authentication
    """
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    dn = request.form['selected-user']
    pin = request.form['pin']
    current = preload.matchInfo(dn)
    cert = CertIngest(current['certpath'])
    key = PrivKeyIngest(current['keypath'],pin)
    hash = cert.getHash()
    signature = key.sign(hash)
    ou = cert.getOU
    serial = cert.getSerial
    return f"{signature}"