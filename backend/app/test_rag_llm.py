from app.rag.retriever import get_retriever
from app.llm.ollama import get_llm


retriever = get_retriever()
llm = get_llm()

question = "When should I use two pointers?"

print("\nRetrieving DSA knowledge...")

results = retriever.invoke(question)

context = "\n\n".join(
    document.page_content
    for document in results
)

print("\nRetrieved context:")
print(context)

prompt = f"""
You are an AI DSA coding coach.

Use the following retrieved DSA knowledge:

{context}

Student question:
{question}

Give a concise conceptual explanation.
Do not immediately provide a complete coding solution.
"""

print("\nCalling Llama 3.2...")

response = llm.invoke(prompt)

print("\n" + "=" * 60)
print("LLAMA RESPONSE")
print("=" * 60)

print(response.content)