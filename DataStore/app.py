"""
File: app.py
Author: Curtis Slone
Date: 03 DEC 2022
Description: Flask API that exposes SCADA device data
"""
from flask import Flask, request, jsonify, redirect, url_for
import ssl
from werkzeug import serving
app = Flask(__name__)

#################
### ROUTES ###
#################
@app.route('/')
def home():
    """Return Homepage"""
    return "hello"

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("../TestCerts/Component/data-scada.crt","../TestCerts/Component/cert-scada.key")
serving.run_simple("0.0.0.0", 4443, app, ssl_context=context)