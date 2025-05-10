🧠 Step 1: What Is Mocking?
Mocking is faking or simulating parts of your system that are:
1. Slow (e.g., databases, APIs)
2. Not implemented yet
3. Irrelevant to the unit you're testing
This ensures your unit test is fast, isolated, and predictable.

>> Things you need to know :
1. Mock
2. Magic Mock
3. Patch
4. Side Effect

1. Mock : Mock is a class that lets you fake objects ( functions , methods ) for testing
for example : 
>> look into the mock and get an idea of how it is being used
>> Define return values
>> Set attributes 
>> Simulate Errors
>> You can assert whether it was called once or more than once