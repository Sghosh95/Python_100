from unittest.mock import Mock

#instance of Mock
obj_mock=Mock()

#storing the result
obj_mock()
# obj_mock()

#asserting if called once or more than once
try:
    obj_mock.assert_called()
    obj_mock.assert_called_once()
    print("Test passed")
except AssertionError as error:
    raise error

print("Called?", obj_mock.called)  # True
print("Call count:", obj_mock.call_count)  # 1
