from pathlib import Path
import pandas as pd

INPUT_FILE = "data/raw/electronics_meta.parquet"
OUTPUT_FILE = "data/processed/products_10k.parquet"

# Create folder if missing
Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)

print("Loading raw data...")

df = pd.read_parquet(INPUT_FILE)

df = df.head(10000)

keep_cols = [
    "title",
    "description",
    "categories",
    "store",
    "parent_asin"
]

df = df[keep_cols]

df.to_parquet(
    OUTPUT_FILE,
    index=False
)

print(f"Saved {len(df)} products")
print(f"Saved to {OUTPUT_FILE}")