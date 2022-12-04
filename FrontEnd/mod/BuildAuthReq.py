import requests
import json

class BuildAuthReq:
    """
    Class to build Authentication Requests to be sent to Authenticator
    """
    def __init__(self,serial,ou,sig):
        """
        Constructor
        """
        self.__headers = {'Content-type': 'application/json',}
        self.__data = self.__buildData(serial,ou,sig)
    def __buildData(self,serial,ou,sig):
        """
        Build data json
        """
        return {'serial': serial, 'ou': ou, 'signature': sig}
    def getData(self):
        """
        Publicly Expose Data
        """
        return self.__data