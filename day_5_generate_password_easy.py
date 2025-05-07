import string
import random

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

lower_alphabets=[]
for elements in string.ascii_lowercase:
    lower_alphabets.append(elements)
# print(lower_alphabets)

upper_alphabets=[]
for elements in string.ascii_uppercase:
    upper_alphabets.append(elements)
# print(upper_alphabets)

alphabets=lower_alphabets+upper_alphabets
# print(alphabets)

#digit generation
digits=[]
for elements in string.digits:
    digits.append(elements)
# print(digits)

#symbols
symbols=[]
for elements in string.punctuation:
    symbols.append(elements)
# print(symbols)

num_alphabets=int(input("number of alphabets in password :"))
num_symbols=int(input("number of symbols in password :"))
num_digits=int(input("number of digits in password :"))

password=""

if num_alphabets+num_symbols+num_digits >=8:

    for elements in range(0,num_alphabets):
        password+=random.choice(alphabets)
    # print(password)
    
    for elements in range(0,num_digits):
        password+=random.choice(digits)
    # print(password)
    
    for elements in range(0,num_symbols):
        password+=random.choice(symbols)
    print(password)

else:
    print("Password length should be atleast 8")
