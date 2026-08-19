from app.rag import DocumentLoader, TextChunker

# Load document
d = DocumentLoader().load("test_data/sample.txt")

# Create chunker with small size to force splits
chunker = TextChunker(chunk_size=80, chunk_overlap=20)

# Split into chunks
chunks = chunker.split(d)

print("TOTAL CHUNKS:", len(chunks))
print()

for chunk in chunks:
    idx = chunk.metadata["chunk_index"]
    print(f"--- Chunk #{idx} (len={len(chunk)}) ---")
    print(chunk.content)
    print(f"METADATA: {chunk.metadata}")
    print()