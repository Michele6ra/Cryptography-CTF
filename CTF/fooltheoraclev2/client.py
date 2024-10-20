import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from myconfig import HOST, PORT, DELTA_PORT
import os
os.environ['PWNLIBNOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIBSILENT'] = 'True'
from pwn import *

if __name__ == '__main__':

    chars = '}{0123456789-CRYPTOabcdefghijklmnopqrstuvwxyzABDEFGHIJKLMNQSUVWXZ'
    input1 = "CRYPTO24{59e0868"
    input2 = "zzzzzzzzzzz"
    flag = ""
    server = remote(HOST,PORT)
    input_gen = b"zzzzzzzzzzzzz"
    
    for i in range(46):
        server.recvlines(4)
        server.sendline(b"enc")
        input_gen += b"z" 
        server.sendline(input_gen.hex().encode())
        cipher1 = server.recvline()
        valuation1 = cipher1[128+4 :160+4]
        for k in chars:            
            server.recvlines(4)
            server.sendline(b"enc")           
            guess = k + flag
            blocco = pad(guess.encode(), AES.block_size)
            forge = input2 + blocco.decode()
            server.sendline(forge.encode().hex().encode())
            cipher2 = server.recvline()
            valuation2 = cipher2[32+4 :64+4]
            if (valuation1 == valuation2):
                flag = k + flag
                print(flag)
                break      
    print(flag) 
    




    