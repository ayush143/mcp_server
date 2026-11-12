from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama 
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathServer.py"],
                "transport": "stdio"
            },
            "weather": {
               "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            }
        }
    )
    
    tools = await client.get_tools()
    
    model = ChatOllama(
        model="qwen3:latest", 
        base_url="http://localhost:11434"
    )
    
    agent = create_react_agent(
        model, tools
    )
    
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "whats(3+2)*12 ?"}]}
    )
    print("math_response", math_response['messages'][-1].content)
    
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in california ?"}]} # Fixed spelling
    )
   
    print("weather_response", weather_response['messages'][-1].content)
    
asyncio.run(main())