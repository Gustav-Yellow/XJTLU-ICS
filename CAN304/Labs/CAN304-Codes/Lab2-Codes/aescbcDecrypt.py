# --- CAN304, CAN409 Lab  -----------------------------------------------------
#
# Lab 2: Start Encryption with Crypto Libraries
#
# AES decryption with the Cipher Block Chaining (CBC) mode
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------

from Crypto.Cipher import AES

ciphertext = b'\xa7\x8a1\xdf\xf3\xe9\x07\x87\n\xb9\xad\x92!^\xfb\xff\xd5\x90\x84\xa3\xa8\xe5\x86\x88Rnm\x15\x8a@\xa8\x15'

# Let's assume that the key and iv are somehow available
key = b'\xd6|iK\x8e\x94E\xd9\x82\x83,\xbap/\x8e\xdd'
iv = b'\xe5\x8f\x89V\x02\xddQz\xe9\x90SD\xd4\x90\xe8\xb6'

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext_pad = cipher.decrypt(ciphertext).decode("utf-8")

# Reove paddings from the plaintext
"""
       [ IV ]                  [ C_1 (密文块1) ]             [ C_2 (密文块2) ]
         |                           |                           |
         +---------> ( XOR ) <-------+                           |
                        |                                      |
                        v                                      |
                   [ AES 解密 ] (使用 Key)                       |
                        |                                      |
                        v                                      |
                      [ P_1 ] <---------------------+          |
                      (明文1)                       |          |
                                                    |          |
       (反馈机制：使用前一块密文)                     |          |
                                                    |          |
                                         [ C_1 ] ---+----------+
                                           |                 |
                                           +------> ( XOR ) <-+
                                                      |
                                                      v
                                                 [ AES 解密 ] (使用 Key)
                                                      |
                                                      v
                                                    [ P_2 ]
                                                    (明文2)"""
pad = ord(plaintext_pad[-1])
plaintext = plaintext_pad[:-pad]

print("The plaintext is: \n" + plaintext)
