from app.rag.models import Chunk, Document


class TextChunker:
    """Recursively splits text on natural boundaries with overlap."""

    DEFAULT_SEPARATORS = ["\n\n", "\n", ". ", " ", ""]

    def __init__(
        self,
        chunk_size: int = 600,
        chunk_overlap: int = 100,
        separators: list[str] | None = None,
    ):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if chunk_overlap < 0:
            raise ValueError("chunk_overlap cannot be negative")
        if chunk_overlap >= chunk_size:
            raise ValueError(
                f"chunk_overlap ({chunk_overlap}) must be < chunk_size ({chunk_size})"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or self.DEFAULT_SEPARATORS

    def split(self, document: Document) -> list[Chunk]:
        """Split a Document into overlapping Chunks."""
        texts = self.split_text(document.content)

        return [
            Chunk(
                content=text,
                metadata={
                    **document.metadata,
                    "chunk_index": i,
                    "total_chunks": len(texts),
                    "chunk_length": len(text),
                },
            )
            for i, text in enumerate(texts)
        ]

    def split_documents(self, documents: list[Document]) -> list[Chunk]:
        """Split many Documents into one flat list of Chunks."""
        chunks = []
        for doc in documents:
            chunks.extend(self.split(doc))
        return chunks

    def split_text(self, text: str) -> list[str]:
        """Split a raw string into chunk-sized strings."""
        if not text or not text.strip():
            return []

        pieces = self._recursive_split(text, self.separators)
        return self._merge(pieces)

    def _recursive_split(self, text: str, separators: list[str]) -> list[str]:
        """Break text into pieces, each <= chunk_size where possible."""
        if len(text) <= self.chunk_size:
            return [text]

        separator, remaining = self._pick_separator(text, separators)

        if separator == "":
            return self._hard_split(text)

        parts = text.split(separator)
        parts = [p + separator for p in parts[:-1]] + [parts[-1]]

        out = []
        for part in parts:
            if not part:
                continue
            if len(part) <= self.chunk_size:
                out.append(part)
            else:
                out.extend(self._recursive_split(part, remaining))
        return out

    def _pick_separator(
        self, text: str, separators: list[str]
    ) -> tuple[str, list[str]]:
        """Return the first separator present in text, plus the finer ones."""
        for i, sep in enumerate(separators):
            if sep == "":
                return "", []
            if sep in text:
                return sep, separators[i + 1:]
        return "", []

    def _hard_split(self, text: str) -> list[str]:
        """Last resort: cut mid-word at fixed size."""
        return [
            text[i:i + self.chunk_size]
            for i in range(0, len(text), self.chunk_size)
        ]

    def _merge(self, pieces: list[str]) -> list[str]:
        """Greedily pack pieces into chunks, carrying overlap forward."""
        chunks: list[str] = []
        current: list[str] = []
        current_len = 0

        for piece in pieces:
            piece_len = len(piece)

            if current and current_len + piece_len > self.chunk_size:
                chunks.append("".join(current))
                current, current_len = self._carry_overlap(current)

            current.append(piece)
            current_len += piece_len

        if current:
            chunks.append("".join(current))

        return [c.strip() for c in chunks if c.strip()]

    def _carry_overlap(self, pieces: list[str]) -> tuple[list[str], int]:
        """Keep trailing pieces up to chunk_overlap chars for the next chunk."""
        carried: list[str] = []
        total = 0

        for piece in reversed(pieces):
            if total + len(piece) > self.chunk_overlap:
                break
            carried.insert(0, piece)
            total += len(piece)

        return carried, total