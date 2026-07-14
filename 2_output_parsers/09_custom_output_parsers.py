from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Create a custom output parser that inherits from BaseOutputParser
# It takes the string response from the LLM and transforms it
class UppercaseOutputParser(BaseOutputParser[str]):
    """Parse the output of an LLM call to a completely uppercase string."""
    
    def parse(self, text: str) -> str:
        """Parse the output of an LLM call."""
        # Custom logic: strip whitespace and convert to ALL CAPS
        return text.strip().upper()

# Initialize the custom parser
output_parser = UppercaseOutputParser()

prompt = PromptTemplate.from_template(
    "Tell me a short one-liner joke about {subject}."
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

chain = prompt | llm | output_parser

result = chain.invoke({"subject": "programmers"})

print("Custom Uppercase Parser Result:")
print(result)
print(f"\nType: {type(result)}")
