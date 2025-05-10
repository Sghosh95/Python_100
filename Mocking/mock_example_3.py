class APIClient:
    def fetch_data(self):
        return {"Status":200,"Logged":"Yes"}
# we define a class and a function

# Now we will mock the objects to test it

from unittest.mock import Mock , patch
# need to patch the class
@patch('__main__.APIClient')
def test_fetch_data(mock_client_class):
    mock_instance=mock_client_class.return_value
    mock_instance.fetch_data.return_value={"Status":200,"Logged":"Yes"}


    client = APIClient()
    result = client.fetch_data()
    print(result)  # {"status": 200, "data": "mock data"}

test_fetch_data()