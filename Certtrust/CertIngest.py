import hashlib
import base64
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes, padding

class CertIngest:
    """
    """
    def __init__(self,crtpath):
        self.__crt = open(crtpath, "rb")
        self.__crtobj = x509.load_der_x509_certificate(self.__crt.read())
        self.__hash = self.__cert2hash()
        self.__publicKey = self.__crtobj.public_key()
    def __cert2hash(self):
        """
        Hash Base64 Encoding of self.__crtobj
        """
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: self.__crt.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()
    def getHash(self):
        """
        Publicly expose hash
        """
        return self.__hash
    def encrypt(self,data):
        """
        Encrypt bytes
        """
        return self.__publicKey.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
        )