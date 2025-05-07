class Person:
    name="a"
    age=20

    #define a method with the objects of the class can have
    def talk(cls):
        print(cls.name)
        print(cls.age)

#now create the object instance

object_p1=Person() #new instance
object_p1.talk()

