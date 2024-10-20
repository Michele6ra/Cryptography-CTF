import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from myconfig import HOST, PORT, DELTA_PORT
import os
os.environ['PWNLIBNOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIBSILENT'] = 'True'
from pwn import *

if __name__ == '__main__':
    
    chars = '}{0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    input1 = "CRYPTO24{59e0868"
    flag = ""
    server = remote(HOST,PORT)
    input_gen = b"zz"

    for i in range(46):
        server.recvlines(4)
        server.sendline(b"enc")

        input_gen += b"z" 
        print(input_gen)
        server.sendline(input_gen.hex().encode())
        cipher1 = server.recvline()
        cipher1 = cipher1[3:]
        valuation1 = cipher1[3*32+1 :4*32]
        for k in chars:            
            server.recvlines(4)
            server.sendline(b"enc")
            forge = k + flag
            server.sendline(pad(forge.encode(), AES.block_size).hex().encode())
            cipher2 = server.recvline()
            cipher2=cipher2[3:]
            valuation2 = cipher2[0*32+1 :1*32]
            if (valuation1 == valuation2):
                flag = k + flag
                print(flag)
                break      
    print(flag) 
    





    