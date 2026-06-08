import faiss
import pandas as pd

from src.retrieval.embeddings import EmbeddingModel


class SemanticSearchEngine:

    def __init__(self):

        self.df = pd.read_parquet(
            "data/processed/products_10k.parquet"
        )

        self.index = faiss.read_index(
            "data/indexes/faiss.index"
        )

        self.model = EmbeddingModel()

    def search(
        self,
        query,
        top_k=10
    ):

        query_embedding = self.model.encode(
            [query]
        )

        query_embedding = query_embedding.astype(
            "float32"
        )

        faiss.normalize_L2(
            query_embedding
        )

        scores, ids = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(
            scores[0],
            ids[0]
        ):

            row = self.df.iloc[idx]

            results.append(
                {
                    "title": row["title"],
                    "asin": row["parent_asin"],
                    "score": float(score),
                }
            )

        return results