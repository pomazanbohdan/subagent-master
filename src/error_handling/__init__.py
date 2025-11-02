"""
Error Handling Module

Error classification, delegation, and recovery mechanisms.
"""

from .classification import classify_error
from .delegation import delegate_error_handling
from .recovery import attempt_recovery

__all__ = [
    'classify_error',
    'delegate_error_handling', 
    'attempt_recovery'
]