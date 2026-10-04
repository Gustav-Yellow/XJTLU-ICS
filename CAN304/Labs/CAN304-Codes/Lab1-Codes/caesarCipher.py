# --- CAN304, CAN409 Lab  -----------------------------------------------------
#
# Lab 1: Programing and Hacking Classical Ciphers
#
# Caesar Cipher (Shift Cipher)
# Programming the Caesar cipher
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------


# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.+-*/='

# Input the plaintext/ciphertext:
# message = 'Welcome to the world of cryptography!'
message = 'qy6w97yL.9L.2yL*9!6xL9zLw!=0.91!u02=M'
print("Original message: \n"+message)

# Set the key:
key = 304
key = key%len(SYMBOLS)

# Set the mode: encrypt or decrypt
# mode = 'encrypt'
mode = 'decrypt'

# The result (ciphertext after encrypt or plaintext after decrypt):
translated = []

for symbol in message:
    #symbols in SYMBOLS will be translated (i.e., encrypted/decrypted)
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Encryption/Decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wrap-around, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        # Append the encrypted/decrypted symbol:
        translated.append(SYMBOLS[translatedIndex])
        
    else:
        # Append the symbol without encrypting/decrypting:
        translated.append(symbol)


print("%sed message:"% (mode.title()))
print(''.join(translated))

