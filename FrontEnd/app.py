"""
File: app.py
Author: Curtis Slone
Date: 11 Nov 2022
Description: FrontEnd app that allows x509 authenticated users to view temperature and humidity data ingested from various industrial sensors 
and allows authenticated administrators to update sensor information
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
import ssl
from werkzeug import serving
from mod.PreLoad import *
app = Flask(__name__)
preload = PreLoad()
dnList = preload.getDNListing()
#################
### ROUTES ###
#################
@app.route('/')
def home():
    """Return Homepage"""
    return render_template('home.html', list=dnList)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("../TestCerts/Component/web-scada.crt","../TestCerts/Component/web-scada.key")
serving.run_simple("0.0.0.0", 1443, app, ssl_context=context)