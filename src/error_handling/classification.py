"""
Error Classification System

Error classification and categorization for intelligent error handling.
"""

from typing import Dict, List, Any, Optional
from enum import Enum


class ErrorCategory(Enum):
    """Categories of errors in the orchestration system."""
    SYSTEM_ERROR = "system_error"
    CONFIGURATION_ERROR = "configuration_error"
    AGENT_ERROR = "agent_error"
    NETWORK_ERROR = "network_error"
    TIMEOUT_ERROR = "timeout_error"
    RESOURCE_ERROR = "resource_error"
    VALIDATION_ERROR = "validation_error"
    UNKNOWN_ERROR = "unknown_error"


class ErrorSeverity(Enum):
    """Severity levels for errors."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ClassifiedError:
    """A classified error with metadata."""
    
    def __init__(self, error: Exception, category: ErrorCategory, severity: ErrorSeverity, 
                 context: Dict[str, Any], recoverable: bool = True):
        self.error = error
        self.category = category
        self.severity = severity
        self.context = context
        self.recoverable = recoverable
        self.timestamp = None


def classify_error(error: Exception, context: Dict[str, Any] = None) -> ClassifiedError:
    """Classify an error based on its type and context.
    
    Args:
        error: The exception to classify
        context: Additional context about when the error occurred
        
    Returns:
        ClassifiedError with category, severity, and recovery information
    """
    if context is None:
        context = {}
    
    # Determine error category
    category = _determine_error_category(error, context)
    
    # Determine error severity
    severity = _determine_error_severity(error, context)
    
    # Determine if error is recoverable
    recoverable = _is_recoverable(error, category)
    
    return ClassifiedError(error, category, severity, context, recoverable)


def _determine_error_category(error: Exception, context: Dict[str, Any]) -> ErrorCategory:
    """Determine the category of an error."""
    error_type = type(error).__name__
    error_message = str(error).lower()
    
    # Network-related errors
    if any(keyword in error_message for keyword in ['connection', 'network', 'timeout', 'unreachable']):
        if 'timeout' in error_message:
            return ErrorCategory.TIMEOUT_ERROR
        return ErrorCategory.NETWORK_ERROR
    
    # Configuration-related errors
    if any(keyword in error_message for keyword in ['config', 'setting', 'parameter', 'yaml', 'json']):
        return ErrorCategory.CONFIGURATION_ERROR
    
    # Resource-related errors
    if any(keyword in error_message for keyword in ['memory', 'disk', 'cpu', 'resource']):
        return ErrorCategory.RESOURCE_ERROR
    
    # Validation errors
    if any(keyword in error_message for keyword in ['validation', 'invalid', 'missing', 'required']):
        return ErrorCategory.VALIDATION_ERROR
    
    # Agent-specific errors
    if any(keyword in error_message for keyword in ['agent', 'delegation', 'orchestration']):
        return ErrorCategory.AGENT_ERROR
    
    # System errors
    if any(keyword in error_message for keyword in ['system', 'os', 'permission', 'access']):
        return ErrorCategory.SYSTEM_ERROR
    
    return ErrorCategory.UNKNOWN_ERROR


def _determine_error_severity(error: Exception, context: Dict[str, Any]) -> ErrorSeverity:
    """Determine the severity of an error."""
    error_type = type(error).__name__
    error_message = str(error).lower()
    
    # Critical errors
    if any(keyword in error_message for keyword in ['critical', 'fatal', 'crash', 'corrupt']):
        return ErrorSeverity.CRITICAL
    
    # High severity errors
    if error_type in ['MemoryError', 'OSError', 'PermissionError']:
        return ErrorSeverity.HIGH
    
    # Medium severity errors
    if error_type in ['ValueError', 'KeyError', 'AttributeError', 'TimeoutError']:
        return ErrorSeverity.MEDIUM
    
    # Low severity errors
    return ErrorSeverity.LOW


def _is_recoverable(error: Exception, category: ErrorCategory) -> bool:
    """Determine if an error is recoverable."""
    # Some categories are generally recoverable
    recoverable_categories = [
        ErrorCategory.NETWORK_ERROR,
        ErrorCategory.TIMEOUT_ERROR,
        ErrorCategory.AGENT_ERROR
    ]
    
    if category in recoverable_categories:
        return True
    
    # Some error types are generally not recoverable
    non_recoverable_types = ['MemoryError', 'SystemError']
    if type(error).__name__ in non_recoverable_types:
        return False
    
    # Default to recoverable
    return True


def get_error_recovery_strategy(classified_error: ClassifiedError) -> Dict[str, Any]:
    """Get recovery strategy for a classified error.
    
    Args:
        classified_error: The classified error
        
    Returns:
        Dictionary containing recovery strategy information
    """
    if not classified_error.recoverable:
        return {
            'strategy': 'none',
            'action': 'fail_fast',
            'message': 'Error is not recoverable'
        }
    
    strategies = {
        ErrorCategory.NETWORK_ERROR: {
            'strategy': 'retry_with_backoff',
            'max_retries': 3,
            'backoff_factor': 2.0
        },
        ErrorCategory.TIMEOUT_ERROR: {
            'strategy': 'increase_timeout',
            'factor': 1.5,
            'max_timeout': 300
        },
        ErrorCategory.AGENT_ERROR: {
            'strategy': 'fallback_agent',
            'fallback_count': 2
        },
        ErrorCategory.CONFIGURATION_ERROR: {
            'strategy': 'reload_config',
            'validate_after_reload': True
        },
        ErrorCategory.RESOURCE_ERROR: {
            'strategy': 'resource_cleanup',
            'cleanup_actions': ['cache_clear', 'temp_file_cleanup']
        }
    }
    
    return strategies.get(classified_error.category, {
        'strategy': 'generic_retry',
        'max_retries': 2
    })