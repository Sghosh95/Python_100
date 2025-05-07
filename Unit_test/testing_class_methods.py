import unittest


# define a class
class calculator:
    # here self refers to the current object
    def square(self,x):

        return x*x
    
# test class
class testCalculator(unittest.TestCase):
    # def the function
    def testCalculator(self):
        #here self refers to the current testcase object
        #create instance of class
        obj_calc=calculator()
        self.assertEqual(obj_calc.square(4),16)
        self.assertLess(obj_calc.square(5),26)

# main to run all test cases in the file
if __name__=="__main__":
    unittest.main()