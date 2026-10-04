# --- CAN304, CAN409 Lab  -----------------------------------------------------
#
# Lab 1: Programing and Hacking Classical Ciphers
#
# Transposition Cipher 
# Programming the Transposition cipher
#
# By Jie Zhang <jie.zhang01@xjtlu.edu.cn>
#
# -----------------------------------------------------------------------------

import math

def main():
    myMessage = 'Welcome to the world of cryptography!'
    #myMessage = 'Wtocaeorrpl lyhctdpyoh t!meooe fg w r'
    print("The message is: \n"+myMessage)

    myKey = 8
    myMode = 'encrypt'
    #myMode = 'decrypt'

    ciphertext = encryptMessage(myKey, myMessage)
    #plaintext = decryptMessage(myKey, myMessage)


    print("The ciphertext is: \n"+ciphertext)
    #print("The plaintext is: \n"+plaintext) 


def encryptMessage(key, message):
    """
    实际上就是根据密钥（key）的长度创建对应列数的表格。
    然后从index为0的列开始循环整个message，将对应index上的字符添加到对应列的字符串中。
    然后一直进行内循环，每添加完一个字符，就将当前的index加上key。直到最后的index大于message的长度。
    然后将列的index+1，再进行下一轮外循环。
    :param key:
    :param message:
    :return:
    """
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list.
            ciphertext[column] += message[currentIndex]

            # move currentIndex over
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)

def decryptMessage(key, message):
    """

    :param key:
    :param message:
    :return:
    """
    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to next column.

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

# If transpositionCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
