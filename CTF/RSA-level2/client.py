#from gmpy2 import isqrt
import math
from Crypto.Util.number import long_to_bytes
n= 84579385253850209980531118129485716360575269582423585759001305965013034395499445816183248675447710453177558996114910965695049824431833160231360553529286419317374940825879760576417322050461035628520331998356731488662783964882867470865445762024182798458285340930223702904421982112483822508094601373760076526513
a = b = math.isqrt(n)
b2 = pow(a,2) - n
i=0
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


while True :
    print(i)
    if b2 == pow(b,2):
        break
    else :
        a+=1
        b2 = pow(a,2) - n
        b=math.isqrt(b2)

    i+=1
p= a+b
q= a-b
print(p)
print(q)


phi = euler_totient(p, q)
d = modinv(65537, phi)

ct = 17668912838657324025145974741772418705042500725249546941532860274474967308105880488339989276944955996505219230783445824255159192918050910923274393622976856688164873271519593664637389313627158186713709798641755794557335453137110328826176249263923330675599181311888750799280794535134718146446678320514719996743

m = pow(ct, d, n)


print(m)
print(long_to_bytes(m))
print(long_to_bytes(m).hex())
print(long_to_bytes(m).decode())


