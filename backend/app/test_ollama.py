from app.llm.ollama import get_llm


llm = get_llm()

response = llm.invoke(
    "Explain binary search to a beginner in simple terms."
)

print("\n" + "=" * 60)
print("OLLAMA RESPONSE")
print("=" * 60)
print(response.content)