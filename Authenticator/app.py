from mod.AuthRecv import AuthRecv
while True:
    rec = AuthRecv()
    print(rec.exposeData())
    del rec