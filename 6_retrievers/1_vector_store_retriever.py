import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# Initialize embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(
    ["LangChain is a framework for developing applications powered by LLMs.", 
     "Vector stores are databases for storing embeddings."],
    embedding=embeddings
)

# Create a standard VectorStoreRetriever
retriever = vectorstore.as_retriever()

# Retrieve documents
docs = retriever.invoke("What is LangChain?")
print(docs)
