"""
Error Delegation System

Intelligent delegation of error handling to specialized error recovery agents.
"""

from typing import Dict, List, Any, Optional, Callable
from .classification import ClassifiedError, ErrorCategory, ErrorSeverity


class ErrorDelegationStrategy:
    """Strategy for delegating error handling."""
    
    def __init__(self, handler: Callable, priority: int = 0, conditions: List[Callable] = None):
        self.handler = handler
        self.priority = priority
        self.conditions = conditions or []


def delegate_error_handling(classified_error: ClassifiedError, 
                          available_handlers: Dict[str, Callable] = None) -> Dict[str, Any]:
    """Delegate error handling to appropriate specialized handlers.
    
    Args:
        classified_error: The classified error to handle
        available_handlers: Dictionary of available error handlers
        
    Returns:
        Dictionary containing delegation result and handler information
    """
    if available_handlers is None:
        available_handlers = {}
    
    # Determine delegation strategy based on error characteristics
    strategy = _determine_delegation_strategy(classified_error)
    
    # Select appropriate handler
    selected_handler = _select_handler(classified_error, strategy, available_handlers)
    
    if selected_handler:
        try:
            # Execute the selected handler
            result = selected_handler(classified_error)
            
            return {
                'success': True,
                'handler': selected_handler.__name__,
                'strategy': strategy,
                'result': result,
                'error_resolved': result.get('resolved', False)
            }
        except Exception as handler_error:
            return {
                'success': False,
                'handler': selected_handler.__name__,
                'strategy': strategy,
                'error': str(handler_error),
                'error_resolved': False
            }
    else:
        return {
            'success': False,
            'handler': None,
            'strategy': strategy,
            'error': 'No suitable handler found',
            'error_resolved': False
        }


def _determine_delegation_strategy(classified_error: ClassifiedError) -> str:
    """Determine the best delegation strategy for an error."""
    category = classified_error.category
    severity = classified_error.severity
    
    # Critical errors need immediate attention
    if severity == ErrorSeverity.CRITICAL:
        return 'urgent_specialist'
    
    # Network and timeout errors can often be handled automatically
    if category in [ErrorCategory.NETWORK_ERROR, ErrorCategory.TIMEOUT_ERROR]:
        return 'auto_retry'
    
    # Configuration errors need configuration specialists
    if category == ErrorCategory.CONFIGURATION_ERROR:
        return 'config_specialist'
    
    # Agent errors need orchestration specialists
    if category == ErrorCategory.AGENT_ERROR:
        return 'orchestration_specialist'
    
    # Resource errors need system specialists
    if category == ErrorCategory.RESOURCE_ERROR:
        return 'system_specialist'
    
    # Default to general error handling
    return 'general_handler'


def _select_handler(classified_error: ClassifiedError, 
                   strategy: str, 
                   available_handlers: Dict[str, Callable]) -> Optional[Callable]:
    """Select the best handler for the given strategy."""
    # Handler mapping for different strategies
    handler_mapping = {
        'urgent_specialist': ['critical_error_handler', 'emergency_handler'],
        'auto_retry': ['retry_handler', 'network_handler', 'timeout_handler'],
        'config_specialist': ['config_handler', 'validation_handler'],
        'orchestration_specialist': ['orchestration_handler', 'agent_handler'],
        'system_specialist': ['system_handler', 'resource_handler'],
        'general_handler': ['general_error_handler', 'default_handler']
    }
    
    preferred_handlers = handler_mapping.get(strategy, ['general_error_handler'])
    
    # Find the first available handler from preferred list
    for handler_name in preferred_handlers:
        if handler_name in available_handlers:
            return available_handlers[handler_name]
    
    # If no preferred handler is available, try any handler
    for handler_name, handler in available_handlers.items():
        if _can_handle_error(handler, classified_error):
            return handler
    
    return None


def _can_handle_error(handler: Callable, classified_error: ClassifiedError) -> bool:
    """Check if a handler can handle a specific error."""
    # This would implement logic to check handler capabilities
    # For now, return True as a default
    return True


def create_error_handlers() -> Dict[str, Callable]:
    """Create a default set of error handlers."""
    handlers = {}
    
    def critical_error_handler(error: ClassifiedError) -> Dict[str, Any]:
        """Handle critical errors with immediate attention."""
        return {
            'resolved': False,
            'action': 'escalate',
            'priority': 'critical',
            'message': 'Critical error requires immediate attention'
        }
    
    def retry_handler(error: ClassifiedError) -> Dict[str, Any]:
        """Handle errors with retry logic."""
        return {
            'resolved': True,
            'action': 'retry',
            'max_retries': 3,
            'backoff_factor': 2.0,
            'message': 'Error will be handled with retry logic'
        }
    
    def config_handler(error: ClassifiedError) -> Dict[str, Any]:
        """Handle configuration errors."""
        return {
            'resolved': True,
            'action': 'reload_config',
            'validate': True,
            'message': 'Configuration will be reloaded and validated'
        }
    
    def general_error_handler(error: ClassifiedError) -> Dict[str, Any]:
        """Handle general errors."""
        return {
            'resolved': error.recoverable,
            'action': 'log_and_continue' if error.recoverable else 'fail',
            'message': f'General error handling for {error.category.value}'
        }
    
    # Register handlers
    handlers['critical_error_handler'] = critical_error_handler
    handlers['retry_handler'] = retry_handler
    handlers['config_handler'] = config_handler
    handlers['general_error_handler'] = general_error_handler
    
    return handlers