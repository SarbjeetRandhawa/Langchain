import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings()
# MMR is useful when you have many similar documents and want diverse results
vectorstore = Chroma.from_texts(
    [
        "LangChain is awesome for LLMs.", 
        "LangChain makes LLM development easy.", 
        "LangChain provides tools for RAG.",
        "Python is a popular programming language."
    ],
    embedding=embeddings
)

# Create an MMR retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2, "fetch_k": 4} # Fetch 4, return the 2 most diverse
)

docs = retriever.invoke("What is LangChain?")
for i, doc in enumerate(docs):
    print(f"Doc {i+1}: {doc.page_content}")
