from src.retrieval.bm25 import BM25SearchEngine
from src.retrieval.faiss_search import SemanticSearchEngine

BM25_INDEX = "data/indexes/bm25.pkl"


def print_results(results):
    print()

    for i, item in enumerate(results, start=1):

        print(f"{i}. {item['title']}")

        print(f"   Score: {item['score']:.4f}")

        print(f"   ASIN : {item['asin']}")

        print()

    print("-" * 60)


def main():

    print("Loading BM25...")
    bm25 = BM25SearchEngine()
    bm25.load(BM25_INDEX)

    print("Loading Semantic Search...")
    semantic = SemanticSearchEngine()

    print("\nAmazon Product Search V2\n")

    while True:

        print("\nChoose Mode")
        print("1. BM25")
        print("2. Semantic")
        print("3. Exit")

        mode = input("> ")

        if mode == "3":
            break

        query = input("\nSearch > ")

        if mode == "1":
            results = bm25.search(query)

        elif mode == "2":
            results = semantic.search(query)

        else:
            print("Invalid choice")
            continue

        print_results(results)


if __name__ == "__main__":
    main()