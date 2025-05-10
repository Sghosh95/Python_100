from unittest.mock import Mock

# check what params the mock was called with
mock_instance=Mock()

# calling with parameters
mock_instance("Sourav","mock examples")

# assert with called parameters
try:
    mock_instance.assert_called_once_with("Sourav","mock examples")
    print("Call count :",mock_instance.call_count)
    print("Called with :",mock_instance.call_args)
except AssertionError as e:
    raise e