"""
Phase 13: Tools - Custom Tools
This script demonstrates how to create:
1. Simple custom tools using the @tool decorator.
2. Structured custom tools with multiple parameters using Pydantic and StructuredTool.
"""

from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field

# ---------------------------------------------------------
# 1. Simple Custom Tool using the @tool decorator
# ---------------------------------------------------------
# The @tool decorator is the easiest way to define a custom tool.
# The docstring of the function is automatically used as the tool's description,
# which is critical for the LLM to understand when to use it.

@tool
def get_current_temperature(location: str) -> str:
    """
    Get the current temperature for a given location.
    
    Args:
        location (str): The city or location (e.g., "San Francisco", "New York").
        
    Returns:
        str: The current temperature as a string.
    """
    # In a real app, you would make an API call (e.g., to OpenWeatherMap) here.
    # We'll use mocked data for demonstration.
    mocked_data = {
        "San Francisco": "15°C",
        "New York": "22°C",
        "London": "12°C"
    }
    
    temp = mocked_data.get(location, "Temperature data not available.")
    return f"The current temperature in {location} is {temp}."

# ---------------------------------------------------------
# 2. Structured Custom Tool using Pydantic
# ---------------------------------------------------------
# When a tool requires complex or multiple inputs, it's best to define 
# the input schema explicitly using Pydantic. This ensures the LLM
# strictly adheres to the expected argument types and structures.

class FlightSearchSchema(BaseModel):
    """Schema for the Flight Search Tool."""
    origin: str = Field(description="The airport code for the departure city (e.g., 'JFK').")
    destination: str = Field(description="The airport code for the arrival city (e.g., 'SFO').")
    date: str = Field(description="The date of departure in YYYY-MM-DD format.")
    passengers: int = Field(default=1, description="Number of passengers.")

def search_flights(origin: str, destination: str, date: str, passengers: int) -> str:
    """Search for available flights based on user criteria."""
    
    # In a real application, you'd call a flight search API here.
    return (f"Found 3 flights from {origin} to {destination} on {date} "
            f"for {passengers} passenger(s). Prices start at $299.")

# We create the tool by binding the function and its Pydantic schema
flight_search_tool = StructuredTool.from_function(
    func=search_flights,
    name="Flight_Search",
    description="Use this tool to search for flights between two cities.",
    args_schema=FlightSearchSchema,
)

# ---------------------------------------------------------
# Example Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    print("--- Testing Simple @tool ---")
    print(f"Tool Name: {get_current_temperature.name}")
    print(f"Tool Description: {get_current_temperature.description}")
    
    # Execute the tool
    response_1 = get_current_temperature.invoke({"location": "New York"})
    print(f"Result: {response_1}")
    
    print("\n--- Testing StructuredTool ---")
    print(f"Tool Name: {flight_search_tool.name}")
    print(f"Tool Description: {flight_search_tool.description}")
    
    # Execute the structured tool
    response_2 = flight_search_tool.invoke({
        "origin": "JFK",
        "destination": "LHR",
        "date": "2024-12-25",
        "passengers": 2
    })
    print(f"Result: {response_2}")
