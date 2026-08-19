from sentence_transformers import SentenceTransformer

from app.rag.models import Chunk


class Embedder:
    """Turns text chunks into vectors using a Hugging Face model."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str) -> list[float]:
        """Embed a single raw string."""
        vector = self.model.encode(text, convert_to_numpy=True)
        return vector.tolist()

    def embed_chunk(self, chunk: Chunk) -> list[float]:
        """Embed a single Chunk's content."""
        return self.embed_text(chunk.content)

    def embed_chunks(self, chunks: list[Chunk]) -> list[list[float]]:
        """Embed many Chunks in one batch (faster than one at a time)."""
        texts = [c.content for c in chunks]
        vectors = self.model.encode(texts, convert_to_numpy=True)
        return [v.tolist() for v in vectors]