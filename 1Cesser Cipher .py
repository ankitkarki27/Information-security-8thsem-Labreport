message = "COME AT HALF PAST SIX"  # Now lowercase
key = 2
ciphered = ""

for char in message:
    if char.isupper():  # Handle uppercase
        shifted = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        ciphered += shifted
    elif char.islower():  # Handle lowercase
        shifted = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        ciphered += shifted
    else:  # Non-alphabetic (spaces, symbols, etc.)
        ciphered += char

print("Original:", message)
print("Shift:", key)
print("Encrypted:", ciphered)