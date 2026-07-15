from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# RunnablePassthrough allows you to pass inputs through unchanged or add additional keys to the input.
# It is very common when you need to pass an initial input through multiple steps without losing it.

prompt = ChatPromptTemplate.from_template("Write a funny tweet about {topic}")
model = ChatGroq(model="llama-3.3-70b-versatile")
output_parser = StrOutputParser()

# In this chain, RunnablePassthrough takes the raw input string and formats it into a dictionary 
# with the key "topic".
chain = {"topic": RunnablePassthrough()} | prompt | model | output_parser

# Notice we invoke it with just a string, not a dictionary!
response = chain.invoke("coffee")
print(response)
