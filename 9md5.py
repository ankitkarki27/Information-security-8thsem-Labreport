import hashlib

# Original text
str = "come home tomorrow"
print("Original Text:")
print(str)
output = hashlib.md5(str.encode())
print("Hash of Original Text:")
print(output.hexdigest())

# Slightly modified text
str = "come home tomorrow."
print("\nModified Text:")
print(str)
output = hashlib.md5(str.encode())
print("Hash of Modified Text:")
print(output.hexdigest())

# Reverted to original
str = "come home tomorrow"
print("\nReverted Text:")
print(str)
output = hashlib.md5(str.encode())
print("Hash of Reverted Text:")
print("Hash of Reverted Text:")
print(output.hexdigest())
