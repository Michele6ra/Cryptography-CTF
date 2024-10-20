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
    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    ciao = "mynamesuperadmin"
    #print(bytes.fromhex(ciao))
    print(server.recvline()) #"What do you want to do?\n"
    print(server.recvline()) # "quit - quit the program\n"
    print(server.recvline()) #"enc - encrypt something\n"
    print(server.recvline()) #"dec - decrypt something\n"
    print(server.recvline()) #"help - show this menu again\n"
    server.sendline(b"enc")
    print(server.recvline()) #"What do you want to encrypt?"
    input=b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" #passata come byte ma letta con fromhex()

    server.sendline(input) 
    iv = server.recvline() # IV.hex()
    iv= iv[6:]
    cipher = server.recvline() #encrypted.hex()
    cipher = cipher[11:]
    print("-----------------------------")
    print(iv)
    print(cipher)
    print("-----------------------------")

    cipherus = cipher.decode()
    ivus = iv.decode()
    plainkey = bytes([d ^ o for d,o in zip(iv, bytes.fromhex(cipherus) )])
    
    print(ivus)
    print(cipherus)
    print("with from hex")
    print(bytes.fromhex(ivus))
    print(bytes.fromhex(cipherus))


    print(server.recvline()) #\n

    print(server.recvline()) #"What do you want to do?\n"
    print(server.recvline()) #"quit - quit the program\n"
    print(server.recvline()) #"enc - encrypt something\n"
    print(server.recvline()) # "dec - decrypt something\n"
    print(server.recvline()) #"help - show this menu again\n"
    server.sendline(b"dec")

    inputus = input.hex()
    plainkeyus = plainkey.hex()
    key = bytes([d ^ o for d,o in zip(bytes.fromhex(plainkeyus), bytes.fromhex(inputus) )])
    print("questa dovrebbe essere la chiave vera e propria:")
    print(key.hex())
    #keyus = key.decode()
    print("------------------------------")
    #print(keyus)
    print(ivus)
    print("------------------------------")

    encript = AES.new( key , AES.MODE_CBC, bytes.fromhex(ivus))
    admin = b"mynamesuperadmin"
    
    result = encript.encrypt(bytes.fromhex(admin.hex()))
    print("result is:")
    print(result.hex())

    print(server.recvline())#"What do you want to decrypt?\n> "

    server.sendline(result.hex().encode())
    print("ciao")

    print(server.recvline()) # "Gimme the IV\n"
    server.sendline(iv)
    print(server.recvline()) 
    print(server.recvline())

    

    print(server.recvline())
    print(server.recvline())
    print(server.recvline())
    print(server.recvline())
    print(server.recvline())



    
