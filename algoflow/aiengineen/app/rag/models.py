from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Chunk:
    """A piece of a Document, ready for embedding."""
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def __len__(self) -> int:
        return len(self.content)

    def __repr__(self) -> str:
        preview = self.content[:50].replace("\n", " ")
        idx = self.metadata.get("chunk_index", "?")
        return f"Chunk(#{idx}, len={len(self.content)}, '{preview}...')"