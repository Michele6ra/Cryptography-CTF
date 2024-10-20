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


    print(server.recvline())
    username = b'michele'

    server.sendline(username)
    cookie_jason = server.recvline()
    encrpyted_cookie = server.recvline()
    print(cookie_jason)
    print(encrpyted_cookie)

    output = encrpyted_cookie[20:]
    nonce_enc = output[:16]
    token_enc = output[17:]
    
    print(nonce_enc)
    print(token_enc)


    token_encrypt = base64.b64decode(token_enc)
    nonce = base64.b64decode(nonce_enc)

    token = json.dumps({
        "username": "michele"
    })

    
    keystream = bytes([d ^ o for d,o in zip(token_encrypt,token.encode())])
    print("token_encrypt e token normale")
    print(token_encrypt)
    print(token.encode())
    print('keystream')
    print(keystream)

    token_forgiato = json.dumps ({
        "admin": True
    })
    token_admin = bytes([d ^ o for d,o in zip(keystream,token_forgiato.encode())])
    print(server.recvline())
    print(server.recvline())
    print(server.recvline())
    print(server.recvline())
    server.sendline(b"flag")
    print(server.recvline())

    result = nonce_enc.decode()+"."+base64.b64encode(token_admin).decode()
    print(result)
    server.sendline(result.encode())
    print(server.recvline())
    print(server.recvline())
    print(server.recvline())
    