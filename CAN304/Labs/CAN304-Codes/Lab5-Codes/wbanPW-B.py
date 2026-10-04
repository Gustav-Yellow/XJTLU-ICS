# --- CAN304, CAN409 Lab  -----------------------------------------------------
# Lab 5: The ECC lib and ECDH-based AKA protocols
#
# Password Authenticated Association in IEEE 802.15.6 
# Party B
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
from hashlib import sha256
from ecc.elliptic import mul,add,neg
from ecc.curves import get_curve


DOMAINS = {
    # Bits : (p, order of E(GF(P)), parameter b, base point x, base point y)
    256: (0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
          0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
          0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
          0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
          0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
}

if __name__ == '__main__':

    global Ta,Rb,p,n,b,x,y,c_p,c_q,c_n,M1,M2,M3,Kb

    HOST = '127.0.0.1'
    PORT = 9004

    # initialization
    p, n, b, x, y=DOMAINS[256]
    c_p=3
    c_n=p
    c_q=p-b
    idA='00000001'
    idB='00000002'
    PW=(1234,5678)
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

            # 2. B side: 1)receive M1 from A, 2)generate my keypair 3)generate Nb 4) send M2
            # 2.1) receive M1=(B,A,Na,PKax,PKay) from B
            M1=connection.recv(1024).decode()
            Na=M1.split(',')[2]
            PKapwx=M1.split(',')[3]
            PKapwy=M1.split(',')[4]
            PKapw=(int(PKapwx),int(PKapwy))
            # 2.2) generate my keypair
            keypair = Key.generate(256)
            PKbx = keypair._pub[1][0]
            PKby = keypair._pub[1][1]
            SKb = keypair._priv[1]
            # 2.3) genearate my nonce Nb
            Nb=random.randint(000000,999999)
            # 2.4) B->A: M2=(A,B,Nb,PKbx,PKby)
            M2=idA+','+idB+','+str(Nb)+','+str(PKbx)+','+str(PKby)
            connection.send(M2.encode())


            # 4. B side: 1) receive M3 from A 2) compute Kb 3) compute maca_check, macb 4)verfiy maca 5)send M4
            # 4.1) receive M3=maca from A
            M3=connection.recv(1024).decode()
            maca=M3
            # 4.2) compute Kb
            PKa=add(c_p,c_q,c_n,PKapw,PW)
            Kb=mul(c_p,c_q,c_n,PKa,SKb)
            # 4.3) compute maca_check, macb
            hmac_stringa=idB+idA+str(Nb)+Na
            newhash=hmac.new(str(Kb[0]).encode(),''.encode(),sha256)
            newhash.update(hmac_stringa.encode())
            maca_check=newhash.hexdigest()
            hmac_stringb=idA+idB+Na+str(Nb)
            newhash=hmac.new(str(Kb[0]).encode(),''.encode(),sha256)
            newhash.update(hmac_stringb.encode())
            macb=newhash.hexdigest()        
            # 4.4) verify maca           
            if maca_check==maca:
                # 4.5) send M4
                M4=macb
                connection.send(M4.encode())
                print('maca is valid')
                print('the shared secrety is', Kb)
            else:
                print('maca is invalid, protocol fails')
            token=1

    except KeyboardInterrupt:
        print('>>>quit')
    #sys.exit(0)




