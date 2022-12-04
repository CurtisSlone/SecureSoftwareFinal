from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa,padding

class PrivKeyIngest:
    """
    Class to ingest private key. Performs decryption and signing actions
    """
    def __init__(self,keyPath,keyPass):
        """
        Constructor
        """
        self.__keyPath = keyPath
        self.__keyPass = keyPass
        self.__privKey = self.__getKeyObj()
    def __getKeyObj(self):
        """
        Extract Key Object
        """
        with open(self.__keyPath,'rb') as keyfile:
            privKey = serialization.load_pem_private_key(keyfile.read(),password=str.encode(self.__keyPass))
        return privKey
    def sign(self,data):
        """
        Signing
        """
        return self.__privKey.sign(str.encode(data),padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())
    def decrypt(self,ciphertext):
        """
        Decryption
        """
        return self.__privKey.decrypt(ciphertext,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))