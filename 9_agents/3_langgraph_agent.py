"""
Phase 14: Agents - LangGraph Agents (Modern Approach)

This script demonstrates how to build an agent using LangGraph, 
which is the recommended modern approach replacing AgentExecutor.
It provides much finer-grained control over the agent's state and execution.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

load_dotenv()

# 1. Define Tools
@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

tools = [get_word_length]

# 2. Initialize LLM
# Note: Ensure you use a model that supports native tool calling (e.g., gpt-3.5-turbo, gpt-4)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 3. Create the LangGraph Agent
# The `create_react_agent` from langgraph.prebuilt automatically constructs 
# a StateGraph that manages the reasoning loop and tool execution.
agent_executor = create_react_agent(llm, tools)

if __name__ == "__main__":
    print("Testing the LangGraph Agent...")
    
    # We pass the input as a list of messages (the state expects a 'messages' key)
    inputs = {"messages": [HumanMessage(content="What is the length of the word 'supercalifragilisticexpialidocious'?")]}
    
    # Run the graph
    for chunk in agent_executor.stream(inputs, stream_mode="values"):
        message = chunk["messages"][-1]
        message.pretty_print()
