import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

load_dotenv()

vectorstore = Chroma(collection_name="split_parents", embedding_function=OpenAIEmbeddings())
store = InMemoryStore()

child_splitter = RecursiveCharacterTextSplitter(chunk_size=100)

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
)

docs = [Document(page_content="This is a very long document. " * 20)]

retriever.add_documents(docs)
retrieved_docs = retriever.invoke("very long document")
print(f"Retrieved Document length: {len(retrieved_docs[0].page_content)}")
