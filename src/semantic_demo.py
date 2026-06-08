from src.retrieval.faiss_search import (
    SemanticSearchEngine
)

engine = SemanticSearchEngine()

print("\nSemantic Search V2")
print("Type 'exit' to quit\n")

while True:

    query = input("Search > ")

    if query.lower() == "exit":
        break

    results = engine.search(query)

    print()

    for i, item in enumerate(
        results,
        start=1
    ):

        print(
            f"{i}. {item['title']}"
        )

        print(
            f"   Score: {item['score']:.4f}"
        )

        print(
            f"   ASIN : {item['asin']}"
        )

        print()

    print("-" * 60)