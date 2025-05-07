import unittest


# define true false function
def is_even(number):
    if number%2==0:
        return True
    else:
        return False
    
# define the class for unit testing 
class testTrue_Fasle(unittest.TestCase):
    def testTrue_False(self):
        self.assertTrue(is_even(56))
        self.assertFalse(is_even(61))

# running the unit test

if __name__=="__main__":
    unittest.main()