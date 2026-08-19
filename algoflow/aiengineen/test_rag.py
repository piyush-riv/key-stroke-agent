from app.rag import DocumentLoader, TextChunker

d = DocumentLoader().load('test_data/sample.txt')
c = TextChunker(chunk_size=80, chunk_overlap=20).split(d)

print('TOTAL CHUNKS:', len(c))

for x in c:
    idx = x.metadata['chunk_index']
    print(f'\n--- Chunk #{idx} (len={len(x)}) ---')
    print(x.content)