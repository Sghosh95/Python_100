#rock paper scissor

#rock=1
#scissor=2
#paper=3
import random

elements=["rock","paper","scissor"]
user_choice=int(input("Enter your choice :"))
print("you took :",user_choice)
computer_choice=random.randint(0,2)
print("computer took : ",computer_choice)

if user_choice==computer_choice:
    print("It is a draw")
elif user_choice>=3 or user_choice <0 :
    print("Invalid selection")
elif user_choice==0 and computer_choice==1:
    print("you lost")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice==1 and computer_choice==0:
    print("you win")
elif user_choice==1 and computer_choice==2:
    print("you lost")
elif user_choice>computer_choice:
    print("you win")
else:
    print("check again")
    
