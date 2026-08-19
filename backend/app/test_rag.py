from app.rag.vector_store import create_vector_store
from app.rag.retriever import get_retriever


# Run this ONCE to create the index
create_vector_store()


retriever = get_retriever()

results = retriever.invoke(
    "When should I use two pointers?"
)

for i, document in enumerate(results, start=1):

    print("\n" + "=" * 50)
    print(f"RESULT {i}")
    print("=" * 50)

    print(document.page_content)
    print(document.metadata)