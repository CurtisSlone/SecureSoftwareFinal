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
        TLSListener.__init__(self,2443,'./certs/auth-scada.crt','./certs/auth-scada.key','./certs/clients.crt')
    def listenerFunction(self):
        """
        Function unique to each TLS Listener instance
        """
        print("received creds, forwarding")
        return TLSReq(3443,'cert.scada.local','./certs/cert-scada.crt','./certs/auth-scada.crt','./certs/auth-scada.key',self.exposeData())
    