from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader


KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent / "knowledge"


def load_knowledge():
    loader = DirectoryLoader(
        str(KNOWLEDGE_DIR),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True,
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    return documents