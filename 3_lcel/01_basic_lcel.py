from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# 1. Create a prompt template
prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")

# 2. Initialize a model (Replace with your preferred model)
model = ChatGroq(model="llama-3.3-70b-versatile")

# 3. Create an output parser
output_parser = StrOutputParser()

# 4. Chain them together using LCEL (the | operator)
chain = prompt | model | output_parser

# 5. Invoke the chain
response = chain.invoke({"topic": "programming"})
print(response)
