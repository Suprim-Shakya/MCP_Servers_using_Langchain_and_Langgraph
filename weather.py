from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Fetches the current weather for a given city."""
    # Simulate fetching weather data
    return f"The current weather in {city} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    print("Weather MCP server is running.")