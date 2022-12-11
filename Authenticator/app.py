from mod.AuthRecv import AuthRecv
from mod.CertValid import CertValid
while True:
    authRecv = AuthRecv()
    tmp = authRecv.exposeData()
    del authRecv
    certValid = CertValid(tmp)
    del certValid