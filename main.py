import os
os.environ["FASTMCP_NO_AUTORUN"] = "1"

from mcp.server.fastmcp import FastMCP

mcp = FastMCP('OS-Tools')

@mcp.tool()
def save_information(name: str, info: str) -> str:
    return f"Saved {name}: {info}"

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


# Important: prevent auto-run
if __name__ == "__main__":
    pass
