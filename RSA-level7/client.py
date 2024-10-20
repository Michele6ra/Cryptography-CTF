import os
os.environ['PWNLIB_NOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIB_SILENT'] = 'True'
from pwnlib.tubes.remote import remote
from Crypto.Util.number import long_to_bytes

#test the connection with the server
server = remote('130.192.5.212', 6647)

n = int(server.recvline().decode())

c = int(server.recvline().decode())


# init the bounds
upper_bound = n
lower_bound = 0
e = 65537


# loop
m = c #ciphertext
for i in range(n.bit_length()):
    m = (pow(2, e, n) * m) % n

    # interact with the server
    server.sendline(str(m).encode())
    bit = int(server.recvline().decode())
    print(lower_bound)
    print(upper_bound)
    # update bounds based on the leaked LSB
    if  bit == 1:
        lower_bound = (upper_bound + lower_bound) // 2
        
    else:
        upper_bound = (upper_bound + lower_bound) // 2
        


#print decoded message
print(long_to_bytes(lower_bound).decode())

print(long_to_bytes(upper_bound).decode())





