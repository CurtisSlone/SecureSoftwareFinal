from mod.TLSReq import TLSReq
from mod.TLSListener import TLSListener

class AuthRecv(TLSListener):
    """
    Authenticator Server receive creds from FrontEnd
    """
    def __init__(self):
        """
        Constructor
        """
        TLSListener.__init__(self,2443,'./certs/auth-scada.crt','./certs/auth-scada.key','./certs/clients.crt',)
    def __listenerFunction(self):
        """
        Function unique to each TLS Listener instance
        """
        return TLSReq(3443,'cert.scada.local','./certs/cert-scada.crt','./certs/auth-scada.crt','./certs/auth-scada.key',self.__data)