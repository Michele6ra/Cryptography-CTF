import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from myconfig import HOST, PORT, DELTA_PORT
import os
os.environ['PWNLIBNOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIBSILENT'] = 'True'
from pwn import *


if __name__ == "__main__":
    server = remote(HOST, PORT)
    
    for i in range(128):
        print(server.recvline())
        print(server.recvuntil(b": "))
        server.sendline(b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(server.recvuntil(b": "))
        output1= server.recvline()
        print(server.recvuntil(b": "))
        server.sendline(b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(server.recvuntil(b": "))
        output2= server.recvline()
        print(server.recvline())
        if(output1 == output2):
            server.sendline(b"ECB")
        else :
            server.sendline(b"CBC")
        print(server.recvline())
        

    print(server.recvline(2))




        
        
        






