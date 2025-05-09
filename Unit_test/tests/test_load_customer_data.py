import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

from src.customer_loader import load_customer_data

class TestCustomerData(unittest.TestCase):
    @patch('src.customer_loader.load_customer_data')  # ✅ correct patch path
    def test_load_customer_data(self, mock_loader):
        now = datetime.now()

        # Build mock data with matching schema
        data = [
            [1, "Sourav", "Sourav", now, now + timedelta(days=10)],
            [2, "Sourav", "SG", now, now + timedelta(days=10)],
            [3, "Sourav", "SG1", now, now + timedelta(days=20)],
        ]
        columns = ["ID", "Name", "Manager_Name", "Effective_from", "Effective_to"]
        dtypes = {
            "ID": np.int64,
            "Name": str,
            "Manager_Name": str,
            "Effective_from": "datetime64[ns]",
            "Effective_to": "datetime64[ns]",
        }

        df = pd.DataFrame(data, columns=columns).astype(dtypes)
        mock_loader.return_value = df

        # Call the function and assert
        result = mock_loader()  # ✅ use the mock directly
        mock_loader.assert_called_once()

        # Use pandas testing utility
        pd.testing.assert_frame_equal(result, df)
        print("Called?", mock_loader.called)  # True
        print("Call count:", mock_loader.call_count)  # 1

# if __name__ == "__main__":
#     unittest.main()
