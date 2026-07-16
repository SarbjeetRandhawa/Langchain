import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever

load_dotenv()

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(
    ["The latest iPhone has a great camera.", "Apple announced new MacBooks."],
    embedding=embeddings
)

llm = ChatOpenAI(temperature=0)

# MultiQueryRetriever generates multiple variants of the query
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(), 
    llm=llm
)

docs = retriever_from_llm.invoke("What did Apple recently release?")
print(f"Retrieved {len(docs)} documents.")
