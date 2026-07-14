from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

# Define the Pydantic model for the expected output
class Actor(BaseModel):
    name: str = Field(description="name of an actor")
    film_names: list[str] = Field(description="list of names of films they starred in")

# Initialize the base parser
parser = PydanticOutputParser(pydantic_object=Actor)

# A deliberately malformed JSON string (e.g., using single quotes instead of double quotes, missing closing brackets)
malformed_output = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump', 'Cast Away'"

print("--- Attempting to parse with base PydanticOutputParser ---")
try:
    parser.parse(malformed_output)
except Exception as e:
    print(f"Failed to parse! Error:\n{e}\n")

# Initialize the LLM to use for fixing the output
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Initialize the OutputFixingParser, passing the original parser and the LLM
fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=llm)

print("--- Attempting to parse with OutputFixingParser ---")
# The fixing parser will try the base parser first. If it fails, it sends the malformed text and instructions to the LLM to fix.
fixed_result = fixing_parser.parse(malformed_output)

print("Successfully fixed and parsed Result:")
print(fixed_result)
print(f"\nType of result: {type(fixed_result)}")

