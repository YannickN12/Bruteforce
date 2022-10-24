#sha256 brute force from user input

import hashlib
import sys
import itertools
import string
import random
import os

def main():
    clear = lambda: os.system('cls')
    clear()
    print("Welcome to the SHA256 brute-forcer")
    print("This program will brute-force SHA256 hashes")
    print("This program will generate a random 4 character password")
    print("This program will then brute-force the hash of that password")
    print("You will then be prompted to enter a hash to brute-force")
    print("This program will then brute-force that hash")
    print("")

    #generate random password
    chars = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(chars) for i in range(8))
    print("The password is: " + password)

    #hash the password
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    print("The hash of the password is: " + hex_dig)

    #prompt user to enter hash to brute-force
    print("")
    hashToBrute = input("Enter the hash to brute-force: ")

    #brute-force the hash

    print("")
    print("Cracking hash...")
    print("")
    for i in itertools.product(string.ascii_lowercase + string.digits, repeat=8):
        brute = ''.join(i)
        hash_object = hashlib.sha256(brute.encode())
        hex_dig = hash_object.hexdigest()
        if hex_dig == hashToBrute:
            print("The password is: " + brute)
            print("")
            currenttime = time.process_time()
            print("Time taken: " + str(currenttime) + " seconds")
            print("")
            print("This is the end of the program. Press ENTER to exit.")
            input()
            sys.exit()

main()







            
















 










