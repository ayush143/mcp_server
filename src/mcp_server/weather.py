from mcp.server.fastmcp import FastMCP

mcp=FastMCP('weather')

@mcp.tool()
async def get_weather(location:str)->str:
    """_summary_
    Get weather information for a given location
    """
    return "its always sunny in philadelphia"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
    