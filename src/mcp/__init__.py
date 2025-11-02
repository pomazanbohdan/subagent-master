"""
MCP Tools Integration Module
Intelligent MCP tool selection and execution for small tasks.
"""

from .intelligent_tools import (
    is_mcp_task,
    intelligent_mcp_tool_selection,
    execute_mcp_tool_chain,
    execute_with_mcp_tools,
    synthesize_mcp_results
)

__all__ = [
    'is_mcp_task',
    'intelligent_mcp_tool_selection',
    'execute_mcp_tool_chain',
    'execute_with_mcp_tools',
    'synthesize_mcp_results'
]