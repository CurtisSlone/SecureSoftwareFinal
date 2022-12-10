import socket
import ssl
import json

class AuthReq:
    """
    Proxy Authentication Information to Certtrust for verification
    """
    def __init__(self,serial,ou,sig): #Data depends on process used
        """
        Constructor
        """
        self.__host_addr = '127.0.0.1'
        self.__host_port = 2443 #Change based on process
        self.__server_sni_hostname = 'auth.scada.local' #Change based on process
        self.__server_cert = './certs/auth-scada.crt' #Change based on process
        self.__client_cert = './certs/web-scada.crt' #Change based on process
        self.__client_key = './certs/web-scada.key' #Change based on process
        self.__connection = self.__buildConnection()
        self.__data = self.__buildAuth(serial,ou,sig) #Change based on process
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
    def __buildAuth(self,serial,ou,sig): #Change based on process, use case for abstraction and inheritence
        """
        Build Authorization JSON
        """
        return json.dumps({"serial":serial,"ou":ou,"signature":sig})