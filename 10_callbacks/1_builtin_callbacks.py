"""
Phase 15: Callbacks - Built-in Callback Handlers

This script demonstrates how to use LangChain's built-in callback handlers,
specifically the StdOutCallbackHandler which logs all events to the console.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.callbacks import StdOutCallbackHandler

load_dotenv()

# 1. Initialize the built-in callback handler
handler = StdOutCallbackHandler()

# 2. Initialize the LLM
# You can pass callbacks directly to the constructor (they will be used for all calls)
llm = ChatOpenAI(model="gpt-3.5-turbo", callbacks=[handler])

prompt = PromptTemplate.from_template("Tell me a short joke about {topic}.")
chain = prompt | llm

if __name__ == "__main__":
    print("Executing chain with StdOutCallbackHandler...")
    
    # You can also pass callbacks at execution time
    # This is useful if you only want to trace a specific run
    response = chain.invoke(
        {"topic": "ice cream"},
        config={"callbacks": [handler]}
    )
    
    print("\\n--- Final Result ---")
    print(response.content)
