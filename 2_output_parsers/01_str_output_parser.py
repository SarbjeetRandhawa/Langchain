from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_messages(
[
    ("system","You are helpful."),
    ("human","{question}")
]
)

parser = StrOutputParser()


chain = prompt | llm | parser

result = chain.invoke(
{
    "question":"How to build a cpu chip?"
})

print(result)