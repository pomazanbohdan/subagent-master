"""
Performance Monitoring System

Monitoring and metrics collection for the orchestration system.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import time
import threading
import logging


class PerformanceMetrics:
    """Container for performance metrics."""
    
    def __init__(self):
        self.task_count = 0
        self.success_count = 0
        self.error_count = 0
        self.total_response_time = 0.0
        self.min_response_time = float('inf')
        self.max_response_time = 0.0
        self.agent_performance = {}
        self.error_types = {}
        self.start_time = datetime.now()
    
    def record_task_start(self, task_id: str, agent: str = None):
        """Record the start of a task."""
        self.task_count += 1
        if agent:
            if agent not in self.agent_performance:
                self.agent_performance[agent] = {
                    'count': 0,
                    'successes': 0,
                    'errors': 0,
                    'total_time': 0.0
                }
            self.agent_performance[agent]['count'] += 1
    
    def record_task_success(self, task_id: str, response_time: float, agent: str = None):
        """Record successful task completion."""
        self.success_count += 1
        self.total_response_time += response_time
        self.min_response_time = min(self.min_response_time, response_time)
        self.max_response_time = max(self.max_response_time, response_time)
        
        if agent:
            self.agent_performance[agent]['successes'] += 1
            self.agent_performance[agent]['total_time'] += response_time
    
    def record_task_error(self, task_id: str, error_type: str, agent: str = None):
        """Record task error."""
        self.error_count += 1
        
        if error_type not in self.error_types:
            self.error_types[error_type] = 0
        self.error_types[error_type] += 1
        
        if agent:
            self.agent_performance[agent]['errors'] += 1
    
    def get_success_rate(self) -> float:
        """Calculate success rate."""
        if self.task_count == 0:
            return 0.0
        return self.success_count / self.task_count
    
    def get_average_response_time(self) -> float:
        """Calculate average response time."""
        if self.success_count == 0:
            return 0.0
        return self.total_response_time / self.success_count
    
    def get_agent_success_rate(self, agent: str) -> float:
        """Get success rate for specific agent."""
        if agent not in self.agent_performance:
            return 0.0
        
        agent_data = self.agent_performance[agent]
        if agent_data['count'] == 0:
            return 0.0
        
        return agent_data['successes'] / agent_data['count']
    
    def get_summary(self) -> Dict[str, Any]:
        """Get performance summary."""
        uptime = datetime.now() - self.start_time
        
        return {
            'task_count': self.task_count,
            'success_count': self.success_count,
            'error_count': self.error_count,
            'success_rate': self.get_success_rate(),
            'average_response_time': self.get_average_response_time(),
            'min_response_time': self.min_response_time if self.min_response_time != float('inf') else 0,
            'max_response_time': self.max_response_time,
            'uptime_seconds': uptime.total_seconds(),
            'agent_performance': self.agent_performance,
            'error_types': self.error_types
        }


class PerformanceMonitor:
    """Performance monitoring system."""
    
    def __init__(self, collection_interval: float = 60.0):
        self.collection_interval = collection_interval
        self.metrics = PerformanceMetrics()
        self.running = False
        self.thread = None
        self.callbacks = []
        self.logger = logging.getLogger(__name__)
    
    def start_monitoring(self):
        """Start performance monitoring."""
        if self.running:
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.thread.start()
        self.logger.info("Performance monitoring started")
    
    def stop_monitoring(self):
        """Stop performance monitoring."""
        self.running = False
        if self.thread:
            self.thread.join()
        self.logger.info("Performance monitoring stopped")
    
    def record_task_start(self, task_id: str, agent: str = None):
        """Record task start."""
        self.metrics.record_task_start(task_id, agent)
    
    def record_task_success(self, task_id: str, response_time: float, agent: str = None):
        """Record task success."""
        self.metrics.record_task_success(task_id, response_time, agent)
    
    def record_task_error(self, task_id: str, error_type: str, agent: str = None):
        """Record task error."""
        self.metrics.record_task_error(task_id, error_type, agent)
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics."""
        return self.metrics.get_summary()
    
    def add_callback(self, callback: Callable):
        """Add a callback for metric updates."""
        self.callbacks.append(callback)
    
    def _monitoring_loop(self):
        """Main monitoring loop."""
        while self.running:
            try:
                # Collect and report metrics
                metrics = self.get_metrics()
                
                # Call callbacks
                for callback in self.callbacks:
                    try:
                        callback(metrics)
                    except Exception as e:
                        self.logger.error(f"Error in monitoring callback: {e}")
                
                time.sleep(self.collection_interval)
            
            except Exception as e:
                self.logger.error(f"Error in monitoring loop: {e}")
                time.sleep(self.collection_interval)


# Global performance monitor instance
_performance_monitor = None


def get_performance_monitor() -> PerformanceMonitor:
    """Get the global performance monitor instance."""
    global _performance_monitor
    if _performance_monitor is None:
        _performance_monitor = PerformanceMonitor()
    return _performance_monitor


def monitor_performance():
    """Start performance monitoring."""
    monitor = get_performance_monitor()
    monitor.start_monitoring()
    return monitor


def stop_monitoring():
    """Stop performance monitoring."""
    monitor = get_performance_monitor()
    monitor.stop_monitoring()


def record_task_metrics(task_id: str, success: bool, response_time: float = None, 
                      error_type: str = None, agent: str = None):
    """Record task metrics."""
    monitor = get_performance_monitor()
    
    if success and response_time is not None:
        monitor.record_task_success(task_id, response_time, agent)
    elif not success:
        monitor.record_task_error(task_id, error_type or "unknown", agent)


def get_performance_summary() -> Dict[str, Any]:
    """Get current performance summary."""
    monitor = get_performance_monitor()
    return monitor.get_metrics()