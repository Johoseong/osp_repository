#!/usr/bin/python
import sys
import my_pkg

if __name__ == "__main__":
    while True:
        menu = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))

        if menu == 3:
            print("exit the program...")
            break

        if menu == 1:
            binaryInput = my_pkg.BinaryInput()
            my_pkg.BinaryToOct(binaryInput)
            my_pkg.BinaryToDec(binaryInput)
            my_pkg.BinaryToHex(binaryInput)

        if menu == 2:
            first_list, second_list = my_pkg.InputTwoList()
            
            my_pkg.union(first_list, second_list)
            my_pkg.intersection(first_list, second_list)
