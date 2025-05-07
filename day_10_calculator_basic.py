def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2 
def division(n1,n2):
    return n1/n2


restart=False
result=0
while restart!=True:
    #choice of operation
    print("choice: \n1.addition\n2.substract\n3.multiply\n4.division")
    choice=input("Enter your choice :").lower()
    if choice=="restart":
        restart=True
    elif choice=="addition":
        n1=int(input("Enter first number :"))
        n2=int(input("Enter second number :"))
        result=add(n1,n2)
    elif choice=="substract":
        n1=int(input("Enter first number :"))
        n2=int(input("Enter second number :"))
        result=substract(n1,n2)
    elif choice=="multiply":
        n1=int(input("Enter first number :"))
        n2=int(input("Enter second number :"))
        result=multiply(n1,n2)
    elif choice=="division":
        n1=int(input("Enter first number :"))
        n2=int(input("Enter second number :"))
        result=division(n1,n2)
    else:
        print("Wrong operation")
        
    print(f"Operation :{choice} , Result : {result}")   
        
    
    
