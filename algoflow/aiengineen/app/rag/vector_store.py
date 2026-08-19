import numpy as np
import faiss

from app.rag.models import Chunk


class VectorStore:
    """FAISS-backed similarity index over embedded Chunks."""

    def __init__(self, dimension: int = 384):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks: list[Chunk] = []

    def add(self, chunks: list[Chunk], vectors: list[list[float]]) -> None:
        """Add chunks and their vectors to the index."""
        if len(chunks) != len(vectors):
            raise ValueError(
                f"chunks ({len(chunks)}) and vectors ({len(vectors)}) "
                "must be the same length"
            )

        array = np.array(vectors, dtype="float32")
        self.index.add(array)
        self.chunks.extend(chunks)

    def search(self, query_vector: list[float], top_k: int = 3) -> list[tuple[Chunk, float]]:
        """Return the top_k most similar chunks to the query vector."""
        if self.index.ntotal == 0:
            return []

        query_array = np.array([query_vector], dtype="float32")
        distances, indices = self.index.search(query_array, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx == -1:
                continue
            results.append((self.chunks[idx], float(dist)))

        return results

    def __len__(self) -> int:
        return self.index.ntotal