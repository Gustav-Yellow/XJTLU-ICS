# --- CAN304, CAN409 Lab  -----------------------------------------------------
# Lab 5: The ECC lib and ECDH-based AKA protocols
#
# ECDH key agreement protocol
# Party B
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
          0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,               0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
}

if __name__ == '__main__':

    global p,n,b,x,y,c_p,c_q,c_n

    HOST = '127.0.0.1'
    PORT = 6633

    # initialization
    p, n, b, x, y=DOMAINS[256]
    c_p=3
    c_n=p
    c_q=p-b
    G=(x,y)

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

            # 2. B side: 
            # 2.1) receive M1=(PKa) from B
            M1=connection.recv(1024).decode()            
            PKax=M1.split(',')[0]
            PKay=M1.split(',')[1]
            PKa=(int(PKax),int(PKay))
            # 2.2) generate y_b=SKb, h2=PKa=SKb*G using Key.generate(bit)
            keypair = Key.generate(256)
            SKb = keypair._priv[1]
            PKbx = keypair._pub[1][0]
            PKby = keypair._pub[1][1]
            PKb = (PKbx,PKby)
            # 2.3) B->A: M2=(PKb)
            M2=str(PKb[0])+','+str(PKb[1])
            connection.send(M2.encode())

            # 4. B side:compute shared key k2=SKb*PKa
            k2=mul(c_p,c_q,c_n,PKa,SKb)
            print('B side: the shared secrety is', k2)
            
            token=1

    except KeyboardInterrupt:
        print('>>>quit')
    #sys.exit(0)




