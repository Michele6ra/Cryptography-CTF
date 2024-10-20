
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
    admin = b"mynamesuperadmin"
    mask=b"AAAAAAAAAAAAAAAA"
    for message in server.recvlines(5):
        print(message)

    server.sendline(b"enc")
    print(server.recvline()) #"What do you want to encrypt?"
    admin_hex = bytes.fromhex(admin.hex())
    print(admin_hex)
    mask_hex = bytes.fromhex(mask.hex())
    print(mask_hex)
    admin_masked = bytes([d ^ o for d,o in zip(admin_hex, mask_hex )])
    server.sendline(admin_masked.hex().encode())
    iv = bytes.fromhex( server.recvline().decode().strip().split(": ")[1] ) # IV.hex()
    print("iv =")
    print(iv)
    cipher = bytes.fromhex( server.recvline().decode().strip().split(": ")[1] ) # cipher.hex()
    print("cipher =")
    print(cipher)
    xorone = bytes([d ^ o for d,o in zip(mask_hex, iv )])    
    for message in server.recvlines(6):
        print(message)   
    server.sendline(b"dec")
    print(server.recvline())#"What do you want to decrypt?\n> "
    server.sendline(cipher.hex().encode())
    print(server.recvline()) # "Gimme the IV\n"    
    server.sendline(xorone.hex().encode())

    print(server.recvline()) # mh normal day or flag    
    print(server.recvline())