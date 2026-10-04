# --- CAN304, CAN409 Lab  -----------------------------------------------------
#
# Lab 1: Programing and Hacking Classical Ciphers
#
# Vigenere Cipher
# Programming the Vigenere cipher 
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = "Learn Cryptography with fun!"
    #myMessage = "Psscp Hncdlziwwtvq hkyd jif!"
    print('Origial message: \n'+myMessage)
    myKey = 'EOSLCFW'
    myMode = 'encrypt'
    #myMode = 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] 

    keyIndex = 0
    key = key.upper()

    for symbol in message: # Loop through each symbol in message.
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS.
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # Add if encrypting.
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # Subtract if decrypting.

            num %= len(LETTERS) # Handle any wraparound.

            # Append the encrypted/decrypted symbol:
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Append the symbol without encrypting/decrypting.
            translated.append(symbol)

    return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
