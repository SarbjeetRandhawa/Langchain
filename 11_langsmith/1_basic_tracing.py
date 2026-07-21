"""
Phase 16: LangSmith & Production - Basic Tracing

This script demonstrates how to enable LangSmith tracing.
LangSmith provides unparalleled visibility into exactly what is happening
inside your chains and agents (prompts, token usage, latency, etc.).
"""

from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Note: For LangSmith to work, you MUST have the following environment variables set:
# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_API_KEY=<your_langsmith_api_key>
# LANGCHAIN_PROJECT=<your_project_name> (optional, defaults to "default")
load_dotenv()

# We explicitly check if tracing is enabled
if os.environ.get("LANGCHAIN_TRACING_V2") != "true":
    print("WARNING: LANGCHAIN_TRACING_V2 is not set to 'true' in your environment.")
    print("LangSmith tracing will NOT be active.")
    print("Ensure you have a .env file with LANGCHAIN_TRACING_V2 and LANGCHAIN_API_KEY.")

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create a simple chain
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert on coffee. Answer concisely."),
    ("human", "What is the difference between {coffee1} and {coffee2}?")
])

chain = prompt | llm

if __name__ == "__main__":
    print("Invoking the chain. If environment variables are set, this run will be traced in LangSmith.")
    
    # When this runs, LangChain automatically sends a trace to LangSmith in the background
    response = chain.invoke({
        "coffee1": "an Americano",
        "coffee2": "a Drip Coffee"
    })
    
    print("\\nResponse:")
    print(response.content)
    print("\\nCheck your LangSmith dashboard at https://smith.langchain.com/ to view the trace!")
