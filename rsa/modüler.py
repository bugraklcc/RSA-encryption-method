def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

m = 282124 
a = 218427

gcd, x, y = extended_gcd(a, m)

if gcd == 1:
    D = x % m
    print(D)
else:
    print("Modüler ters yok.")