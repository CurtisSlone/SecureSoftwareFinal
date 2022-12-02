from cryptography import x509
import pem
with open('test_certs/identity-ca-chain.pem', 'rb') as f:
    pem_data = pem.parse(f.read())
print(pem_data)
# cert = x509.load_pem_x509_certificate(pem_data)
# cert.serial_number