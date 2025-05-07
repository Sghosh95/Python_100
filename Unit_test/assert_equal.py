import unittest


# give the function definition
def add(a,b):
    return a+b

# write the class for unit test cases
# We need to give Testcase as the parameter
class testMath(unittest.TestCase):
    # now define the test case function
    def test_add(self):
        self.assertEqual(add(3,5),9)

# now the test defintion has been written , now we can call unittest.main to test it

if __name__=='__main__':
    unittest.main()