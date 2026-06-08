from src.retrieval.bm25 import BM25SearchEngine
from src.retrieval.faiss_search import SemanticSearchEngine

QUERIES = [
    "gaming mouse",
    "wireless pointer",
    "portable audio",
    "travel charger",
    "video recording camera",
]

bm25 = BM25SearchEngine()
bm25.load("data/indexes/bm25.pkl")

semantic = SemanticSearchEngine()

for query in QUERIES:

    print("\n" + "=" * 80)
    print("QUERY:", query)

    print("\nBM25")

    for item in bm25.search(query, top_k=5):

        print(item["title"])

    print("\nSEMANTIC")

    for item in semantic.search(query, top_k=5):

        print(item["title"])