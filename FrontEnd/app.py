"""
File: app.py
Author: Curtis Slone
Date: 11 Nov 2022
Description: FrontEnd app that allows x509 authenticated users to view temperature and humidity data ingested from various industrial sensors 
and allows authenticated administrators to update sensor information
"""
import ssl
import base64
import json
from flask import Flask, render_template, request, jsonify
from extras.PreLoad import PreLoad
from datetime import datetime
from werkzeug import serving
from extras.UserIngest import UserIngest
from flask_login import LoginManager, login_required, current_user, login_user, logout_user, UserMixin
from models.UserModel import UserModel
####################
### App Declarations
####################
app = Flask(__name__)
app.secret_key = "SECRET"
login_manager = LoginManager()
login_manager.init_app(app)
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
    userObject = UserIngest(current['certpath'],current['keypath'],pin)
    if userObject.isUnlocked():
        """
        Create User Model for authentication
        """
        current = UserModel(dn,userObject.shareOU())
        login_user(current)
    return jsonify({'success': "Authenticated."})
#################
## USER LOADER ##
#################
@login_manager.user_loader
def load_user(userObject):
    """
    
    """
    return userObject
#############
#### Add TLS
#############
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("./certs/web-scada.crt","./certs/web-scada.key")
serving.run_simple("0.0.0.0", 1443, app, ssl_context=context)