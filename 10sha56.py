import hashlib

# Original message
msg1 = "STUDY INFOSEC"
hash1 = hashlib.sha256(msg1.encode()).hexdigest()
print("Original Message:", msg1)
print("SHA256 Hash:", hash1)
print("Length of Hash:", len(hash1), "hexadecimal characters\n")

# Slightly changed message
msg2 = "STUDE INFOSEC"  # Y changed to E
hash2 = hashlib.sha256(msg2.encode()).hexdigest()
print("Changed Message:", msg2)
print("SHA256 Hash:", hash2)
print("Length of Hash:", len(hash2), "hexadecimal characters\n")

# Comparing both hashes
print("Are the two hashes different?", hash1 != hash2)
