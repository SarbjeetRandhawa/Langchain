"""
Phase 13: Tools - Toolkits
This script demonstrates the concept of Toolkits in LangChain.

A Toolkit is a collection of tools that are designed to be used together
to accomplish a specific task. Instead of writing custom tools for everything,
you can use pre-built toolkits to instantly give your agent a suite of capabilities.

Common Toolkits include:
- SQLDatabaseToolkit (for querying SQL databases)
- FileManagementToolkit (for interacting with the local file system)
- GitHubToolkit (for managing repositories and issues)
- GmailToolkit (for reading and sending emails)
"""

from langchain_community.agent_toolkits import FileManagementToolkit
import os

# ---------------------------------------------------------
# 1. Setting up a Toolkit (FileManagementToolkit Example)
# ---------------------------------------------------------
# We will use the FileManagementToolkit as it doesn't require API keys.
# It gives an agent the ability to read, write, copy, and list files.

# Create a temporary directory for the agent to work in safely
working_directory = "./agent_workspace"
os.makedirs(working_directory, exist_ok=True)

# Initialize the toolkit.
# You can restrict which tools are enabled to prevent the agent from doing dangerous things.
file_toolkit = FileManagementToolkit(
    root_dir=working_directory,
    selected_tools=["read_file", "write_file", "list_directory", "copy_file"]
)

# ---------------------------------------------------------
# 2. Extracting Tools from a Toolkit
# ---------------------------------------------------------
# You don't pass the Toolkit object itself to the agent.
# Instead, you extract the list of tools from it using `.get_tools()`.

tools = file_toolkit.get_tools()

# ---------------------------------------------------------
# 3. Using Toolkits with LCEL (LangChain Expression Language)
# ---------------------------------------------------------
# In modern LangChain, you bind the extracted tools directly to a 
# Chat Model using LCEL.

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

# Dummy key to prevent initialization crash if not set
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "dummy-key"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Bind the tools to the LLM
llm_with_tools = llm.bind_tools(tools)

# Create a standard LCEL prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to a file system. Use your tools to manage files."),
    ("human", "{input}")
])

# Build the LCEL Chain
lcel_chain = prompt | llm_with_tools

# ---------------------------------------------------------
# Example Output
# ---------------------------------------------------------
if __name__ == "__main__":
    print(f"Number of tools in the File Management Toolkit: {len(tools)}\n")
    
    print("Available Tools in this Toolkit:")
    print("=" * 60)
    for tool in tools:
        print(f"Tool Name: {tool.name}")
        # The description is what the LLM reads to know when to use the tool
        print(f"Description: {tool.description.splitlines()[0]}") 
        print("-" * 60)
        
    print("\nHow it works in LCEL:")
    print("1. We extracted the tools: `tools = file_toolkit.get_tools()`")
    print("2. We bound them to the LLM: `llm_with_tools = llm.bind_tools(tools)`")
    print("3. We built the chain: `lcel_chain = prompt | llm_with_tools`")
    print("\nIf you invoke this chain (requires valid OpenAI key), the LLM will output 'tool_calls' instead of raw text!")
