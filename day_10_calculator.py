def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2 
def division(n1,n2):
    return n1/n2

#try to use dictionary
operations={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":division
    ,
}

# print(operations["+"](8,4))
def calculator():
    continue_operation=True
    num1=float(input("Enter the first number.:"))
    
    while continue_operation:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick one symbol :")
        num2=float(input("Enter the second number.:"))
        result=operations[operation_symbol](num1,num2) #operations["+"]=add , add(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        
        choice=input("Y to continue with last result or N to restart").lower()
        
        if choice=="y":
            num1=result
        elif choice=="n":
            continue_operation=False
            calculator()
        else:
            exit()
 
calculator()          
