import json
from pathlib import Path

from importlib import import_module

from .models import Document


class DocumentLoader:

    SUPPORTED_EXTENSIONS = {".txt", ".md", ".json", ".pdf"}

    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if not path.is_file():
            raise ValueError(
                f"Path is not a file: {file_path}"
            )

        extension = path.suffix.lower()

        if extension not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}. "
                f"Supported types: {self.SUPPORTED_EXTENSIONS}"
            )

        if extension in (".txt", ".md"):
            content = self._load_txt(path)

        elif extension == ".json":
            content = self._load_json(path)

        elif extension == ".pdf":
            content = self._load_pdf(path)

        content = self._normalize_text(content)

        if not content:
            raise ValueError(
                f"No usable text found in: {file_path}"
            )

        metadata = {
            "source": str(path),
            "filename": path.name,
            "file_type": extension[1:],
        }

        return Document(
            content=content,
            metadata=metadata,
        )

    def _load_txt(self, path: Path) -> str:
        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    def _load_json(self, path: Path) -> str:
        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
        )

    def _load_pdf(self, path: Path) -> str:
        try:
            pdf_module = import_module("pypdf")
        except ImportError as error:
            raise RuntimeError(
                "PDF support requires the 'pypdf' package to be installed."
            ) from error

        reader = pdf_module.PdfReader(str(path))

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)

    def _normalize_text(self, text: str) -> str:
        lines = []

        for line in text.splitlines():
            line = " ".join(line.split())

            if line:
                lines.append(line)

        return "\n".join(lines)