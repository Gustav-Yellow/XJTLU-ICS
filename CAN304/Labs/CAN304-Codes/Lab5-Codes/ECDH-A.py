# --- CAN304, CAN409 Lab  -----------------------------------------------------
# Lab 5: The ECC lib and ECDH-based AKA protocols
#
# ECDH key agreement protocol
# Party A
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------


import socket
from collections import OrderedDict
from ecc.elliptic import mul,add,neg
from ecc.Key import Key

DOMAINS = {
    # Bits : (p, order of E(GF(P)), parameter b, base point x, base point y)

    256: (0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
          0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
          0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
          0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
          0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)      
}

if __name__== '__main__':

    global p,n,b,x,y,c_p,c_q,c_n
    server_ip = "127.0.0.1"
    server_port = 6633

    # initialization
    p, n, b, x, y = DOMAINS[256]
    c_p = 3
    c_n = p
    c_q = p - b
    G = (x,y)


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
            
            # 1. A side:
            #1.1) generate x_a=SKa, h1=PKa*G using Key.generate(bit)
            keypair = Key.generate(256)
            SKa = keypair._priv[1]
            PKax = keypair._pub[1][0]
            PKay = keypair._pub[1][1]
            PKa = (PKax,PKay)

            # 1.2) A->B: M1=(PKa)
            M1=str(PKa[0])+','+str(PKa[1])
            sock.send(M1.encode())
 
            # 3. A side: receive M2 from B
            M2 = sock.recv(1024).decode()
            PKbx = M2.split(',')[0]
            PKby = M2.split(',')[1]
            PKb = (int(PKbx),int(PKby))
            
            # 4 A side: compute shared secret k1=SKa*PKb
            k1=mul(c_p,c_q,c_n,PKb,SKa)          
            print ('A side: the shared secret is', k1)

            token=1
            
    except KeyboardInterrupt:
        s.close()
        print("KeyboardInterrupt")

    







