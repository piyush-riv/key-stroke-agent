from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore
from app.rag.models import Chunk


class Retriever:
    """Wraps Embedder + VectorStore into a single retrieve() call."""

    def __init__(self, embedder: Embedder, vector_store: VectorStore):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 3) -> list[Chunk]:
        """Return the top_k chunks most relevant to the query."""
        query_vector = self.embedder.embed_text(query)
        results = self.vector_store.search(query_vector, top_k=top_k)
        return [chunk for chunk, _distance in results]

    def retrieve_with_scores(self, query: str, top_k: int = 3) -> list[tuple[Chunk, float]]:
        """Same as retrieve(), but also returns distance scores."""
        query_vector = self.embedder.embed_text(query)
        return self.vector_store.search(query_vector, top_k=top_k)