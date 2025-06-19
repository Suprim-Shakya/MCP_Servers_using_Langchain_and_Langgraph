# Create a client that connects to both the Weather and Math MCP servers

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq


from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "Math": {
                "command": "python",
                "args": ["mathserver.py"],  # Path to the math server script
                "transport": "stdio",
            },
            "Weather": {
                "url": "http://localhost:8000/mcp",  # Assuming the weather server runs on this URL
                "transport": "streamable_http",
            },
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(
        model = "qwen-qwq-32b")
    agent = create_react_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (9 + 13) * 12?"}]}
    )

    print(f"Math Response: {math_response['messages'][-1].content}")
    
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather in Kathmandu?"}]}
    )
    
    print(f"Weather Response: {weather_response['messages'][-1].content}")

    

asyncio.run(main())
# This client connects to both the Math and Weather MCP servers, allowing you to query them.