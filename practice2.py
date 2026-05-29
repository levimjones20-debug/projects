import random
import string
print("welcome to the password generator")
length = int(input("how long should the password be? "))
use_symbols = input("include symbols? (y/n) ")
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
if use_symbols == "y":
    all_chars = letters + numbers + symbols
else:
    all_chars = letters + numbers
password = ""
for i in range(length):
    password = password + random.choice(all_chars)
print(f"your password: {password}")
