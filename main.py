import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lowercase_letters = uppercase_letters.lower()

digits = "0123456789"

upper, lower, nums = True, True,True

all =""

if upper:
    all+=uppercase_letters
if lower:
    all+=lowercase_letters
if nums:
    all+= digits
    
length = 6
amount = 20

for x in range(amount):
    password = "".join(random.sample(all, length))
    
    print(password)


