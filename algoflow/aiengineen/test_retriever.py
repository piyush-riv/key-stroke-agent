from pathlib import Path

from app.rag import (
    DocumentLoader,
    TextChunker,
    Embedder,
    VectorStore,
    Retriever
)




KNOWLEDGE_BASE = Path("app/knowledge_base")



loader = DocumentLoader()

documents = []

for file_path in KNOWLEDGE_BASE.rglob("*.md"):
    document = loader.load(str(file_path))
    documents.append(document)

print("TOTAL DOCUMENTS:", len(documents))



chunker = TextChunker(
    chunk_size=500,
    chunk_overlap=50
)

chunks = chunker.split_documents(documents)

print("TOTAL CHUNKS:", len(chunks))




embedder = Embedder()

vectors = embedder.embed_chunks(chunks)

print("TOTAL VECTORS:", len(vectors))




store = VectorStore(dimension=384)

store.add(chunks, vectors)

print("VECTOR STORE SIZE:", len(store))




retriever = Retriever(
    embedder=embedder,
    vector_store=store
)




query = "how does binary search work"

results = retriever.retrieve(
    query,
    top_k=5
)




print()
print(f'QUERY: "{query}"')
print(f"RETRIEVED {len(results)} CHUNKS:")
print()

for i, chunk in enumerate(results):

    print(f"--- Chunk {i} ---")
    print(chunk.content)
    print()