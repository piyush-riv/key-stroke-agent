from app.rag.embeddings import get_embeddings


print("Loading embedding model...")

embeddings = get_embeddings()

text = "When should I use the two pointer technique?"

print("\nCreating embedding...")

vector = embeddings.embed_query(text)

print("\nEmbedding created successfully!")
print("Vector dimension:", len(vector))
print("First 10 values:", vector[:10])