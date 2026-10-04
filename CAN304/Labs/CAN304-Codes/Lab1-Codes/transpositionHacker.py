# --- CAN304, CAN409 Lab  -----------------------------------------------------
#
# Lab 1: Programing and Hacking Classical Ciphers
#
# Transposition Cipher 
# Hacking the Transposition cipher with with brute-force
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------


import transpositionCipher

message = 'Wtocaeorrpl lyhctdpyoh t!meooe fg w r'

# Brute-force by looping through every possible key.
for key in range(1, len(message)):
    decryptedText = transpositionCipher.decryptMessage(key, message)
    print('Key=%s:' % (key))
    print(decryptedText)
    #print('Key=%s:' % (key, ''.join(decryptedText)))

