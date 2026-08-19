from pathlib import Path
from app.rag import DocumentLoader

loader = DocumentLoader()

files = list(Path("app/knowledge_base").rglob("*.md"))

print("TOTAL FILES:", len(files))
print()

success = 0
failed = 0

for file in files:
    try:
        document = loader.load(str(file))

        if document and document.content.strip():
            print("SUCCESS:", file)
            success += 1
        else:
            print("FAILED:", file)
            failed += 1

    except Exception as e:
        print("FAILED:", file)
        print("ERROR:", e)
        failed += 1

print()
print("========== SUMMARY ==========")
print("TOTAL:", len(files))
print("SUCCESSFUL:", success)
print("FAILED:", failed)