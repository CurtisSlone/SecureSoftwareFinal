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
        self.__server = "https://localhost:2443"
        self.__headers = ""
        self.__data = self.__buildData(serial,ou,sig)
    def __buildData(self,serial,ou,sig):
        """
        Build data json
        """
        return {'serial': serial, 'ou': ou, 'signature': sig}
    def __getData(self):
        """
        Publicly Expose Data
        """
        return self.__data
    def sendRequest(self):
        """
        Send Data
        """
        return ""