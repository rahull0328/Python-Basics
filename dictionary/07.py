# Convert a dictionary into a DataFrame (using pandas)

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [22, 21, 23],
    'Grade': ['A', 'B', 'A']
}

df = pd.DataFrame(data)
print(df)
