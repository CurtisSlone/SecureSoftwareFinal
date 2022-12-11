from mod.TLSListener import TLSListener
from mod.ProcessAuth import ProcessAuth

class CertListener(TLSListener):
    """
    Receive Proxied Authenticator Information
    Inherits from TLSListener
    """
    def __init__(self):
        """
        Constructor
        """
        self.__requestIdentity, self.__incomingRequest = self.parseReq()
        super().__init__(3443,'./certs/cert-scada.crt','./certs/cert-scada.key','./certs/clients.crt')
    def __listenerFunction(self):
        """
        Function unique to each TLS Listener instance
        """
        requestIdentity, incomingRequest = self.parseReq()
        return ProcessAuth(self.exposeData())