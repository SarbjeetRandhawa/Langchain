import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever

load_dotenv()

doc_list = [
    "I like apples",
    "I like oranges",
    "Apples and oranges are fruits",
]

bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 2

embedding = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(doc_list, embedding)
vectorstore_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Combine them into an EnsembleRetriever (Hybrid Search)
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vectorstore_retriever], 
    weights=[0.5, 0.5]
)

docs = ensemble_retriever.invoke("apples")
print("Ensemble Results:")
for doc in docs:
    print(doc.page_content)
