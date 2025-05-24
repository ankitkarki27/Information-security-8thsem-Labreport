from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Message and key
message = "Good Morning ALL"
key = get_random_bytes(16)  # AES-128 uses a 16-byte key

# Prepare message (must be padded to AES block size 16 bytes)
data = message.encode()
padded_data = pad(data, AES.block_size)

# AES Encryption
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(padded_data)

# AES Decryption
decrypt_cipher = AES.new(key, AES.MODE_ECB)
decrypted_data = unpad(decrypt_cipher.decrypt(ciphertext), AES.block_size)

# Output
print("Original Message :", message)
print("Encrypted (hex)  :", ciphertext.hex())
print("Decrypted Message:", decrypted_data.decode())
