import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from myconfig import HOST, PORT, DELTA_PORT

import os
os.environ['PWNLIBNOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIBSILENT'] = 'True'

from pwn import *

if __name__ == '__main__':
    server = remote(HOST,PORT)
    initialize = int(1)    
    print(server.recvline())
    server.sendline(b"1")
    print(server.recvline())
    cipertext_flag = server.recvline()
    cipertext_flag = cipertext_flag.decode()
    cipertext_flag = bytes.fromhex(cipertext_flag)
    print(cipertext_flag)
    print(server.recv())
    server.sendline(b"y")
    print(server.recv())
    server.sendline(b"micheledavidefrancescoedoardogianfrancofedericoannanicolopaologabrieler")
    cipertext_michele = server.recvline()
    cipertext_michele = cipertext_michele.decode()
    cipertext_michele = bytes.fromhex(cipertext_michele)
    print("ciphertext_michele ")
    print(cipertext_michele)
    keystream = bytes([d ^ o for d,o in zip(cipertext_michele, b"micheledavidefrancescoedoardogianfrancofedericoannanicolopaologabrieler" )])
    print("il keystream dovrebbe essere:")
    print(keystream)
    result = bytes([d ^ o for d,o in zip(cipertext_flag, keystream)])
    print(result)


    


