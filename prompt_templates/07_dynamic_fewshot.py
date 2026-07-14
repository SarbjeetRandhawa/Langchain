from langchain_core.example_selectors.base import BaseExampleSelector
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from typing import Dict, List

# 1. Define a pool of examples
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
    {"input": "3+4", "output": "7"},
    {"input": "What is the capital of France?", "output": "Paris"},
    {"input": "Who wrote Hamlet?", "output": "Shakespeare"},
]

# 2. Create a custom example selector
class CustomExampleSelector(BaseExampleSelector):
    def __init__(self, examples: List[Dict[str, str]]):
        self.examples = examples
    
    def add_example(self, example: Dict[str, str]) -> None:
        self.examples.append(example)
        
    def select_examples(self, input_variables: Dict[str, str]) -> List[Dict[str, str]]:
        # This is a dynamic selection logic.
        # In a real scenario, this is where you'd use Semantic Similarity via Vector Databases!
        query = input_variables.get("question", "").lower()
        
        # If the query contains math symbols, return math examples
        if any(math_symbol in query for math_symbol in ["+", "-", "*", "/", "math"]):
            return self.examples[:3] 
        
        # Otherwise, return general knowledge examples
        return self.examples[3:]

# Initialize our selector
example_selector = CustomExampleSelector(examples)

# 3. Define how each example should be formatted
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}")
])

# 4. Create the dynamic few-shot prompt using the example selector
dynamic_few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    example_selector=example_selector,
)

# 5. Assemble the final prompt
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    dynamic_few_shot_prompt,
    ("human", "{question}")
])

print("--- Example 1: Math Query ---")
math_query_prompt = final_prompt.invoke({"question": "What is 10+10?"})
print(math_query_prompt.to_string())

print("\n" + "="*40 + "\n")

print("--- Example 2: General Knowledge Query ---")
general_query_prompt = final_prompt.invoke({"question": "What is the capital of Spain?"})
print(general_query_prompt.to_string())
