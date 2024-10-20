from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from pwn import *
import json, base64

u_1 = b'zz'
u_2 = pad(b'true}',AES.block_size)
u_3 = b'zzzz'


#{"username": "zz
#true}ppppppppppp
#zzzz", "admin":o
#false}pppppppppp


#{"username": "zz       1
#---------------\       2
#"surname--------       3
#---------------\       4
#":--------------       5
#true,-----------       6
#zzzz", "admin":-       7
#false}pppppppppp       8

#{"username": "zz       1
#-zzz", "admin":-       7
#true,-----------       6
#"surname--------       3
#":--------------       5
#false}pppppppppp       8
#input = zz---------------"surname-----------------------":--------------true,---------------
input1= 'zz               "surname                       ":              true,               zzzz' 
input = 'zz               "surname                       ":              true,           zzzz'
#'zz---------------\"surname-----------------------\":--------------true,-----------zzzz'


#print(u_1+u_2+u_3)

host = '130.192.5.212'
port =  6551
server = remote(host,port)


response1 = server.recvuntil(b'> ').decode()
print(response1)
#username = u_1 + u_2 + u_3
#print(input)
print(input)
server.sendline(input.encode())
token = server.recvline().decode()
response2 = server.recvuntil(b'> ')


tokenB64 = token[20:]
print('Token in b64 sporco --> ',token)
token = base64.b64decode(tokenB64)

print('Token in b64 --> ',tokenB64)
print('Token in esa --> ',token)
#for i in range(0,len(token),AES.block_size):
#                print(token[i:i + AES.block_size])

print("lunghezza token encriptato -->", len(token))
print(token[0:16])
print(token[16:32])
print(token[32:48])
print(token[48:64])
print(token[64:80])
print(token[80:96])
print(token[96:112])
print(token[112:128])
first_block = token[0:16]
second_block = token[16:32]
third_block = token[32:48]
fourth_block = token[48:64]
fifth_block = token[64:80]
sixth_block = token[80:96]
seventh_block = token[96:112]
eighth_block = token[112:128]
#nineth_block = token[128:144]


forge_token = first_block + seventh_block + sixth_block + third_block + fifth_block + eighth_block
forged_token_b64 = base64.b64encode(forge_token)
server.sendline(b'flag')
resp = server.recvuntil(b'> ')
print(resp)
server.sendline(forged_token_b64)
print(server.recvlines(3))
