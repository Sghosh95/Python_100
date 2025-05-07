import unittest
from src.string_utils import capitalize,reverse



class TestStringUtils(unittest.TestCase):
    def test_captitalize(self):
        self.assertEqual(capitalize("hello"),"Hello")


    def test_reverse(self):
        self.assertEqual(reverse("abc"),"cba")