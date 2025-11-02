"""
Enhanced Task Distribution Module
Intelligent distribution between agents and MCP tools based on task complexity.
"""

from .enhanced_distribution import (
    enhanced_task_distribution,
    execute_task_with_best_agent,
    execute_with_task_delegation,
    analyze_task_complexity,
    validate_agent_availability,
    track_progress,
    wait_for_parallel_completion,
    handle_partial_parallel_failure,
    synchronize_parallel_results,
    resolve_conflicts,
    synthesize_results,
    comprehensive_user_reporting
)

__all__ = [
    'enhanced_task_distribution',
    'execute_task_with_best_agent',
    'execute_with_task_delegation',
    'analyze_task_complexity',
    'validate_agent_availability',
    'track_progress',
    'wait_for_parallel_completion',
    'handle_partial_parallel_failure',
    'synchronize_parallel_results',
    'resolve_conflicts',
    'synthesize_results',
    'comprehensive_user_reporting'
]