"""
Phase 13: Tools - Tool Errors & Validation
This script demonstrates how to handle errors gracefully when tools fail,
including input validation, custom exceptions, and using LangChain's built-in
error handling features (e.g., ToolException) so the agent can recover.
"""

from langchain_core.tools import tool, StructuredTool, ToolException
from pydantic import BaseModel, Field, field_validator

# ---------------------------------------------------------
# 1. Input Validation with Pydantic
# ---------------------------------------------------------
# Validating inputs before executing the tool logic is critical.
# We can use Pydantic validators to ensure the LLM passes correct data.

class CalculatorSchema(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")
    operation: str = Field(description="Math operation to perform ('add' or 'divide')")

    @field_validator("operation")
    def validate_operation(cls, v):
        if v not in ["add", "divide"]:
            raise ValueError("Operation must be either 'add' or 'divide'")
        return v

def safe_calculator(a: int, b: int, operation: str) -> str:
    """A safe calculator that performs basic operations."""
    if operation == "add":
        return str(a + b)
    elif operation == "divide":
        # We handle runtime errors explicitly
        if b == 0:
            raise ToolException("Cannot divide by zero. Please provide a non-zero denominator.")
        return str(a / b)
    return "Unknown operation"

# ---------------------------------------------------------
# 2. Handling Tool Errors Gracefully
# ---------------------------------------------------------
# If a tool throws a standard exception (like ValueError or ZeroDivisionError), 
# the agent execution will crash.
# By setting `handle_tool_error=True` and raising `ToolException`,
# we can return the error message back to the LLM so it can correct its mistake!

calculator_tool = StructuredTool.from_function(
    func=safe_calculator,
    name="Safe_Calculator",
    description="Useful for performing addition or division safely.",
    args_schema=CalculatorSchema,
    handle_tool_error=True, # <--- CRITICAL: Sends ToolException message to the LLM instead of crashing
)

# ---------------------------------------------------------
# 3. Custom Error Handlers
# ---------------------------------------------------------
# You can also pass a custom function to `handle_tool_error` to standardize
# how error messages are formatted for the LLM.

def custom_error_handler(error: ToolException) -> str:
    return f"The tool execution failed with error: {error.args[0]}\nPlease try again with different inputs."

calculator_tool_custom = StructuredTool.from_function(
    func=safe_calculator,
    name="Safe_Calculator_Custom",
    description="Useful for performing addition or division safely.",
    args_schema=CalculatorSchema,
    handle_tool_error=custom_error_handler,
)

# ---------------------------------------------------------
# Example Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    print("--- 1. Testing Input Validation Error ---")
    try:
        # LLM tries to send a wrong operation
        calculator_tool.invoke({"a": 10, "b": 5, "operation": "multiply"})
    except Exception as e:
        print(f"Pydantic Validation Error Caught:\n{e}\n")

    print("--- 2. Testing Runtime Error with handle_tool_error=True ---")
    # LLM tries to divide by zero. Because handle_tool_error=True, 
    # it won't crash the script; it returns the error string to the LLM.
    result = calculator_tool.invoke({"a": 10, "b": 0, "operation": "divide"})
    print(f"Tool Output returned to LLM: '{result}'\n")

    print("--- 3. Testing Custom Error Handler ---")
    result_custom = calculator_tool_custom.invoke({"a": 10, "b": 0, "operation": "divide"})
    print(f"Tool Output returned to LLM: '{result_custom}'\n")
