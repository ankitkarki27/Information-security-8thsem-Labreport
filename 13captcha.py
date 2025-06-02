import random
import string

def generate_captcha(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def verify_human():
    captcha = generate_captcha()
    print(f"CAPTCHA: {captcha}")
    user_input = input("Enter the CAPTCHA to verify you're human: ")
    
    if user_input == captcha:
        print("Verification successful! You're human.")
        return True
    print("Verification failed. Try again.")
    return False

verify_human()