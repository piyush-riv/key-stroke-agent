from pathlib import Path
from langchain_community.vectorstores import FAISS

from .embeddings import get_embeddings


VECTOR_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "faiss_index"


def get_retriever():

    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        str(VECTOR_DB_PATH),
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    return retriever