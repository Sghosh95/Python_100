# import the Mock class from unittest.mock

from unittest.mock import Mock

# create an instance of the Mock class
mock_instance=Mock()
# assigning a return value , suppose the definition was print(the string written)
mock_instance.return_value="The mock behaves like a function, but it is fake"

# store the Mock into result
result=mock_instance()

print(result)