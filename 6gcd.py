def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example
a, b = 31, 2
print("GCD of", a, "and", b, "is:", gcd(a, b))
