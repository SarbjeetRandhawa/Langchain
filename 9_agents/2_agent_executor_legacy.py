"""
Phase 14: Agents - AgentExecutor (Legacy)

This script demonstrates the legacy AgentExecutor, which is heavily reliant
on LangChain's built-in memory and tools handling before the transition to LangGraph.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a specific location."""
    # In a real app, this would call an API
    if "seattle" in location.lower():
        return "It is currently raining and 50 degrees in Seattle."
    return f"It is sunny and 75 degrees in {location}."

tools = [get_weather]

# Initialize LLM with tool calling capabilities
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create a prompt for the agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use tools when necessary."),
    ("human", "{input}"),
    # This placeholder is where the agent scratchpad will be injected
    ("placeholder", "{agent_scratchpad}"),
])

# Create the agent
# Note: create_tool_calling_agent uses OpenAI's native tool calling instead of ReAct prompting
agent = create_tool_calling_agent(llm, tools, prompt)

# Create the executor (Legacy approach)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True # Good practice for legacy executors
)

if __name__ == "__main__":
    print("Testing the legacy AgentExecutor...")
    
    response = agent_executor.invoke({
        "input": "What is the weather like in Seattle and in Miami?"
    })
    
    print("\nFinal Answer:")
    print(response["output"])
