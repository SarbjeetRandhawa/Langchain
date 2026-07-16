import os
import datetime
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain_core.documents import Document

load_dotenv()

vectorstore = Chroma(embedding_function=OpenAIEmbeddings())

retriever = TimeWeightedVectorStoreRetriever(
    vectorstore=vectorstore, decay_rate=0.0001, k=1
)

now = datetime.datetime.now()

retriever.add_documents([
    Document(page_content="hello world", metadata={"last_accessed_at": now - datetime.timedelta(days=1)})
])

retriever.add_documents([
    Document(page_content="hello world", metadata={"last_accessed_at": now})
])

results = retriever.invoke("hello world")
print("Most recent/relevant doc's last accessed at:", results[0].metadata["last_accessed_at"])
