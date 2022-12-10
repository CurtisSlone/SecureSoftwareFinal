import socket
import ssl

class ProxyAuth:
    """
    Proxy Authentication Information to Certtrust for verification
    Based on TLSReq
    """
    def __init__(self,authJson): #Data depends on process used
        """
        Constructor
        """
        self.__host_addr = '127.0.0.1'
        self.__host_port = 3443 #Change based on process
        self.__server_sni_hostname = 'cert.scada.local' #Change based on process
        self.__server_cert = './certs/cert-scada.crt' #Change based on process
        self.__client_cert = './certs/auth-scada.crt' #Change based on process
        self.__client_key = './certs/auth-scada.key' #Change based on process
        self.__connection = self.__buildConnection()
        self.__data = authJson #Change based on process
        self.__connect()
        self.__send(str.encode(self.__data))
        self.__close()

    def __buildConnection(self):
        """
        Init connection
        """
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=self.__server_cert)
        context.load_cert_chain(certfile=self.__client_cert, keyfile=self.__client_key)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return context.wrap_socket(s, server_side=False, server_hostname=self.__server_sni_hostname)
    def __connect(self):
        """
        Connect
        """
        self.__connection.connect((self.__host_addr, self.__host_port))
    def __send(self,data):
        """
        send
        """
        self.__connection.send(bytes(data))
    def __close(self):
        """
        Close Connection
        """
        self.__connection.close()