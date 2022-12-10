import hashlib
import base64
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
class CertIngest:
    """
    Public Cert Object that hashes base64 encoding of Certificate binary, encrypts data using the public key, and exposes the certificate hash
    """
    def __init__(self,crtpath):
        self.__crtpath = crtpath
        self.__crtobj = self.__setCertObj()
        self.__hash = self.__cert2hash()
        self.__publicKey = self.__crtobj.public_key()
    def __setCertObj(self):
        """
        """
        return x509.load_pem_x509_certificate(open(self.__crtpath,'rb').read())
    def __cert2hash(self):
        """
        Hash Base64 Encoding of Cert Binary
        """
        hash_md5 = hashlib.md5()
        with open(self.__crtpath,'rb') as crt:
            for chunk in iter(lambda: crt.read(4096), b""):
                chunk64 = base64.b64encode(chunk)
                hash_md5.update(chunk64)
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
        return self.__publicKey.encrypt(data,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    def verifySig(self,sig,message):
        """
        Validate digital signature
        """
        return self.__publicKey.verify(sig,message,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256()
        )