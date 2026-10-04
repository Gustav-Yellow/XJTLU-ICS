# --- CAN304, CAN409 Lab  -----------------------------------------------------
#
# Lab 2: Start Encryption with Crypto Libraries
#
# RSA encryption with OAEP
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

data = "Learn Cryptography with fun!".encode("utf-8")
 
public_key = RSA.import_key(open("pub_key.pem").read())

# Encrypt the data with the public RSA key
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(data)

print ("The ciphertext is:")
print (ciphertext)
