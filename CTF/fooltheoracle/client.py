import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from myconfig import HOST, PORT, DELTA_PORT
import os
os.environ['PWNLIBNOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIBSILENT'] = 'True'
from pwn import *

if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-}'
    input1 = "CRYPTO24{59e0868"
    input2 = ""
    k = ""
    server = remote(HOST,PORT)
    input_gen = "zz"
    for i in range(46):
        print(i)
        server.recvuntil(b">")
        server.sendline(b"enc")
        input_gen += 'z'
        server.recvuntil(b">")
        server.sendline(input_gen.encode())
        print(input_gen.encode().hex())
        cipherfinal = server.recvline().decode()
        print(cipherfinal)
        N = len(cipherfinal)//AES.block_size
        print(N)
        sixth_block = cipherfinal[97:113]

        for s in chars:

            server.recvuntil(b">")
            server.sendline(b"enc")
            
            gen_block = pad((s+k).encode(), AES.block_size).hex()
            server.recvuntil(b">")
            server.sendline(gen_block)
            cipher_gen = server.recvline().decode()
            cipher_gen = cipher_gen[:32]

            if (sixth_block == cipher_gen):
                k = s + k
                print(k)
                print(s)
                break
            
    server.close()
    

    

    