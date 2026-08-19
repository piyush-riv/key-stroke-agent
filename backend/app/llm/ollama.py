from langchain_ollama import ChatOllama


def get_llm():

    return ChatOllama(
        model="llama3.2:latest",
        temperature=0.2,
    )