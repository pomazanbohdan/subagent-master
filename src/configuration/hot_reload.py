"""
Hot Reload System

Hot reload functionality for configuration changes.
"""

from typing import Dict, List, Any, Callable, Optional
from pathlib import Path
import time
import threading
import logging
from .loader import get_configuration_loader


class HotReloadManager:
    """Manages hot reloading of configuration files."""
    
    def __init__(self, check_interval: float = 1.0):
        self.check_interval = check_interval
        self.watched_files = {}
        self.callbacks = {}
        self.running = False
        self.thread = None
        self.logger = logging.getLogger(__name__)
    
    def watch_file(self, file_path: str, callback: Callable = None):
        """Watch a configuration file for changes.
        
        Args:
            file_path: Path to the file to watch
            callback: Optional callback to call when file changes
        """
        full_path = Path(file_path)
        if full_path.exists():
            self.watched_files[file_path] = full_path.stat().st_mtime
            if callback:
                self.callbacks[file_path] = callback
            self.logger.info(f"Watching file for changes: {file_path}")
    
    def unwatch_file(self, file_path: str):
        """Stop watching a file."""
        if file_path in self.watched_files:
            del self.watched_files[file_path]
        if file_path in self.callbacks:
            del self.callbacks[file_path]
        self.logger.info(f"Stopped watching file: {file_path}")
    
    def start_watching(self):
        """Start the hot reload monitoring thread."""
        if self.running:
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._watch_loop, daemon=True)
        self.thread.start()
        self.logger.info("Hot reload monitoring started")
    
    def stop_watching(self):
        """Stop the hot reload monitoring thread."""
        self.running = False
        if self.thread:
            self.thread.join()
        self.logger.info("Hot reload monitoring stopped")
    
    def _watch_loop(self):
        """Main monitoring loop."""
        while self.running:
            try:
                self._check_files()
                time.sleep(self.check_interval)
            except Exception as e:
                self.logger.error(f"Error in hot reload loop: {e}")
    
    def _check_files(self):
        """Check for file modifications."""
        config_loader = get_configuration_loader()
        
        for file_path, last_mtime in list(self.watched_files.items()):
            full_path = Path(file_path)
            
            if not full_path.exists():
                self.logger.warning(f"Watched file disappeared: {file_path}")
                continue
            
            current_mtime = full_path.stat().st_mtime
            if current_mtime > last_mtime:
                self.logger.info(f"File modified: {file_path}")
                
                try:
                    # Reload configuration
                    config_loader.reload_configuration(file_path)
                    
                    # Update modification time
                    self.watched_files[file_path] = current_mtime
                    
                    # Call callback if registered
                    if file_path in self.callbacks:
                        callback = self.callbacks[file_path]
                        callback(file_path, config_loader.get_configuration(file_path))
                    
                    self.logger.info(f"Successfully reloaded: {file_path}")
                
                except Exception as e:
                    self.logger.error(f"Failed to reload {file_path}: {e}")


# Global hot reload manager
_hot_reload_manager = None


def get_hot_reload_manager() -> HotReloadManager:
    """Get the global hot reload manager instance."""
    global _hot_reload_manager
    if _hot_reload_manager is None:
        _hot_reload_manager = HotReloadManager()
    return _hot_reload_manager


def enable_hot_reload(file_paths: List[str] = None, callbacks: Dict[str, Callable] = None):
    """Enable hot reload for configuration files.
    
    Args:
        file_paths: List of file paths to watch
        callbacks: Dictionary mapping file paths to callback functions
    """
    if file_paths is None:
        file_paths = [
            "config/agents/master_agents.yaml",
            "config/dynamic/agent_registry.yaml",
            "config/rules/selection_rules.yaml"
        ]
    
    manager = get_hot_reload_manager()
    
    # Watch files
    for file_path in file_paths:
        callback = callbacks.get(file_path) if callbacks else None
        manager.watch_file(file_path, callback)
    
    # Start monitoring
    manager.start_watching()


def disable_hot_reload():
    """Disable hot reload monitoring."""
    manager = get_hot_reload_manager()
    manager.stop_watching()


def add_watch_file(file_path: str, callback: Callable = None):
    """Add a file to hot reload monitoring."""
    manager = get_hot_reload_manager()
    manager.watch_file(file_path, callback)


def remove_watch_file(file_path: str):
    """Remove a file from hot reload monitoring."""
    manager = get_hot_reload_manager()
    manager.unwatch_file(file_path)


def default_reload_callback(file_path: str, config: Dict[str, Any]):
    """Default callback for configuration reload."""
    logging.info(f"Configuration reloaded: {file_path}")
    # Additional default processing can be added here