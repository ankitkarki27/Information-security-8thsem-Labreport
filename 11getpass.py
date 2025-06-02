import getpass

database = {"ram": "123456", "shyam": "654321"}
username = input("Enter username: ")

if username in database:
    while getpass.getpass("Enter password: ") != database[username]:
        print("Incorrect password, try again")
    print("Access granted")
else:
    print("User not found")