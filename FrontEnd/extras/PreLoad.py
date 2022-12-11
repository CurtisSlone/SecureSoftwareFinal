"""
"""
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
                "certpath": "../TestCerts/fred-adm.crt",
                "keypath": "../TestCerts/fred-adm.key"
            },
            {
                "dn": "fred-user",
                "certpath": "../TestCerts/fred-user.crt",
                "keypath": "../TestCerts/fred-user.key"
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
        
