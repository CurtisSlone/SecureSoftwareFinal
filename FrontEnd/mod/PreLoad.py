import os

class PreLoad:
    """
    Preload available cert/key pairs for FrontEnd
    """
    def __init__(self):
        """
        Init Preloaded value
        """
        self.__dnListing = [
            {
                "dn": "fred-adm",
                "certpath": "../TestCerts/User/fred-adm.crt",
                "keypath": "../TestCerts/User/fred-adm.key"
            },
            {
                "dn": "fred-user",
                "certpath": "../TestCerts/User/fred-user.crt",
                "keypath": "../TestCerts/User/fred-user.key"
            }
        ]
    def getDNListing(self):
        """
        Publicly expose dnListing
        """
        return self.__dnListing
    def matchInfo(self,name):
        """
        Method that received dn and matches 
        """
        for  dn in self.__dnListing:
            if name == dn['dn']:
                return dn
        return {}        
        
