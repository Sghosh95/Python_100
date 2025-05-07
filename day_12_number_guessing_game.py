import random

actual_number=random.randint(1,100)
print(actual_number)
print("\n"*30)
print("Welcome to the number guessing game :")
difficulty=input("choose a difficultyu level : hard or easy ").lower()
print("Your game difficulty level :",difficulty)
if difficulty=="easy":
    number_of_attempts=5
elif difficulty=="hard":
    number_of_attempts=10

match=0
while number_of_attempts!=0 and match!=1:
    print("Number of attempts left :",number_of_attempts)
    guessed_number=int(input("Guess a number :"))
    if guessed_number > actual_number:
    # if guessed_number-actual_number>=30:
        print("too high")
    elif guessed_number<actual_number:
        print("too low")
    elif guessed_number==actual_number:
        match=1
    number_of_attempts-=1

if match==1:
    print("Guessed number and number matched",guessed_number)
else:
    print("you lost the game")
    
    
