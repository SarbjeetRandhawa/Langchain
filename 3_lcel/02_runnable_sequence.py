from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# RunnableSequence is what gets created under the hood when you use the | operator.
# You can also create one explicitly.

prompt = ChatPromptTemplate.from_template("What is a good name for a company that makes {product}?")
model = ChatGroq(model="llama-3.3-70b-versatile")
output_parser = StrOutputParser()

# Explicitly defining a RunnableSequence
chain = RunnableSequence(
    first=prompt,
    middle=[model],
    last=output_parser
)

# This is exactly equivalent to: chain = prompt | model | output_parser

response = chain.invoke({"product": "eco-friendly water bottles"})
print(response)
