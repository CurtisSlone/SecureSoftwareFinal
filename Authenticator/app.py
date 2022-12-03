"""
File: app.py
Author: Curtis Slone
Date: 01 Dec 2022
Description: Flask App that authenticates x509 digital identities. Uses JWT to manage sessions.
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
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
context.load_cert_chain("../TestCerts/Component/auth-scada.crt","../TestCerts/Component/auth-scada.key")
serving.run_simple("0.0.0.0", 2443, app, ssl_context=context)