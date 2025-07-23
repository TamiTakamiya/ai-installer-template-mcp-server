# server.py
import importlib.resources
from fastmcp import FastMCP
from aap_inventory_tool import generate_command

mcp = FastMCP("AI Installer Template MCP Server")

@mcp.tool
def get_template(platform: str, topology: str, session_id: str) -> str:
    """Get a template for AAP Installer for given platform and topology"""
    with importlib.resources.open_text("ai_installer_template.data", f'{platform}_{topology}_template.txt') as f:
        content = f.read()
    return content

@mcp.tool
def get_inventory(platform: str, topology: str, host: str, session_id: str) -> str:
    """Get an inventory for AAP Installer for given platform and topology"""
    class Args:
        platform: str
        topology: str
        host: str

    args = Args()
    args.platform = platform
    args.topology = topology
    args.host = host
    print(f"platform:{platform} topology:{topology} session_id:{session_id}")

    return generate_command(args)

if __name__ == "__main__":
    mcp.run(transport="http")
