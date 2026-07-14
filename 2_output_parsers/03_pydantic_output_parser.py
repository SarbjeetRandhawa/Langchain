from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

# Define the Pydantic model for the output
class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(description="The age of the person")
    city: str = Field(description="The city where the person lives")

# Initialize the parser
parser = PydanticOutputParser(pydantic_object=Person)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Extract the person's information from the text.
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
        "text": "John Doe is a 30 year old software engineer living in New York.",
        "format_instructions": parser.get_format_instructions()
    }
)

print("Parsed Result:")
print(result)
print(f"\nType of result: {type(result)}")
