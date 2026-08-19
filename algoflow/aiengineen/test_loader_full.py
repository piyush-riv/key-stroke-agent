from app.rag import DocumentLoader

loader = DocumentLoader()

files_to_test = [
    "test_data/sample.txt",
    "README.md",
    "test_data/sample.json",
]

for path in files_to_test:
    print(f"\n=== Loading: {path} ===")
    try:
        doc = loader.load(path)
        print("CONTENT:")
        print(doc.content)
        print("METADATA:", doc.metadata)
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}")