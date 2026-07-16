import os
import uuid
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import InMemoryStore
from langchain_core.documents import Document

load_dotenv()

vectorstore = Chroma(collection_name="summaries", embedding_function=OpenAIEmbeddings())
store = InMemoryStore()

retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    docstore=store,
    id_key="doc_id"
)

doc_id = str(uuid.uuid4())
parent_doc = Document(page_content="This is the full text of a long document about LangChain.", metadata={"doc_id": doc_id})

sub_docs = [
    Document(page_content="Summary: LangChain is a framework for LLMs.", metadata={"doc_id": doc_id}),
    Document(page_content="Keywords: LangChain, LLM, Framework.", metadata={"doc_id": doc_id}),
]

retriever.docstore.mset([(doc_id, parent_doc)])
retriever.vectorstore.add_documents(sub_docs)

results = retriever.invoke("Summary about LangChain")
print("Retrieved Parent Document:", results[0].page_content)
