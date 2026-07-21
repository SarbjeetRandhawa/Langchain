"""
Phase 17: MCP (Model Context Protocol) - LangChain Client

This script demonstrates how an AI application (like a LangChain Agent) 
can connect to an MCP server to dynamically discover and use its tools.

Note: In a real-world scenario, you would run the MCP server (1_mcp_server.py)
as a separate process.
"""

from dotenv import load_dotenv
import asyncio
import sys
from contextlib import AsyncExitStack

# Note: Requires `pip install mcp langchain-mcp-adapters`
try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    # LangChain adapter to convert MCP tools into LangChain tools
    from langchain_mcp_adapters.tools import load_mcp_tools
except ImportError:
    print("Please install required packages: pip install mcp langchain-mcp-adapters")
    sys.exit(1)

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

load_dotenv()

async def run_mcp_agent():
    # 1. Define how to connect to the MCP server
    # We will start the python script 1_mcp_server.py as a subprocess
    server_params = StdioServerParameters(
        command="python",
        args=["1_mcp_server.py"],
        env=None
    )
    
    print("Connecting to MCP Server...")
    
    # 2. Establish connection and session
    async with AsyncExitStack() as stack:
        # Start the subprocess
        stdio_transport = await stack.enter_async_context(stdio_client(server_params))
        read, write = stdio_transport
        
        # Initialize the MCP session
        session = await stack.enter_async_context(ClientSession(read, write))
        await session.initialize()
        print("Connected successfully!")
        
        # 3. Discover capabilities (Tools)
        # The client asks the server: "What tools do you have?"
        print("Discovering tools from the MCP server...")
        
        # We use the LangChain adapter to automatically fetch and convert the MCP tools
        # into LangChain @tool formatted functions!
        langchain_tools = await load_mcp_tools(session)
        
        print(f"Found {len(langchain_tools)} tools: {[t.name for t in langchain_tools]}")
        
        # 4. Create an Agent with the dynamically loaded tools
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        agent = create_react_agent(llm, langchain_tools)
        
        print("\\nAsking the agent to perform a math problem using the remote MCP tools...")
        inputs = {"messages": [HumanMessage(content="What is 452 added to 129?")]}
        
        # Run the agent
        async for chunk in agent.astream(inputs, stream_mode="values"):
            chunk["messages"][-1].pretty_print()

if __name__ == "__main__":
    # We run the async client
    asyncio.run(run_mcp_agent())
