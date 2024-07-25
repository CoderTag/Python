# password generator
import string
import random

symbols = ['!', '@', '#', '$', '%']
numbers = list(range(0,10))
letters = list(string.ascii_letters)
# pwd_len = int(input("Enter password length: "))
pwd_num = int(input("Enter the number of numbers in password: "))
pwd_sym = int(input("Enter the number of symbols in password: "))
pwd_let = int(input("Enter the number of letters in password: "))

pwd = ''

for num in range(0, pwd_let):
    pwd += random.choice(letters)

for num in range(0, pwd_sym):
    pwd += random.choice(symbols)

for num in range(0, pwd_num):
    pwd += str(random.choice(numbers))

pwd_list = list(pwd)
random.shuffle(pwd_list)
pwd_list = ''.join(pwd_list)
print(pwd)
print(pwd_list)

