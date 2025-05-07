import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)

lower_alphabets=[]
for elements in string.ascii_lowercase:
    lower_alphabets.append(elements)
print(lower_alphabets)

upper_alphabets=[]
for elements in string.ascii_uppercase:
    upper_alphabets.append(elements)
print(upper_alphabets)

alphabets=lower_alphabets+upper_alphabets
print(alphabets)

#digit generation
digits=[]
for elements in string.digits:
    digits.append(elements)
print(digits)

#symbols
symbols=[]
for elements in string.punctuation:
    symbols.append(elements)
print(symbols)
