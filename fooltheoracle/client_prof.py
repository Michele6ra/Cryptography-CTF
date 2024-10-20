import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from myconfig import HOST, PORT, DELTA_PORT
import os
os.environ['PWNLIBNOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIBSILENT'] = 'True'
from pwn import *

if __name__ == '__main__':
    #server = remote(HOST,PORT)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-}'
    input1 = "CRYPTO24{59e0868"
    input2 = "CRYPTO24{59e086"
    k = ""

    print(input2.encode().hex())
    for i in chars:
        server = remote(HOST,PORT)
        for message in server.recvlines(4):
            print(message)
        server.sendline(b"enc")
        guess = input1 +  i  + input2
        print(guess)
        print(guess.encode().hex())
        server.sendline(guess.encode().hex())
        cipher = server.recvline().decode()
        print(cipher)
        cipher1=cipher[4:36]
        print(cipher[4:36])
        print("-----------")
        cipher2=cipher[36:68]
        print(cipher[36:68])
        print("-----------")

        if (cipher1 == cipher2):
            print(i)
            break
        server.close()

    
