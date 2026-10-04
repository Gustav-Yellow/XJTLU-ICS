# --- CAN304, CAN409 Lab  -----------------------------------------------------
#
# Lab 2: Start Encryption with Crypto Libraries
#
# AES encrytion with the Cipher Block Chaining (CBC) mode
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------

from Crypto.Cipher import AES

# 现在有 28 bytes
data = 'Learn cryptography with fun!'

# Add paddings to the plaintext so that the length is multiple of the cipher block size.
# AES默认块长度为16bytes，所以此时 28 % 16 = 12
# 然后16-12=4，让28+4=32也就是给现在的字符串后面加上4bytes的内容，得到长度为16的倍数的字符串
pad_len = AES.block_size - (len(data) % AES.block_size)
if pad_len != 0:
    data = data + chr(pad_len)*pad_len

# Let's assume that the key and iv are somehow available. Alternatively, you can generate the them using get_random_bytes()
# In real life, the key is negotiated between the encrypting and the decrypting entities. The iv must be “unpredictable”, in other words, randomly generated before the encryption starts. 
key = b'\xd6|iK\x8e\x94E\xd9\x82\x83,\xbap/\x8e\xdd'
iv = b'\xe5\x8f\x89V\x02\xddQz\xe9\x90SD\xd4\x90\xe8\xb6'


"""
CBC加密流程
       [ IV ] <------ (仅用于第一块)
         |
         v
      ( XOR ) <--- [ P_1 (明文块1) ]
         |
         v
    [ AES 加密 ] (使用 Key K)
         |
         v
       [ C_1 ] ----+----> (输出密文块1)
         |         |
         | (反馈)  |
         v         |
      ( XOR ) <----+
         |
         v
      ( XOR ) <--- [ P_2 (明文块2) ]
         |
         v
    [ AES 加密 ] (使用 Key K)
         |
         v
       [ C_2 ] ----+----> (输出密文块2)"""
#cipher = AES.new(key, AES.MODE_CBC, iv)
#ciphertext = cipher.encrypt(data.encode('utf-8'))


# ECB加密非常不安全
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(data.encode('utf-8'))

print ("The ciphertext is: \n" + str(ciphertext))
