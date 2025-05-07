# write the test cases with the same name of the python file



import unittest
from src.calculator import Calculator

# test class
class TestCalculator(unittest.TestCase):
    #test function
    def test_add(self):
        calc=Calculator()
        print("Testing add():")
        self.assertEqual(calc.add(2,3),5)

    def test_square(self):
        calc=Calculator()
        print("Testing Square():")
        self.assertEqual(calc.square(5),25)
