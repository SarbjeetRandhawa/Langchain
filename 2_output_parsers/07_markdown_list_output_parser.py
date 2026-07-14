from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import MarkdownListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Initialize the parser
output_parser = MarkdownListOutputParser()

# Create a prompt template
prompt = PromptTemplate(
    template="List 3 {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
) 

# Create a chain
chain = prompt | llm | output_parser

# Invoke the chain
result = chain.invoke({"subject": "fastest animals in the world"})

print("Parsed Markdown List Result:")
print(result)
print(f"\nType of result: {type(result)}")
