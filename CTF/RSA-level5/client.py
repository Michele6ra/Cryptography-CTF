import os
os.environ['PWNLIB_NOTERM']='True'
os.environ['PWNLIB_SILENT']='True'
import pwn
from Crypto.Util.number import long_to_bytes

server = pwn.remote("130.192.5.212", 6645)
n=int(server.recvline().decode())
ct=int(server.recvline().decode())
e= 65537

input = (pow(2,e,n)*ct)%n
server.sendline(b'd'+str(input).encode())

bit = int(server.recvline().decode())
bit = bit //2

print(long_to_bytes(bit).decode())
