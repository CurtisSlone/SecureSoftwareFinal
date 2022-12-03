"""
File: app.py
Author: Curtis Slone
Date: 03 DEC 2022
Description: Flask API that receives requests from authenticator to validate x509 Digital Identity Signed Hashes.
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
    return render_template('home.html')

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("../TestCerts/Component/cert-scada.crt","../TestCerts/Component/cert-scada.key")
serving.run_simple("0.0.0.0", 3443, app, ssl_context=context)