from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("../testcerts/fred-user-id.key","rb") as keyfile:
    private_key = serialization.load_pem_private_key(
        keyfile.read(),
        password=b'12345678'
    )

cert = x509.load_pem_x509_certificate(open("../testcerts/fred-user-id.crt",'rb').read())
public_key = cert.public_key()

#Assert?
isinstance(public_key, rsa.RSAPublicKey)

#Encrypt Data
message=b'message'
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
