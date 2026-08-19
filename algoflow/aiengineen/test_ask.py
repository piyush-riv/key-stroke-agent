from pathlib import Path

from app.rag import (
    DocumentLoader,
    TextChunker,
    Embedder,
    VectorStore,
    Retriever
)



KNOWLEDGE_BASE = Path("app/knowledge_base")


print("Loading and indexing your knowledge base...\n")




loader = DocumentLoader()

chunker = TextChunker(
    chunk_size=200,
    chunk_overlap=40
)

embedder = Embedder()

store = VectorStore(
    dimension=384
)




files_to_index = list(KNOWLEDGE_BASE.rglob("*.md"))

print(f"Found {len(files_to_index)} knowledge-base files.\n")



all_chunks = []

for path in files_to_index:

    try:
        doc = loader.load(str(path))

        chunks = chunker.split(doc)

        all_chunks.extend(chunks)

    except Exception as e:

        print(f"Skipping {path}: {e}")




print("\nCreating embeddings...")

vectors = embedder.embed_chunks(all_chunks)




store.add(all_chunks, vectors)




retriever = Retriever(
    embedder=embedder,
    vector_store=store
)




print()
print("=" * 50)
print("KNOWLEDGE BASE INDEXED")
print("=" * 50)

print(f"Files:   {len(files_to_index)}")
print(f"Chunks:  {len(all_chunks)}")
print(f"Vectors: {len(vectors)}")
print(f"FAISS:   {len(store)}")

print("=" * 50)

print("\nAsk a question about your DSA knowledge base.")
print("Type 'exit' or 'quit' to stop.\n")



while True:

    query = input("You: ").strip()


    # Exit
    if query.lower() in ("exit", "quit"):

        print("Bye!")

        break


    # Ignore empty questions
    if not query:
        continue


   

    results = retriever.retrieve_with_scores(
        query,
        top_k=3
    )


   

    print(f'\nTop matches for: "{query}"')

    print("-" * 50)


    for i, (chunk, distance) in enumerate(results):

        source = chunk.metadata.get(
            "filename",
            "unknown"
        )

        print(
            f"\n--- Result {i + 1} ---"
        )

        print(
            f"Source: {source}"
        )

        print(
            f"Distance: {distance:.4f}"
        )

        print()

        print(chunk.content)


    print()