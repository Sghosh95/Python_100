#hangman

random_word_string=input("your word: ")
random_word=[]
for elements in random_word_string:
    random_word.append(elements)
print(random_word)
random_space=[]

for elements in random_word:
    random_space.append("_")
    
print(random_word)    
print(random_space)

#max_life
max_life=3

while max_life >0:
    guessed_letter=input("enter letter :")
    if random_space!=random_word:
        if guessed_letter in random_word:
            index=random_word.index(guessed_letter)
            print("index :",index)
            random_space[index]=guessed_letter
            print("random space filled :",random_space)
            print("life remaining :",max_life)
        else:
            max_life-=1
            print("life remaining:",max_life)
    else:
        print("word matched")
        break

print("game over")

