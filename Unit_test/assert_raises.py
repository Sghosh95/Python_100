import unittest


#define the function
def divide(a,b):
    if b==0:
        raise ValueError("Division by Zero")
    return a/b

# define class unittest
class TestDivide(unittest.TestCase):
    #define unittest function
    def test_divide(self):
        with self.assertRaises(ValueError):
            divide(10,0)


# class for assertIn and assertNotIn
class TestList(unittest.TestCase):
    #define the function
    def test_membership(self):
        members=["a","b","c"]
        self.assertIn("a",members)
        self.assertIsNot("d",members)

# class for assertIsNone and assertIsNotNone
def maybe_none(number):
    if number<0:
        return None
    else:
        return number

class TestNone(unittest.TestCase):
    # def test function
    def test_maybe_none(self):
        self.assertIsNone(maybe_none(-5))
        self.assertIsNotNone(maybe_none(5))


# main
if __name__=='__main__':
    unittest.main()