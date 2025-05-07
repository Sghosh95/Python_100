import random
word_list=["sourav","ghosh"]
lives=6
choosen_word=random.choice(word_list)
print(choosen_word)

placeholder=""
for position in range(len(choosen_word)):
    placeholder+="_"
print(placeholder)



game_over=False
correct_letters=[]
while not game_over:
    guess=input("Guess a letter :").lower()
    print(guess)

    # #check if the letter is one of the letter of the chosen word.print right if it is, else print wrong.
    display=""
    for letter in choosen_word:
        if guess==letter:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)

    if guess not in choosen_word:
        lives-=1
        print("life remaining :",lives)
        if lives==0 and display!=choosen_word:
            game_over=True
            print("you lost")

    if "_" not in display and display==choosen_word:
        game_over=True
        print("you win")




