"""
Phase 14: Agents - create_react_agent

This script demonstrates how to create a basic ReAct agent using the 
langchain.agents.create_react_agent function.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import tool
from langchain import hub

load_dotenv()

# 1. Define Tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers together."""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Add two integers together."""
    return a + b

tools = [multiply, add]

# 2. Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 3. Pull a standard ReAct prompt from LangChain Hub
# This prompt tells the LLM to output its Thought, Action, and Action Input.
prompt = hub.pull("hwchase17/react")

# 4. Create the Agent
# This binds the LLM, the tools, and the prompt together to form the routing logic.
agent = create_react_agent(llm, tools, prompt)

# 5. Create the AgentExecutor
# The executor handles the while-loop of calling the agent, parsing the output, and executing tools.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    print("Asking the agent to perform a math problem...")
    
    # Run the agent
    response = agent_executor.invoke({
        "input": "What is 3 multiplied by 12, and then that result added to 10?"
    })
    
    print("\nFinal Answer:")
    print(response["output"])
