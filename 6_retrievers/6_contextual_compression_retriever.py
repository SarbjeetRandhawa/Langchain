import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

load_dotenv()

llm = ChatOpenAI(temperature=0)
embeddings = OpenAIEmbeddings()

texts = [
    "The town of Springfield was founded in 1890. It is famous for its large donut factory. The mayor is Joe Quimby."
]
vectorstore = Chroma.from_texts(texts, embedding=embeddings)

# Create compressor and contextual compression retriever
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, 
    base_retriever=vectorstore.as_retriever()
)

# The compressor will extract ONLY the relevant sentence about the donut factory
docs = compression_retriever.invoke("What is Springfield famous for?")
for doc in docs:
    print(f"Compressed Output: {doc.page_content}")
