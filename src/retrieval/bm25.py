import pickle
from pathlib import Path

import pandas as pd
from rank_bm25 import BM25Okapi

from src.data.preprocess import (
    build_document,
    tokenize,
)


class BM25SearchEngine:

    def __init__(self):
        self.df = None
        self.bm25 = None

    def build(self, parquet_path):

        print("Loading products...")

        self.df = pd.read_parquet(parquet_path)

        documents = [
            build_document(row)
            for _, row in self.df.iterrows()
        ]

        documents = [
            doc
            for doc in documents
            if doc.strip()
        ]

        print("Tokenizing...")

        tokenized_docs = [
            tokenize(doc)
            for doc in documents
        ]

        print("Building BM25 index...")

        self.bm25 = BM25Okapi(tokenized_docs)

        print("BM25 ready.")

    def save(self, path):

        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(path, "wb") as f:

            pickle.dump(
                {
                    "bm25": self.bm25,
                    "df": self.df
                },
                f
            )

        print(f"Saved index -> {path}")

    def load(self, path):

        with open(path, "rb") as f:

            data = pickle.load(f)

        self.bm25 = data["bm25"]
        self.df = data["df"]

        print(f"Loaded index -> {path}")

    def search(self, query, top_k=10):

        query_tokens = tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        top_indices = scores.argsort()[-top_k:][::-1]

        results = []

        for idx in top_indices:

            row = self.df.iloc[idx]

            results.append(
                {
                    "title": row.get("title", ""),
                    "score": float(scores[idx]),
                    "asin": row.get("parent_asin", ""),
                }
            )

        return results