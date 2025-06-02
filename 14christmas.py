from datetime import date

today = date.today()
target = date(today.year, 12, 25)  # Christmas Day

def show_message():
    theTree = [0, 0, 1, 1, 3, 5, 7, 9, 13, 7,
               11, 15, 19, 11, 15, 19, 11, 15,
               19, 23, 27, 6, 6, 6, 0]

    for row in theTree:
        gap_size = int((14 - (0.5 * (row + 1))))
        print(" " * gap_size + "*" * row)
    print("\n>>>>> MERRY CHRISTMAS <<<<<\n")
    exit()

def bomb():
    if today == target:
        show_message()

print("Running normally,Today is not Christmas Day(25th December)...")
bomb()
