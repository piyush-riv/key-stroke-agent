from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)


def split_documents(documents):

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "h1"),
            ("##", "h2"),
            ("###", "h3"),
        ],
        strip_headers=False,
    )

    character_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
    )

    final_chunks = []

    for document in documents:

        sections = header_splitter.split_text(
            document.page_content
        )

        for section in sections:
            section.metadata.update(document.metadata)

        chunks = character_splitter.split_documents(sections)

        final_chunks.extend(chunks)

    print(f"Created {len(final_chunks)} chunks")

    return final_chunks