from mod.TLSListener import TLSListener
from mod.ProcessAuth import ProcessAuth

class RecvAuth(TLSListener):
    """
    Receive Proxied Authenticator Information
    Inherits from TLSListener
    """
    def __init__(self):
        """
        Constructor
        """
        TLSListener.__init__(self,3443,'./certs/cert-scada.crt','./certs/cert-scada.key','./certs/clients.crt')
    def listenerFunction(self):
        """
        Function unique to each TLS Listener instance
        """
        return ProcessAuth(self.exposeData())