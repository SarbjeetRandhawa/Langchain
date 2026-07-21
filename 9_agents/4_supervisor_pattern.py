"""
Phase 14: Agents - Supervisor Pattern (Multi-Agent System)

This script demonstrates a basic multi-agent setup where a 'Supervisor' LLM
evaluates a task and delegates it to specific worker agents (e.g., a Researcher
and a Coder), then synthesizes the final response.
"""

from dotenv import load_dotenv
import operator
from typing import Annotated, Any, Dict, List, Sequence, TypedDict

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import StateGraph, START, END

load_dotenv()

# 1. Define the State
class AgentState(TypedDict):
    # The list of messages in the conversation
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # The next agent to route to
    next: str

# 2. Define the LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# 3. Define the Supervisor Node
# The supervisor decides who should act next, or if we are FINISHED.
members = ["Researcher", "Coder"]
options = ["FINISH"] + members

system_prompt = (
    "You are a supervisor tasked with managing a conversation between the"
    " following workers: {members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH."
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="messages"),
    (
        "system",
        "Given the conversation above, who should act next?"
        " Or should we FINISH? Select one of: {options}",
    ),
]).partial(options=str(options), members=", ".join(members))

# We use tool calling to force the LLM to output exactly one of the options
supervisor_chain = (
    prompt 
    | llm.with_structured_output({"title": "route", "type": "object", "properties": {"next": {"type": "string", "enum": options}}})
)

def supervisor_node(state: AgentState) -> Dict[str, Any]:
    res = supervisor_chain.invoke(state)
    return {"next": res["next"]}

# 4. Define Worker Nodes
def researcher_node(state: AgentState) -> Dict[str, Any]:
    response = llm.invoke([
        {"role": "system", "content": "You are a web researcher. Provide accurate information."}
    ] + state["messages"])
    # We return the response wrapped in a human message so it's added to the message list
    return {"messages": [HumanMessage(content=f"Researcher: {response.content}")]}

def coder_node(state: AgentState) -> Dict[str, Any]:
    response = llm.invoke([
        {"role": "system", "content": "You are an expert Python programmer. Write code based on the research."}
    ] + state["messages"])
    return {"messages": [HumanMessage(content=f"Coder: {response.content}")]}

# 5. Build the Graph
builder = StateGraph(AgentState)

builder.add_node("Supervisor", supervisor_node)
builder.add_node("Researcher", researcher_node)
builder.add_node("Coder", coder_node)

# All workers report back to the supervisor
builder.add_edge("Researcher", "Supervisor")
builder.add_edge("Coder", "Supervisor")

# The supervisor routes based on the 'next' field in the state
builder.add_conditional_edges(
    "Supervisor",
    lambda state: state["next"],
    {
        "Researcher": "Researcher",
        "Coder": "Coder",
        "FINISH": END
    }
)

builder.add_edge(START, "Supervisor")

# Compile the graph
graph = builder.compile()

if __name__ == "__main__":
    print("Running Multi-Agent Supervisor...")
    
    # Run the graph
    for chunk in graph.stream(
        {"messages": [HumanMessage(content="Find out what LangGraph is and write a simple hello world python script for it.")]},
        {"recursion_limit": 10},
    ):
        for node_name, node_output in chunk.items():
            print(f"\\n--- Output from {node_name} ---")
            if "messages" in node_output:
                print(node_output["messages"][-1].content)
            elif "next" in node_output:
                print(f"Routing to: {node_output['next']}")
