import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain_core.documents import Document

load_dotenv()

docs = [
    Document(page_content="A sci-fi movie about aliens.", metadata={"year": 1980, "rating": 8.5}),
    Document(page_content="A romantic comedy.", metadata={"year": 2023, "rating": 6.2}),
    Document(page_content="An action thriller.", metadata={"year": 1999, "rating": 9.0}),
]

vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())

metadata_field_info = [
    AttributeInfo(name="year", description="The year the movie was released", type="integer"),
    AttributeInfo(name="rating", description="The rating of the movie (1-10)", type="float"),
]

llm = ChatOpenAI(temperature=0)
document_content_description = "Brief description of a movie"

retriever = SelfQueryRetriever.from_llm(
    llm,
    vectorstore,
    document_content_description,
    metadata_field_info,
    verbose=True
)

results = retriever.invoke("What are some movies released after the year 2000?")
for res in results:
    print(res.metadata)
