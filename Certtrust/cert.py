from CertIngest import CertIngest

fred = "../TestCerts/User/fred-adm.crt"
FredCert = CertIngest(fred)

print(FredCert.getHash())