from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# RunnableLambda allows you to wrap custom python functions into your LCEL chains.

def uppercase_formatter(text: str) -> str:
    """A simple custom function to manipulate text."""
    print(f"--- Running custom lambda function ---")
    return text.upper()

# Wrap the function in a RunnableLambda
uppercase_runnable = RunnableLambda(uppercase_formatter)

prompt = ChatPromptTemplate.from_template("Write a one sentence summary of {topic}")
model = ChatGroq(model="llama-3.3-70b-versatile")
output_parser = StrOutputParser()

# Add the custom runnable to the chain
chain = prompt | model | output_parser | uppercase_runnable

response = chain.invoke({"topic": "artificial intelligence"})
print(response)
