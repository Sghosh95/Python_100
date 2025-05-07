"""
The technique of hiding unnecessary data
"""

class Myclass:
    #initialize instance variable
    def __init__(self):
        self.a=10   #public variable
        self.__b=20  #private variable


#object instance
obj=Myclass()
print(obj.a) #publice variable , hence should be visible
# print(obj.b) #error since it is a private variable


#to access the private variable , we need to follow name mangling
# _classname__variable name
print(obj._Myclass__b)