# --- CAN304, CAN409 Lab  -----------------------------------------------------
# Lab 5: The ECC lib and ECDH-based AKA protocols
#
# ECDHE handshake in TLS1.3
# Party A (i.e., the client)
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------

import socket
import time

from ecc.Key import Key
from hashlib import sha256,md5
from ecc.elliptic import mul,add,neg
from ecc.ecdsa import sign,verify


DOMAINS = {
    # Bits : (p, order of E(GF(P)), parameter b, base point x, base point y)

    256: (0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
          0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
          0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
          0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
          0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5),
}

if __name__== '__main__':

    global Ra,Tb,p,n,b,x,y,c_p,c_q,c_n,M1,M2,M3,Ka,macb
    server_ip = "127.0.0.1"
    server_port = 9006

    # initialization
    p, n, b, x, y = DOMAINS[256]
    c_p = 3
    c_n = p
    c_q = p - b
    token=0

    
    # TCP connection to responder B
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(1)  
    print('begin connection')
    sock.connect((server_ip, server_port))
    
    try:
        while (token==0):
            print('connection up')
            print ('connected')
            # 1. A side: send M1=(helloA,PKax,PKay) to B
            #1.1) generate my (A) keypair PKa SKa
            keypair = Key.generate(256)
            PKax = keypair._pub[1][0]
            PKay = keypair._pub[1][1]
            PKa = (PKax,PKay)
            SKa = keypair._priv[1]
            # 1.2) A->B: M1=(helloA,PKax,PKay)
            M1='helloA'+','+str(PKax)+','+str(PKay)
            sock.send(M1.encode())
 
            # 3. A side: 1)receive M2, 2)compute ecdsa signature sa 3)send M3
            # 3.1) receive M2 from B, M2=(helloB,PKbx,PKby)
            M2 = sock.recv(1024).decode()
            helloB=M2.split(',')[0]            
            PKbx = M2.split(',')[1]
            PKby = M2.split(',')[2]
            PKb = (int(PKbx),int(PKby))
            # 3.2) compute sa
            hstringa='helloA'+str(PKax)+str(PKay)
            md5a=md5()
            md5a.update(hstringa.encode())
            ha=md5a.hexdigest()[8:-8]
            ha=int(ha,16)
            sa=sign(ha,(256,int(SKa)))
            # 3.3) A->B: M3=(sa)
            M3=str(sa[0])+','+str(sa[1])
            sock.send(M3.encode())

            # 4. A side: 1)receive M4, 2)verify sb
            M4 = sock.recv(1024).decode()
            sb_0=M4.split(',')[0]
            sb_1=M4.split(',')[1]
            sb=(int(sb_0),int(sb_1))
            stringb=helloB+PKbx+PKby
            md5b=md5()
            md5b.update(stringb.encode())
            hb=md5b.hexdigest()[8:-8]
            hb=int(hb,16)            
            if verify(hb,sb,(256,(int(PKbx),int(PKby))))==True:
                Ka=mul(c_p,c_q,c_n,PKb,SKa) 
                print('signature of sever is valid')
                print ('the shared secret is', Ka)
            else:
                print('signature of server is invalid, protocol fails')
            token=1
            
    except KeyboardInterrupt:
        sock.close()
        print("KeyboardInterrupt")
    #sys.exit(0)

    







