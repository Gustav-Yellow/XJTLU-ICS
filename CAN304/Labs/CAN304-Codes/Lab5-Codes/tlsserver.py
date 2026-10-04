# --- CAN304, CAN409 Lab  -----------------------------------------------------
# Lab 5: The ECC lib and ECDH-based AKA protocols
#
# ECDHE handshake in TLS1.3
# Party B (i.e., the server)
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------

import socket
import time
import random
import hmac

from collections import OrderedDict
from ecc.Key import Key
from hashlib import sha256,md5
from ecc.elliptic import mul,add,neg
from ecc.ecdsa import sign,verify
from ecc.curves import get_curve

DOMAINS = {
    # Bits : (p, order of E(GF(P)), parameter b, base point x, base point y)
    256: (0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
          0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
          0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
          0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
          0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5),
}

if __name__ == '__main__':

    global Ta,Rb,p,n,b,x,y,c_p,c_q,c_n,M1,M2,M3,Kb

    HOST = '127.0.0.1'
    PORT = 9006

    # initialization
    p, n, b, x, y=DOMAINS[256]
    c_p=3
    c_n=p
    c_q=p-b
    token=0

    print('Begin')

    #TCP link
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((HOST,PORT))

    print('Listen to the connection from client...')
    sock.listen(5)
    try:
        while (token==0):
            connection, address = sock.accept()
            print('Connected. Got connection from ', address)

            # 2. B side: 1)receive M1 from A, 2)generate my keypair 3) send M2
            # 2.1) receive M1=(helloA,PKax,PKay) from A
            M1=connection.recv(1024).decode()
            helloA=M1.split(',')[0]
            PKax=M1.split(',')[1]
            PKay=M1.split(',')[2]
            PKa=(int(PKax),int(PKay))
            # 2.2) generate my keypair 
            keypair = Key.generate(256)
            PKbx = keypair._pub[1][0]
            PKby = keypair._pub[1][1]
            SKb = keypair._priv[1]            
            # 2.3) B->A: M2=(helloB,PKbx,PKby)
            M2='helloB'+','+str(PKbx)+','+str(PKby)
            connection.send(M2.encode())


            # 4. B side: 1) receive M3 from A 2) verify ecdsa signature sa 3) compute ecdsa signature sb 4)send M4
            # 4.1) receive M3=sa from A
            M3=connection.recv(1024).decode()
            sa_0=M3.split(',')[0]
            sa_1=M3.split(',')[1]
            sa=(int(sa_0),int(sa_1))
            # 4.2) verify sa
            hstringa=helloA+str(PKax)+str(PKay)
            md5a=md5()
            md5a.update(hstringa.encode())
            ha=md5a.hexdigest()[8:-8] 
            ha=int(ha,16) 
            if verify(ha,sa,(256,(int(PKax),int(PKay))))==True:
                Kb=mul(c_p,c_q,c_n,PKa,SKb)
                # 4.3) compute sb
                hstringb='helloB'+str(PKbx)+str(PKby)
                md5b=md5()
                md5b.update(hstringb.encode())
                hb=md5b.hexdigest()[8:-8]
                hb=int(hb,16) 
                sb=sign(hb,(256,int(SKb)))           
                # 4.4) send M4
                M4=str(sb[0])+','+str(sb[1])
                connection.send(M4.encode())
                print('signature of client is valid')
                print('the shared secrety is', Kb)
            else:
                print('signature of client is invalid, protocol fails')
            token=1

    except KeyboardInterrupt:
        print('>>>quit')
    #sys.exit(0)




