import os
os.environ['PWNLIB_NOTERM']='True'
os.environ['PWNLIB_SILENT']='True'
import pwn
from Crypto.Util.number import long_to_bytes

server = pwn.remote("130.192.5.212", 6646)

c=int(server.recvline().decode())
e= 65537

#input = (pow(2,e,n)*ct)%n
server.sendline(b'd'+str(-1).encode())
print(str(-1))

bit = int(server.recvline().decode())
print(bit)
n = bit+1
print(n)


to_send=(pow(2,e,n)*c)%n
server.send(b'd'+str(to_send).encode()+b'\n')
x=int(server.recvline().decode())
print(long_to_bytes(x//2))
