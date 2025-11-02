"""
Parallel Execution Module

Parallel coordination, synchronization, and competitive execution algorithms.
"""

from .coordination import execute_parallel_tasks_with_coordination
from .synchronization import synchronize_parallel_results

__all__ = [
    'execute_parallel_tasks_with_coordination',
    'synchronize_parallel_results'
]