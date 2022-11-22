"""
File: app.py
Author: Curtis Slone
Date: 11 Nov 2022
Description: REST app that allows x509 authenticated users to view temperature and humidity data ingested from various industrial sensors 
and allows authenticated administrators to update sensor information
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)

#################
### ROUTES ###
#################
@app.route('/')
def home():
    """Return Homepage"""
    return render_template('home.html')