from mod.TLSReq import TLSReq
from mod.TLSListener import TLSListener
class AuthListener(TLSListener):
    """
    Authenticator Server receive creds from FrontEnd
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__(2443,'./certs/auth-scada.crt','./certs/auth-scada.key','./certs/clients.crt')
    def listenerFunction(self):
        """
        Function unique to each TLS Listener instance
        """
        requestIdentity, incomingRequest = self.parseReq()
        if requestIdentity == "FrontEnd":
            print(requestIdentity)
            return TLSReq(3443,'cert.scada.local','./certs/cert-scada.crt','./certs/auth-scada.crt','./certs/auth-scada.key',self.exposeData(),'Authenticator')
        elif requestIdentity == 'Certtrust':
            print(requestIdentity)
    