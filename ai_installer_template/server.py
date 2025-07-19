# server.py
import importlib.resources
from fastmcp import FastMCP
mcp = FastMCP("AI Installer Template MCP Server")

@mcp.tool
def get_template(platform: str, topology: str, session_id: str) -> str:
    """Get a template for AAP Installer for given platform and topology"""
    with importlib.resources.open_text("ai_installer_template.data", f'{platform}_{topology}_template.txt') as f:
        content = f.read()
    return content

if __name__ == "__main__":
    mcp.run(transport="http")
