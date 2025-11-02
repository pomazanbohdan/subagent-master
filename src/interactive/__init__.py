"""
Interactive Clarification Module
Context-aware clarification system with adaptive question generation.
"""

from .clarification import (
    determine_need_for_clarification,
    generate_contextual_questions,
    process_user_responses,
    refine_task_understanding
)

__all__ = [
    'determine_need_for_clarification',
    'generate_contextual_questions',
    'process_user_responses',
    'refine_task_understanding'
]