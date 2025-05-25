import hashlib

# Original text
inputstring = "come home tomorrow"
print("Original Text:")
print(inputstring)
output = hashlib.md5(inputstring.encode())
print("Hash of Original Text:")
print(output.hexdigest())

# Slightly modified text
inputstring = "come home tomorrow."
print("\nModified Text:")
print(inputstring)
output = hashlib.md5(inputstring.encode())
print("Hash of Modified Text:")
print(output.hexdigest())

# Reverted to original
inputstring = "come home tomorrow"
print("\nReverted Text:")
print(inputstring)
output = hashlib.md5(inputstring.encode())
print("Hash of Reverted Text:")
print(output.hexdigest())
