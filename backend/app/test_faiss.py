from app.rag.vector_store import create_vector_store
from app.rag.retriever import get_retriever


print("Creating FAISS index...")

create_vector_store()

print("\nLoading retriever...")

retriever = get_retriever()

queries = [
    "When should I use two pointers?",
    "What is the time complexity of binary search?",
    "How do I find the middle of a linked list?"
]

for query in queries:

    print("\n" + "=" * 70)
    print("QUERY:", query)
    print("=" * 70)

    results = retriever.invoke(query)

    for i, document in enumerate(results, start=1):

        print(f"\n--- Result {i} ---")
        print(document.page_content)
        print("\nSource:", document.metadata.get("source"))