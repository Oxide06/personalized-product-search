from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):

        print("Loading MiniLM model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def encode(self, texts):

        return self.model.encode(
            texts,
            batch_size=16,
            show_progress_bar=True,
            convert_to_numpy=True
        )