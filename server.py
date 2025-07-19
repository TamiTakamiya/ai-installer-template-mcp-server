# server.py
from enum import Enum
from fastmcp import FastMCP

class Platform(Enum):
    CONTAINER: "container"
    RPM: "rpm"

class Topology(Enum):
    GROWTH: "growth"
    ENTERPRISE: "enterprise"

mcp = FastMCP("AI Installer Template MCP Server")

@mcp.tool
def get_template(platform: Platform, topology: Topology, session_id: str) -> str:
    """Get a template for AAP Installer for given platform and topology"""
    return f"platform={platform} topology={topology} session_id={session_id}"

if __name__ == "__main__":
    mcp.run()