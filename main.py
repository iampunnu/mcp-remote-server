from mcp.server.fastmcp import FastMCP
mcp = FastMCP('OS-Tools')
@mcp.tool()
def save_information(name: str, info: str) -> str:
    """
    Save a piece of information for memory.
    DO NOT use this tool for calculations, math, reasoning,
    or any task other than storing text information.
    """
    return f" how are you Saved {name}: {info}"

@mcp.tool()
def add(a: int, b: int) -> int:
        """
        Add two numbers and return their sum.
        Use this tool ONLY for mathematical addition.
        """
        return a + b
