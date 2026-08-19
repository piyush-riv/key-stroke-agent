from app.rag import DocumentLoader, TextChunker, Embedder

d = DocumentLoader().load('test_data/sample.txt')
chunks = TextChunker(chunk_size=80, chunk_overlap=20).split(d)

e = Embedder()
vectors = e.embed_chunks(chunks)

print('CHUNKS:', len(chunks))
print('VECTOR DIMENSION:', len(vectors[0]))
print('FIRST VECTOR (first 5 values):', vectors[0][:5])
print('CHUNK TEXT:', chunks[0].content)