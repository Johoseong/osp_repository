#!/usr/bin/python
import sys

def BinaryInput():
    binaryInput = int(input("input binary number : "))
    strBinaryInput = str(binaryInput)    
    return strBinaryInput

def BinaryToOct(strBinaryInput):
    result = 0

    for i, digit in enumerate(strBinaryInput[::-1]):
        result = result + int(digit) * (2 ** (i%3)) * (10 ** (i//3))

    print("=> OCT> ", result)
            

def BinaryToDec(strBinaryInput):
    result = 0

    for i, digit in enumerate(strBinaryInput[::-1]):
        result = result + int(digit) * (2 ** i)

    print("=> DEC> ", result)    

def BinaryToHex(strBinaryInput):
    result = 0
    list1 = []

    if len(strBinaryInput) % 4 != 0:
        strBinaryInput.zfill(len(strBinaryInput) + len(strBinaryInput) % 4)
    
    for i, digit in enumerate(strBinaryInput[::-1]):
        result = result + int(digit) * (2 ** (i%4))
        if i % 4 == 3:
            if result >= 10:
                list1.append(chr(result + 55))
            else:
                list1.append(result)
            result = 0

    list1.reverse()
    
    print("=> HEX> ", ''.join(map(str, list1)))