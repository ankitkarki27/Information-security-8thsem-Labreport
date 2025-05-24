def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    for c in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if c not in matrix and c.isalpha():
            matrix.append(c)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def preprocess(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    if len(pairs[-1]) == 1:
        pairs[-1] += 'X'
    return pairs

def transform(pairs, matrix, mode='encrypt'):
    result = ""
    shift = 1 if mode == 'encrypt' else -1
    for a, b in pairs:
        r1, c1 = find(matrix, a)
        r2, c2 = find(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5] + matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1] + matrix[(r2 + shift) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

# Inputs
key = "SECURE"
text = "INFORMATION SYSTEM"
matrix = generate_matrix(key)
pairs = preprocess(text)
cipher = transform(pairs, matrix, 'encrypt')
plain = transform(preprocess(cipher), matrix, 'decrypt')

# Output
print("Key Matrix:")
for row in matrix:
    print(row)
print("\nOriginal:", text)
print("Encrypted:", cipher)
print("Decrypted:", plain)
