import unittest


# define the function
def multiply(a,b):
    return a*b

# class for the unit test
class TestMath(unittest.TestCase):
    # define test function
    def test_multiply(self):
        self.assertNotEqual(multiply(3,5),18)


#running the unit test :from unittest.main
if __name__=="__main__":
    unittest.main()