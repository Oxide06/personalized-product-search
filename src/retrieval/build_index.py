from src.retrieval.bm25 import BM25SearchEngine

PARQUET_FILE = "data/raw/electronics_meta.parquet"
INDEX_FILE = "data/indexes/bm25.pkl"

engine = BM25SearchEngine()

engine.build(PARQUET_FILE)

engine.save(INDEX_FILE)