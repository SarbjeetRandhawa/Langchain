"""
Phase 15: Callbacks - Tracking Token Usage & Cost

This script demonstrates how to use the get_openai_callback context manager
to easily track token usage and approximate costs for OpenAI models.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

if __name__ == "__main__":
    print("Executing LLM calls inside the token tracking context...")
    
    # Use the context manager to track everything inside the block
    with get_openai_callback() as cb:
        # First call
        response1 = llm.invoke("What is the capital of France?")
        print(f"Response 1: {response1.content}")
        
        # Second call
        response2 = llm.invoke("What is the capital of Japan?")
        print(f"Response 2: {response2.content}")
        
    print("\\n--- Token Usage Report ---")
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost:.6f}")
