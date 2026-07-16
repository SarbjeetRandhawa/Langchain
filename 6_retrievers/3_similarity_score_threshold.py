import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(
    ["I love machine learning.", "The weather is nice today.", "Deep learning is a subset of ML."],
    embedding=embeddings
)

# Create a retriever that uses a similarity score threshold
retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.8, "k": 3}
)

docs = retriever.invoke("Tell me about artificial intelligence.")
print(docs)
