import pandas as pd

df = pd.read_parquet("data/raw/electronics_meta.parquet")

print("\nColumns:\n")
print(df.columns.tolist())

print("\nFirst row:\n")
print(df.iloc[0])