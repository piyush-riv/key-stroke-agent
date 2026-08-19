from app.rag import DocumentLoader, TextChunker, Embedder, VectorStore

d = DocumentLoader().load('test_data/sample.txt')
chunks = TextChunker(chunk_size=80, chunk_overlap=20).split(d)

e = Embedder()
vectors = e.embed_chunks(chunks)

store = VectorStore(dimension=384)
store.add(chunks, vectors)

print('TOTAL VECTORS IN STORE:', len(store))

query = "how does binary search work"
query_vector = e.embed_text(query)

results = store.search(query_vector, top_k=2)

print(f'\nQUERY: "{query}"')
for chunk, distance in results:
    print(f'\n--- match (distance={distance:.4f}) ---')
    print(chunk.content)