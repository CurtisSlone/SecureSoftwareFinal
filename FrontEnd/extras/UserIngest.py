"""

"""
from extras.CertIngest import CertIngest
from extras.PrivKeyIngest import PrivKeyIngest
class UserIngest:
    """
    
    """
    def __init__(self,certPath,keyPath,pin):
        """

        """
        self.__cert = CertIngest(certPath)
        self.__keyPath = keyPath
        self.__pin = pin
        self.__unlocked = False
        self.___unlockKey()
    def ___unlockKey(self):
        """
        Unlock Key using user supplied pin
        """
        if self.__validatePinAsNumbers():
            try:
                self.__key = PrivKeyIngest(self.__keyPath,self.__pin)
                self.__unlocked = True
            except ValueError:
                """

                """
                return False
    def shareOU(self):
        """
        
        """
        return self.__cert.getOU()
    def shareSerial(self):
        """
        
        """
        return self.__cert.getSerial()
    def __validatePinAsNumbers(self):
        """
        
        """
        return self.__pin.isdigit()
    def isUnlocked(self):
        """
        """
        return self.__unlocked