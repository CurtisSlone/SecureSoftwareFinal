import requests

class BuildAuthReq:
    """
    Class to build Authentication Requests to be sent to Authenticator
    """
    def __init__(self,serial,ou,sig):
        """
        Constructor
        """
        self.__authServer = "https://localhost:2443"
        self.__serial = serial
        self.__ou = ou
        self.__sig = sig
        self.__contentType = "application/json"
        