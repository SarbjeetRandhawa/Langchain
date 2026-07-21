"""
Phase 14: Agents - Human-in-the-Loop

This script demonstrates how to add a "Human-in-the-Loop" step to a LangGraph agent.
This allows a human to review the agent's planned tool calls (e.g., executing a dangerous command)
before allowing the agent to proceed.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage

load_dotenv()

@tool
def execute_sql_query(query: str) -> str:
    """Executes a SQL query on the production database."""
    # Simulating a dangerous tool
    print(f"\\n[DANGER] Executing SQL: {query}\\n")
    return "Query executed successfully. 5 rows affected."

tools = [execute_sql_query]

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 1. Initialize a Checkpointer (MemorySaver)
# LangGraph requires a checkpointer to pause and resume the graph's state.
memory = MemorySaver()

# 2. Create the Agent with an Interrupt
# We tell the graph to interrupt execution *before* calling any tools.
agent_executor = create_react_agent(
    llm, 
    tools, 
    checkpointer=memory,
    interrupt_before=["tools"] # Pause before the 'tools' node executes
)

if __name__ == "__main__":
    # We must provide a thread_id when using a checkpointer
    config = {"configurable": {"thread_id": "thread-1"}}
    
    print("User: Please drop the users table.")
    inputs = {"messages": [HumanMessage(content="Please drop the users table.")]}
    
    # 3. Run the agent until the breakpoint
    print("\\n--- Agent is thinking... ---")
    for chunk in agent_executor.stream(inputs, config=config, stream_mode="values"):
        if "messages" in chunk and chunk["messages"]:
            chunk["messages"][-1].pretty_print()
            
    # 4. Check if the graph is paused
    state = agent_executor.get_state(config)
    
    if state.next:
        print("\\n[System] The agent wants to execute a tool. Execution is paused.")
        print(f"Pending tasks: {state.next}")
        
        # In a real app, you would show this to the user in a UI and ask for approval
        user_input = input("\\nDo you approve this action? (yes/no): ")
        
        if user_input.lower() == "yes":
            print("\\n[System] Action approved. Resuming execution...")
            # To resume, we just call stream/invoke again with None as input
            for chunk in agent_executor.stream(None, config=config, stream_mode="values"):
                chunk["messages"][-1].pretty_print()
        else:
            print("\\n[System] Action denied. We must manually update the state to cancel.")
            # Note: Cancelling a tool call in LangGraph involves updating the state 
            # to provide an artificial response from the tool, simulating a rejection.
            # For simplicity, we just stop execution here.
    else:
        print("\\n[System] Execution finished without needing approval.")
