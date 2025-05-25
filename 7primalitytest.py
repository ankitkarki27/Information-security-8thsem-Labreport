import random

def is_probable_prime(n, k=5):
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Test Numbers
numbers = [5, 21, 30, 61, 561]
print("Fermat's Primality Test Results:")
for num in numbers:
    result = is_probable_prime(num)
    print(f"{num}: {'Probably Prime' if result else 'Composite'}")
