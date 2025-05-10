## What is Unit Testing?
1. Testing small pieces of code (usually functions or methods).
2. Ensures individual units of code behave as expected.




## Why Use It?
1. Catches bugs early

2. Ensures code reliability

3. Simplifies debugging and refactoring




Assertion	                Description
assertEqual(a, b)	        a == b
assertNotEqual(a, b)        a != b
assertTrue(x)	            bool(x) is True
assertFalse(x)	            bool(x) is False
assertIs(a, b)	            a is b
assertIsNone(x)	            x is None
assertRaises(Error, func)	Checks if error is raised


# How to run coverage if there are multiple test files

1. follow the structure 

your_project/
├── calculator.py
├── string_utils.py
├── tests/
│   ├── test_calculator.py
│   └── test_string_utils.py
└── main.py

2. All the test files should be under the test subfolder

3. And the main will run all the tests

4. Showing test case results

✅ Option 1: Use -v (Verbose Mode) with unittest
python -m unittest discover -s tests -p "test_*.py" -v 

✅ Option 2: Add Print Statements (Not Recommended for Final Code)



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. For Coverage useful for gitflow:

>> install coverage : pip install coverage

Run the test with coverage which will generate .coverage file
>> coverage run -m unittest discover -s tests -p "test_*.py" 

Generate report :
>> coverage report 
Name                         Stmts   Miss  Cover
------------------------------------------------
src\calculator.py                5      0   100%
src\string_utils.py              4      0   100%
tests\test_calculator.py        11      0   100%
tests\test_string_utils.py       7      0   100%
------------------------------------------------
TOTAL                           27      0   100%

Generate xml :
>> coverage xml


