from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()


parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"""
Extract information. and explain each term in detail.
{format_instructions}
"""
),
(
 "human",
 "{text}"
)
]
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

chain = prompt | llm | parser

result = chain.invoke(
{
"text":"apple banana car truck grass vine ladyfinger carrot",

"format_instructions":
parser.get_format_instructions()
})

print(result) 