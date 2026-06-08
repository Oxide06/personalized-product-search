from src.retrieval.bm25 import BM25SearchEngine

INDEX_FILE = "data/indexes/bm25.pkl"


def main():

    engine = BM25SearchEngine()

    engine.load(INDEX_FILE)

    print("\nAmazon Search V1")
    print("Type 'exit' to quit\n")

    while True:

        query = input("Search > ")

        if query.lower() == "exit":
            break

        results = engine.search(query)

        print()

        for i, item in enumerate(results, start=1):

            print(f"{i}. {item['title']}")
            print(f"   Score: {item['score']:.2f}")
            print(f"   ASIN : {item['asin']}")
            print()

        print("-" * 60)


if __name__ == "__main__":
    main()