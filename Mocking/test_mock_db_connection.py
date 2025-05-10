import unittest
from unittest.mock import Mock , patch
from mock_db_connection import get_user

class TestDB(unittest.TestCase):
    @patch('mock_db_connection.mysql.connector.connect')
    def test_get_user(self, mock_connect):
        # Create a mock connection and cursor to replicate as real
        mock_conn=Mock()
        mock_cursor=Mock()

        # Set up the return value
        mock_conn.is_connected.return_value=True
        mock_cursor.fetchall.return_value = [("John", "Doe"), ("Alice", "Smith")]

        mock_conn.cursor.return_value=mock_cursor
        mock_connect.return_value=mock_conn

        # call the function
        result=get_user()
        print("result :",result)
        print("mock result:",mock_cursor.fetchall.return_value)

        # Assertions
        self.assertEqual(result, [("John", "Doe"), ("Alice", "Smith")])
        mock_cursor.execute.assert_called_once_with("SELECT * FROM customer")
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()