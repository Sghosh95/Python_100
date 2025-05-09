import numpy as np
import pandas as pd
from datetime import datetime, timedelta


# define dataloader
def load_customer_data():
    
    # storing the current time
    now=datetime.now()

    # define the schema
    columns=["ID","Name","Manager_Name","Effective_from","Effective_to"]

    # give data
    data = [
        [1,"Sourav","Sourav",now, now+ timedelta(days=10)],
        [2,"Sourav","SG",now, now+ timedelta(days=10)],
        [3,"Sourav","SG1",now, now+ timedelta(days=20)],
        [4,"Sourav","SG2",now, now+ timedelta(days=30)],
        [5,"Sourav","SG3",now, now+ timedelta(days=40)],
    ]

    # give the columns type
    dtypes= {"ID": np.int64,
             "Name":str,
             "Manager_Name":str,
             "Effective_from": "datetime64[ns]",
             "Effective_to": "datetime64[ns]"
             }
    
    # Create and return the dataframe
    df = pd.DataFrame(data, columns=columns).astype(dtypes)
    print(df)
    return df
