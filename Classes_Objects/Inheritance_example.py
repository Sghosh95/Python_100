class A:
    a=1
    b=2

    def method(self):
        print(self.a)
        print(self.b)

# Class B inherits Class A : all the elements of class A will be accessible to Class B

class B(A):
    c=3

    def method2(cls):
        print(cls.c)


# By creating an object of B , we can access both the classed A and B
obj=B()
obj.method()
obj.method2()