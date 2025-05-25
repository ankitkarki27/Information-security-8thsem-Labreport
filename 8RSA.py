import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# 1st prime number
p = 3

# 2nd prime number
q = 11

# message to encrypt
msg = 12

n = p * q
z = (p - 1) * (q - 1)

print("The value of z =", z)

# Find e such that 1 < e < z and gcd(e, z) == 1
for e in range(2, z):
    if gcd(e, z) == 1:
        break

print("The value of e =", e)

# Find d such that (d * e) % z == 1
for i in range(10):
    x = 1 + (i * z)
    if x % e == 0:
        d = x // e
        break

print("The value of d =", d)

# Encryption c = (msg^e) % n
c = pow(msg, e, n)
print("Encrypted message is:", c)

# Decryption msgback = (c^d) % n
msgback = pow(c, d, n)
print("Decrypted message is:", msgback)
