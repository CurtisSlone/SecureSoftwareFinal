"""

"""
from extras.CertIngest import CertIngest
from extras.PrivKeyIngest import PrivKeyIngest
class UserIngest:
    """
        Object for user attempting to log in
    """
    def __init__(self,certPath,keyPath,pin):
        """
            Constructor
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
            Expose OU to authentication model to implement authorized roles
        """
        return self.__cert.getOU()
    def shareSerial(self):
        """
            Expose digital identity serial for user 'ID' as required by flask-login
        """
        return self.__cert.getSerial()
    def __validatePinAsNumbers(self):
        """
            Validate that pin entered is digits only
        """
        return self.__pin.isdigit()
    def isUnlocked(self):
        """
        Validates correct pin was entered
        """
        return self.__unlocked