"""
The variables and methods that act together on the data is binded together : Encapsulation
"""

class Student:
    #creating instance variable : means the copies will be available into the object
    def __init__(self): 
        self.id=10
        self.name="SG"

    #now with the self : the object method knows about the self variables
    def display_details(self):
        print(self.id)
        print(self.name)

#create instance
obj=Student()
obj.display_details()