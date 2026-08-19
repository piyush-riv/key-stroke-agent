from pathlib import Path
from langchain_community.vectorstores import FAISS

from .loader import load_knowledge
from .chunker import split_documents
from .embeddings import get_embeddings


VECTOR_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "faiss_index"


def create_vector_store():

    documents = load_knowledge()

    chunks = split_documents(documents)

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    VECTOR_DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    vector_store.save_local(str(VECTOR_DB_PATH))

    print("FAISS index created successfully.")

    return vector_store