from app.rag.loader import load_knowledge
from app.rag.chunker import split_documents


documents = load_knowledge()

print(f"\nDocuments loaded: {len(documents)}")

chunks = split_documents(documents)

print(f"Chunks created: {len(chunks)}")

for i, chunk in enumerate(chunks[:10]):
    print("\n" + "=" * 60)
    print(f"CHUNK {i + 1}")
    print("=" * 60)

    print(chunk.page_content)

    print("\nMETADATA:")
    print(chunk.metadata)