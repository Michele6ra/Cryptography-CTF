from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes

def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = egcd(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
        
def euler_totient(p, q):
    return (p - 1) * (q - 1)


f = FactorDB(155532372776354562033743358690741450391)
f.connect()
p,q = f.get_factor_list()

n = 155532372776354562033743358690741450391

phi = euler_totient(p, q)
d = modinv(65537, phi)

ct = 89785627703612160352678144684692494325

m = pow(ct, d, n)


print(m)
print(long_to_bytes(m))
print(long_to_bytes(m).hex())
print(long_to_bytes(m).decode())