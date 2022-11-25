"""
File: app.py
Author: Curtis Slone
Date: 11 Nov 2022
Description: REST app that allows x509 authenticated users to view temperature and humidity data ingested from various industrial sensors 
and allows authenticated administrators to update sensor information
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
context.load_cert_chain("simple.org.crt","simple.org.key")
serving.run_simple("0.0.0.0", 8000, app, ssl_context=context)