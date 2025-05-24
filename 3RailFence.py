def enc(msg, ord):
    msg = msg.replace(" ", "").upper()
    cols = len(ord)
    rows = (len(msg) + cols - 1) // cols
    padded_length = rows * cols
    msg = msg.ljust(padded_length, 'X')

    # Fill the grid row-wise
    grid = [list(msg[i:i+cols]) for i in range(0, len(msg), cols)]

    # Reorder columns by key
    pt = ''
    for index in ord:
        col = index - 1  # adjust for 0-indexed Python
        for row in grid:
            pt += row[col]
    return pt

def dec(pt, ord):
    cols = len(ord)
    rows = len(pt) // cols
    grid = [[''] * cols for _ in range(rows)]

    # Map ord to actual column positions
    pos_map = [0] * cols
    for i, pos in enumerate(ord):
        pos_map[pos - 1] = i

    # Fill columns in order
    k = 0
    for i in range(cols):
        col = pos_map[i]
        for row in range(rows):
            grid[row][col] = pt[k]
            k += 1

    # Read row-wise
    plain = ''.join(''.join(row) for row in grid)
    return plain

# Input
msg = "I WILL PASS EXAM"
ord = [1, 3, 5, 2, 4]

# Encrypt
encrypted = enc(msg, ord)
decrypted = dec(encrypted, ord)

print("Original msg :", msg)
print("Encrypted msg:", encrypted)
print("Decrypted msg:", decrypted)
