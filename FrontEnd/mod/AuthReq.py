import socket
import ssl

class AuthReq:
    """
    Client to authorization server
    """
    def __init__(self):
        """
        Constructor
        """
        self.__host_addr = '127.0.0.1'
        self.__host_port = 2443
        self.__server_sni_hostname = 'auth.scada.local'
        self.__server_cert = './certs/auth-scada.crt'
        self.__client_cert = './certs/web-scada.crt'
        self.__client_key = './certs/web-scada.key'
        self.__connection = self.__buildConnection()
    def __buildConnection(self):
        """
        Init connection
        """
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=self.__server_cert)
        context.load_cert_chain(certfile=self.__client_cert, keyfile=self.__client_key)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return context.wrap_socket(s, server_side=False, server_hostname=self.__server_sni_hostname)
    def connect(self):
        """
        Connect
        """
        self.__connection.connect((self.__host_addr, self.__host_port))
    def send(self):
        """
        send
        """
        self.__connection.send(b"Test data")
    def close(self):
        """
        Close Connection
        """
        self.__connection.close()