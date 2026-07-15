from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# RunnableParallel (also sometimes called a RunnableMap) allows you to run multiple Runnables 
# in parallel and returns their outputs as a dictionary.

model = ChatGroq(model="llama-3.3-70b-versatile")
output_parser = StrOutputParser()

# Create two different prompts
joke_prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
poem_prompt = ChatPromptTemplate.from_template("Write a short poem about {topic}")

# Create two separate chains
joke_chain = joke_prompt | model | output_parser
poem_chain = poem_prompt | model | output_parser

# Combine them using RunnableParallel
# This will execute both chains at the same time!
map_chain = RunnableParallel(
    joke=joke_chain,
    poem=poem_chain
)

response = map_chain.invoke({"topic": "cats"})

print("--- Joke ---")
print(response["joke"])
print("\n--- Poem ---")
print(response["poem"])
