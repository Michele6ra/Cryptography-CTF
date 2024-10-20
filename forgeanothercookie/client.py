import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long, long2str
from myconfig import HOST, PORT, DELTA_PORT
import os
os.environ['PWNLIBNOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIBSILENT'] = 'True'
from pwn import *
 
if __name__ == '__main__':
    server = remote(HOST,PORT)
    print(server.recv(10))
    first_block =b"aaaaaaa"
    second_block = b"true"
    second_block_padded=pad(second_block,AES.block_size)
    third_block = b"aaaaaaaaa"
    send_block = first_block + second_block_padded + third_block
    print(send_block)
    server.sendline(send_block)
    cipher_long = server.recvline()
    for message in server.recvlines(4):
        print(message)
    server.recv(2)
    server.sendline(b"flag")
    print("--------------")
    print(cipher_long)
    cipher_str = cipher_long.decode()
    cipher_int = int(cipher_str)
    cipher = long_to_bytes(cipher_int)
    print("---------------->")
    print(cipher)
    send_cipher = cipher.hex().encode()
    forge_cipher = send_cipher
    print(forge_cipher)
    print(send_cipher)
    b1=send_cipher[:32]
    b2=send_cipher[32:64]
    b3=send_cipher[64:96]
    b4=send_cipher[96:]

    forge_cipher=b1+b2+b3+b2
    print(forge_cipher)
    forge_cipher=bytes.fromhex(forge_cipher.decode()) 
    
    str_val = str(bytes_to_long(forge_cipher))
    byte_forge_cipher = str_val.encode() 
    print(byte_forge_cipher)


    server.sendline(byte_forge_cipher)
    print(server.recvlines(2))

    
    

