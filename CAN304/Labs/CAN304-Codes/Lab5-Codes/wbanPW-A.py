# --- CAN304, CAN409 Lab  -----------------------------------------------------
# Lab 5: The ECC lib and ECDH-based AKA protocols
#
# Password Authenticated Association in IEEE 802.15.6 
# Party A
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------


import errno
import socket
import time
import random
import hmac



from collections import OrderedDict
from ecc.Key import Key
from hashlib import sha256
from ecc.elliptic import mul,add,neg


DOMAINS = {
    # Bits : (p, order of E(GF(P)), parameter b, base point x, base point y)

    256: (0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
          0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
          0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
          0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
          0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
}

if __name__== '__main__':

    global Ra,Tb,p,n,b,x,y,c_p,c_q,c_n,M1,M2,M3,Ka,macb
    server_ip = '127.0.0.1'
    server_port = 9004

    # initialization
    p, n, b, x, y = DOMAINS[256]
    c_p = 3
    c_n = p
    c_q = p - b
    idA='00000001'
    idB='00000002'
    PW=(1234,5678)
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
            # 1. A side: send M1=(B,A,Na,PKapwx,PKapwy) to B
            #1.1) generate my (A) keypair PKa SKa
            keypair = Key.generate(256)
            PKax = keypair._pub[1][0]
            PKay = keypair._pub[1][1]
            PKa = (PKax,PKay)
            SKa = keypair._priv[1]
            # 1.2) compute PKapw
            negPW=neg(PW,c_n)
            PKapw=add(c_p,c_q,c_n,PKa,negPW)
            #1.2) generate my (A) nonce Na
            Na=random.randint(000000,999999)
            # 1.3) A->B: M1=(B,A,Na,PKax,PKay)
            M1=idA+','+idB+','+str(Na)+','+str(PKapw[0])+','+str(PKapw[1])
            sock.send(M1.encode())
 
            # 3. A side: 1)receive M2, 2)compute Ka, 3)compute maca,macb_check 4)send M3
            # 3.1) receive M2 from B, M2=(A,B,Nb,PKbx,PKby)
            M2 = sock.recv(1024).decode()
            Nb = M2.split(',')[2]
            PKbx = M2.split(',')[3]
            PKby = M2.split(',')[4]
            PKb = (int(PKbx),int(PKby))
            # 3.2) compute Ka
            Ka=mul(c_p,c_q,c_n,PKb,SKa)          
            # 3.3) compute maca,macb_check
            hmac_stringa=idB+idA+Nb+str(Na)
            newhash=hmac.new(str(Ka[0]).encode(),''.encode(),sha256)
            newhash.update(hmac_stringa.encode())
            maca=newhash.hexdigest()
            hmac_stringb=idA+idB+str(Na)+Nb
            newhash=hmac.new(str(Ka[0]).encode(),''.encode(),sha256)
            newhash.update(hmac_stringb.encode())
            macb_check=newhash.hexdigest()
            # 3.4) A->B: M3=(maca)
            M3=maca
            sock.send(M3.encode())

            # 5. A side: 1)receive M4, 2)verify macb
            M4 = sock.recv(1024).decode()
            macb=M4
            if str(macb_check)==macb:
                print('macb is valid')
                print ('the shared secret is', Ka)
            else:
                print('macb is invalid, protocol fails')
            token=1
            
    except KeyboardInterrupt:
        sock.close()
        print("KeyboardInterrupt")
    #sys.exit(0)

    







