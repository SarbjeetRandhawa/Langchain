import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(
    ["Apples are red.", "Bananas are yellow.", "The sky is blue."],
    embedding=embeddings
)

# similarity_search is a method on the vector store itself
docs = vectorstore.similarity_search("What color is a banana?", k=1)
print(docs)
