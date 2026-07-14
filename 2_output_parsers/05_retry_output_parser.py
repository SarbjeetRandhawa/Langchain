from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import RetryOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

# Define our expected output structure using Pydantic
class Action(BaseModel):
    action: str = Field(description="The action to take")
    action_input: str = Field(description="The input to the action")

# Initialize base parser
parser = PydanticOutputParser(pydantic_object=Action)

# Define the original prompt template that the LLM was responding to
prompt_template = PromptTemplate(
    template="Answer the user query by outputting an action.\n{format_instructions}\nUser Query: {query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Simulate a malformed response from the LLM (e.g., it missed the required 'action_input' field)
malformed_response = '{"action": "search"}' 

print("--- Base parser fails on malformed response ---")
try:
    parser.parse(malformed_response)
except Exception as e:
    print(f"Failed to parse! Error:\n{e}\n")

# Initialize the LLM that will be used to retry and fix the output
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Initialize the RetryOutputParser
retry_parser = RetryOutputParser.from_llm(parser=parser, llm=llm)

print("--- RetryOutputParser fixes it using the original prompt context ---")
# We recreate the exact prompt value that was passed to the LLM originally
prompt_value = prompt_template.format_prompt(query="Search for Leonardo DiCaprio's girlfriend")

# The retry parser takes both the broken output AND the original prompt value
# giving the LLM much more context on what it was originally asked to do!
fixed_result = retry_parser.parse_with_prompt(malformed_response, prompt_value)

print("Successfully fixed and parsed Result:")
print(fixed_result)
print(f"\nType of result: {type(fixed_result)}")
