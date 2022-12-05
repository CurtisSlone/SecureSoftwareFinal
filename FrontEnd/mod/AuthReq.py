import socket
import ssl

class AuthReq:
    """
    Class to build TLS connection and send Authorization Request JSON data
    """
    def __init__(self,serial,ou,sign):
        """
        Constructor
        """
        self.__addr = '127.0.0.1'
        self.__port = 2443
        self.__server_sni_host = 'auth.scada.local'
        self.__server_cert = '../certs/auth-scada.crt'
        self.__client_cert = '../certs/web-scada.crt'
        self.__client_key = '../certs/web-scada.key'
        self.__context = self.__createContext()
        self.__connection = self.__createConnection()
    def __createContext(self):
        """
        Create TLS context
        """
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=self.__server_cert)
        return context.load_cert_chain(certfile=self.__client_cert, keyfile=self.__client_key)
    def __createConnection(self):
        """
        Create socket & connection
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self.__context.wrap_socket(s, server_side=False, server_hostname=self.__server_sni_host)
    def connect(self):
        """
        Connect
        """
        self.__connection.connect((self.__addr, self.__port ))
        return 
    def sendData(self,data):
        """"
        Send data to peer
        """
        self.__connection.send(data)
        return
    def closeConnection(self):
        """
        Kill Connection
        """
        self.__connection.close()
        return
