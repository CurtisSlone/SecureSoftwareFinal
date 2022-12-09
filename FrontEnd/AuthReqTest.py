from mod.AuthReq import AuthReq

authreq = AuthReq()

authreq.connect()
authreq.send()
authreq.send()
authreq.close()