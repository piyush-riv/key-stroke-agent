from app.rag import DocumentLoader

d = DocumentLoader().load('README.md')
print('CONTENT:')
print(d.content)
print('METADATA:', d.metadata)