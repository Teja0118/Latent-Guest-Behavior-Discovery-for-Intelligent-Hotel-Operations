import pandas as pd

df = pd.read_csv('./app/data/hospitality_operations_03.csv')

data_shape = df.shape
print(f"Dataset Shape: {data_shape}")
print(f"Number of rows: {data_shape[0]}")
print(f"Number of columns: {data_shape[1]}")

data_columns = df.columns
print(f"Dataset columns: \n {data_columns}")


