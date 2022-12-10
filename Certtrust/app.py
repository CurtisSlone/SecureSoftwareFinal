from mod.RecvAuth import RecvAuth
while True:
    recv = RecvAuth()
    print(recv.exposeData())
    del recv