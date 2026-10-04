# --- CAN304, CAN409 Lab  -----------------------------------------------------
#
# Lab 1: Programing and Hacking Classical Ciphers
#
# Caesar Cipher (Shift Cipher)
# Hacking the Caesar cipher with brute-force
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------


message = 'qy6w97yL.9L.2yL*9!6xL9zLw!=0.91!u02=M'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.+-*/='

# Decrypt the message with every possible key:
for key in range(len(SYMBOLS)):

    translated = []

   
    # Decrypt each symbol in `message` using the key:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wrap-around:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated.append(SYMBOLS[translatedIndex])

        else:
            # Append the symbol without encrypting/decrypting:
            translated.append(symbol)

    # Display every possible decryption:
    print('Key=%s: %s' % (key, ''.join(translated)))
