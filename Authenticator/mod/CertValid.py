from mod.TLSReq import TLSReq
from mod.TLSListener import TLSListener
class CertValid(TLSListener):
    """
    Authenticator Server receive creds from FrontEnd
    """
    def __init__(self,certDetails):
        """
        Constructor
        """
        TLSListener.__init__(self,4443,'./certs/auth-scada.crt','./certs/auth-scada.key','./certs/clients.crt')
        print("running")
        self.__certDetails = certDetails
    def listenerFunction(self):
        """
        Function unique to each TLS Listener instance
        """
        print("TEST")
        if self.exposeData() == b'True':
            """
            ## Allow FrontEnd authentication
            ## Connect Datastore to FrontEnd with Connection Policies
            """
            print("success")
        else:
            print("fail")
            return "Authentication Failed"