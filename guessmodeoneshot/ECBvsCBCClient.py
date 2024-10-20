import os
os.environ['PWNLIB_NOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIB_SILENT'] = 'True'

from pwn import *
from math import ceil
from Crypto.Cipher import AES

from myconfig import HOST,PORT



BLOCK_SIZE = AES.block_size
BLOCK_SIZE_HEX = 2*BLOCK_SIZE


server = remote(HOST, PORT)

for i in range(128):
    print(server.recvline())
    print(server.recv(19))
    otp = server.recvline()
    otp = otp[:-1]
    print(b'otp modificato ------>'+otp)
    print(server.recv(7))

    
    server.sendline(otp)
    output_sporco = server.recv(8)
    output = server.recvline()
    output1 = output[: 32]
    output2 = output[32:64]
    print(output1)
    print(output2)
    

    print(server.recvline())
    if (output1 == output2):
        print("ECB")
        server.sendline(b'ECB')

    else:
        print("CBC")
        server.sendline(b'CBC')
    print(server.recvline())

print(server.recvline())