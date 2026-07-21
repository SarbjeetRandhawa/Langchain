"""
Phase 17: MCP (Model Context Protocol) - Server

This script demonstrates how to create a basic MCP server.
MCP (Model Context Protocol) standardizes how AI applications communicate 
with external data sources and tools.

To run this server, you would typically use an MCP client or the MCP CLI.
"""

# Note: Requires `pip install mcp`
import sys
from mcp.server.fastmcp import FastMCP

# 1. Initialize the FastMCP server
# FastMCP is a high-level API for creating MCP servers in Python (similar to FastAPI)
mcp = FastMCP("Math Server")

# 2. Expose Tools to the AI
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    return a - b

# 3. Expose Resources (Data) to the AI
# Resources represent read-only data that the AI can fetch
@mcp.resource("config://app-settings")
def get_settings() -> str:
    """Get the current application settings."""
    return '{"theme": "dark", "version": "1.0.0"}'

if __name__ == "__main__":
    print("Starting MCP Math Server on stdio transport...")
    print("This server expects to communicate over stdin/stdout using the MCP protocol.")
    
    # 4. Run the server
    # By default, FastMCP runs on stdio, which is perfect for local AI agent integration
    mcp.run(transport='stdio')
