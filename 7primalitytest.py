import random

def ptest(n, k=5):
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Test num
num = [5, 21, 30, 61, 561]
print("Fermat's Primality Test Results:")
for num in num:
    result = ptest(num)
    print(f"{num}: {'Probably Prime' 
          if result else 'Composite'}")
