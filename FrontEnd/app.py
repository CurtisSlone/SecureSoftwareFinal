"""
File: app.py
Author: Curtis Slone
Date: 11 Nov 2022
Description: FrontEnd app that allows x509 authenticated users to view temperature and humidity data ingested from various industrial sensors 
and allows authenticated administrators to update sensor information
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
from mod.PreLoad import PreLoad
from datetime import datetime
from werkzeug import serving
import ssl
import base64
from mod.PreLoad import PreLoad
from mod.CertIngest import CertIngest
from mod.PrivKeyIngest import PrivKeyIngest
from mod.TLSReq import TLSReq
import json
####################
### App Declarations
####################
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
    sig = base64.b64encode(key.sign(cert.getHash()))
    ou = cert.getOU()
    serial = cert.getSerial()
    
    return f"N/A"
#############
#### Add TLS
#############
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("./certs/web-scada.crt","./certs/web-scada.key")
serving.run_simple("0.0.0.0", 1443, app, ssl_context=context)