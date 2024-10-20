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


f = FactorDB(180210299477107234107018310851575181787)
f.connect()
p,q = f.get_factor_list()

n = 180210299477107234107018310851575181787

phi = euler_totient(p, q)
d = modinv(65537, phi)

ct = 27280721977455203409121284566485400046

m = pow(ct, d, n)


print(m)
print(long_to_bytes(m))
print(long_to_bytes(m).hex())
print(long_to_bytes(m).decode())