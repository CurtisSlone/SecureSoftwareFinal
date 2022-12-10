"""
"""
import json
from mod.CertIngest import CertIngest
import base64
from cryptography.exceptions import InvalidSignature
class ProcessAuth:
    """
    Process auth JSON for user authentication
    """
    def __init__(self,json):
        """
        Constructor
        """
        self.__json = json
        self.__reqSerial = self.__getJSONSerial(self.__json)
        self.__reqSig = self.__getJSONSig(self.__json)
        self.__matchedCertFile = self.__locateMatch()
        self.__matchedCert = CertIngest(self.__matchedCertFile)
        self.__matched = False
        self.__validateSig()
    def __getJSONSerial(self,jsonObj):
        """
        Get Serial from JSON
        """
        j = json.loads(jsonObj)
        return j["serial"]
    def __getJSONSig(self,jsonObj):
        """
        Get Sig from JSON
        """
        j = json.loads(jsonObj)
        return j["signature"]
    def __locateMatch(self):
        """
        Parse certtrust.json file, match serial, return filepath 
        """
        with open('./static/certtrust.json','rb') as f:
            """
            load JSON from file
            """
            certtrust = json.load(f)
            for cert in certtrust["certtrust"]:
                """
                Parse for comparison
                """
                if cert["serial"] == self.__reqSerial:
                    return cert["file"]
    def __validateSig(self):
        """
        Validate sig
        """
        sig = base64.b64decode(self.__reqSig)
        message = self.__matchedCert.getHash().encode()
        try:
            self.__matchedCert.verifySig(sig,message)
        except InvalidSignature:
            return "Invalid signature"
        else:
            self.__matched = True
        finally:
            return "complete"
    def isMatched(self):
        """
        Share matched
        """
        return self.__matched