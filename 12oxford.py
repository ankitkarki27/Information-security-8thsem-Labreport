import hashlib
from urllib.request import urlopen

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/2df55facf06c7742f2038a8f6607ea9071596128/Real-Passwords/Top1575-probable-v2.txt'
target_pw = 'oxford'
target_hash = hash_pw(target_pw)

try:
    wordlist = urlopen(url).read().decode().splitlines()
    for word in wordlist:
        if hash_pw(word) == target_hash:
            print(f"Vulnerable! Password found: {word}")
            break
    else:
        print("Password not found in wordlist.")
except:
    print("Failed to load wordlist.")
