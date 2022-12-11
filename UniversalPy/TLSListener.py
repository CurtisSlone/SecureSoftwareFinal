import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl
from abc import abstractmethod
class TLSListener:
    """
    Authenticator Server receive creds from FrontEnd
    """
    def __init__(self,port,serverCert,serverKey,clientsCrt):
        """
        Constructor
        """
        self.__listen_addr = '127.0.0.1' 
        self.__listen_port = port 
        self.__server_cert = serverCert
        self.__server_key = serverKey
        self.__client_certs = clientsCrt
        self.__context = self.__buildContext()
        self.__bindsocket = self.__buildSocket()
        self.__buffer = b''
        self.__data = ""
        self.__status = True
        self.__connect()
    def __buildContext(self):
        """
        Build context
        """
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_cert_chain(certfile=self.__server_cert, keyfile=self.__server_key)
        context.load_verify_locations(cafile=self.__client_certs)
        return context
    def __buildSocket(self):
        """
        Build Socket
        """
        bindsocket = socket.socket()
        bindsocket.bind((self.__listen_addr, self.__listen_port))
        return bindsocket
    def __connect(self):
        """
        Open Connection
        """
        self.__bindsocket.listen(5)
        while self.__status:
            print("Waiting for client on port: "+str(self.__listen_port))
            newsocket, fromaddr = self.__bindsocket.accept()
            self.__connection = self.__context.wrap_socket(newsocket, server_side=True)
            self.__listen()
    def __listen(self):
        try:
            while self.__status:
                data = self.__connection.recv(4096)
                if data:
                    # Client sent us data. Append to buffer
                    self.__buffer += data
                else:
                    # No more data from client. Show buffer and close connection.
                    self.__data = self.__buffer.decode('utf-8')
                    break
        finally:
            absFunc = self.listenerFunction()
            del absFunc
            self.__close()
    def __close(self):
        "Kill connection"
        self.__status = False
        try:
            self.__connection.shutdown(socket.SHUT_RDWR)
            self.__connection.close()
        except OSError:
            print("Connection Closed")
    def exposeData(self):
        """
        Publicly Access Data
        """
        return self.__data
    @abstractmethod
    def listenerFunction(self):
        """
        Function unique to each TLS Listener instance
        """
        ...