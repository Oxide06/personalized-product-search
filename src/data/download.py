from datasets import load_dataset
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Downloading Amazon Electronics metadata...")

meta = load_dataset(
    "McAuley-Lab/Amazon-Reviews-2023",
    "raw_meta_Electronics",
    split="full[:50000]",  # start small
    trust_remote_code=True
)

df = meta.to_pandas()

output_path = DATA_DIR / "electronics_meta.parquet"

df.to_parquet(
    output_path,
    index=False
)

print(f"Saved {len(df)} products")
print(f"Saved to {output_path}")