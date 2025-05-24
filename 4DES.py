from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# 8-byte (64-bit) DES key
key = b'8bytekey'  # Must be exactly 8 bytes

# Message to encrypt
message = "Hello Student".encode()

# Padding to make message multiple of 8 bytes
padded_msg = pad(message, DES.block_size)

# Create DES cipher in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt the message
encrypted = cipher.encrypt(padded_msg)
print("Encrypted (hex):", binascii.hexlify(encrypted).decode())

# Decrypt the message
decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)
print("Decrypted:", decrypted.decode())
