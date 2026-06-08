from pathlib import Path

import faiss
import numpy as np
import pandas as pd

from src.data.preprocess import build_document
from src.retrieval.embeddings import EmbeddingModel

DATA_FILE = "data/processed/products_10k.parquet"

INDEX_FILE = "data/indexes/faiss.index"

EMBED_FILE = "data/embeddings/product_embeddings.npy"


def main():

    Path("data/indexes").mkdir(
        parents=True,
        exist_ok=True
    )

    Path("data/embeddings").mkdir(
        parents=True,
        exist_ok=True
    )

    print("Loading products...")

    df = pd.read_parquet(DATA_FILE)

    docs = []

    for _, row in df.iterrows():
        docs.append(build_document(row))

    print(f"Encoding {len(docs)} products...")

    model = EmbeddingModel()

    embeddings = model.encode(docs)

    embeddings = embeddings.astype("float32")

    faiss.normalize_L2(embeddings)

    np.save(
        EMBED_FILE,
        embeddings
    )

    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)

    index.add(embeddings)

    faiss.write_index(
        index,
        INDEX_FILE
    )

    print("FAISS index saved")
    print(f"Embeddings shape: {embeddings.shape}")


if __name__ == "__main__":
    main()