import socket
import ssl
import json

class TLSReq:
    """
    Client to authorization server
    """
    def __init__(self,port,host,serverCert,clientCert,clientKey,data,identity):
        """
        Constructor
        """
        self.__host_addr = '127.0.0.1'
        self.__host_port = port 
        self.__server_sni_hostname = host 
        self.__server_cert = serverCert 
        self.__client_cert = clientCert 
        self.__client_key = clientKey 
        self.__identity = identity
        self.__connection = self.__buildConnection()
        self.__data = data
        self.__connect()
        self.__send(str.encode(self.__buildReq()))
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
        print(data)
        self.__connection.send(bytes(data))
    def __close(self):
        """
        Close Connection
        """
        self.__connection.close()
    def __buildReq(self):
        """
        Build request 
        """
        req = json.loads(self.__data)
        return json.dumps({
            "identity": self.__identity,
            "req": req
            })