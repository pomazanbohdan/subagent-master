"""
Configuration Loader System

Dynamic configuration loading, validation, and management.
"""

from typing import Dict, List, Any, Optional, Union
from pathlib import Path
import yaml
import json
import logging
from datetime import datetime


class ConfigurationLoader:
    """Dynamic configuration loader with validation and hot reload capabilities."""
    
    def __init__(self, config_root: str = "config"):
        self.config_root = Path(config_root)
        self.configurations = {}
        self.schema_validators = {}
        self.last_modified = {}
        self.logger = logging.getLogger(__name__)
    
    def load_configuration(self, config_path: str, validate: bool = True) -> Dict[str, Any]:
        """Load configuration from file.
        
        Args:
            config_path: Path to configuration file relative to config_root
            validate: Whether to validate the configuration against schema
            
        Returns:
            Dictionary containing loaded configuration
        """
        full_path = self.config_root / config_path
        
        if not full_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {full_path}")
        
        # Load based on file extension
        if full_path.suffix.lower() in ['.yaml', '.yml']:
            config = self._load_yaml(full_path)
        elif full_path.suffix.lower() == '.json':
            config = self._load_json(full_path)
        else:
            raise ValueError(f"Unsupported configuration file format: {full_path.suffix}")
        
        # Validate if requested
        if validate and config_path in self.schema_validators:
            self._validate_configuration(config, config_path)
        
        # Store configuration and track modification time
        self.configurations[config_path] = config
        self.last_modified[config_path] = full_path.stat().st_mtime
        
        self.logger.info(f"Configuration loaded: {config_path}")
        return config
    
    def reload_configuration(self, config_path: str) -> Dict[str, Any]:
        """Reload configuration if file has been modified."""
        full_path = self.config_root / config_path
        
        if not full_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {full_path}")
        
        current_mtime = full_path.stat().st_mtime
        last_mtime = self.last_modified.get(config_path, 0)
        
        if current_mtime > last_mtime:
            self.logger.info(f"Reloading modified configuration: {config_path}")
            return self.load_configuration(config_path, validate=True)
        
        return self.configurations.get(config_path, {})
    
    def get_configuration(self, config_path: str, auto_reload: bool = True) -> Dict[str, Any]:
        """Get configuration, optionally auto-reloading if modified."""
        if auto_reload:
            self.reload_configuration(config_path)
        
        return self.configurations.get(config_path, {})
    
    def _load_yaml(self, file_path: Path) -> Dict[str, Any]:
        """Load YAML configuration file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in {file_path}: {e}")
    
    def _load_json(self, file_path: Path) -> Dict[str, Any]:
        """Load JSON configuration file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {file_path}: {e}")
    
    def _validate_configuration(self, config: Dict[str, Any], config_path: str):
        """Validate configuration against schema."""
        # This would implement schema validation
        # For now, just perform basic validation
        if not isinstance(config, dict):
            raise ValueError(f"Configuration must be a dictionary: {config_path}")
        
        self.logger.debug(f"Configuration validated: {config_path}")
    
    def register_schema_validator(self, config_path: str, validator: callable):
        """Register a schema validator for a configuration file."""
        self.schema_validators[config_path] = validator
    
    def list_configurations(self) -> List[str]:
        """List all loaded configuration files."""
        return list(self.configurations.keys())
    
    def clear_configuration(self, config_path: str):
        """Clear a specific configuration from memory."""
        if config_path in self.configurations:
            del self.configurations[config_path]
        if config_path in self.last_modified:
            del self.last_modified[config_path]
    
    def clear_all_configurations(self):
        """Clear all configurations from memory."""
        self.configurations.clear()
        self.last_modified.clear()


# Global configuration loader instance
_config_loader = None


def get_configuration_loader() -> ConfigurationLoader:
    """Get the global configuration loader instance."""
    global _config_loader
    if _config_loader is None:
        _config_loader = ConfigurationLoader()
    return _config_loader


def load_configuration(config_path: str, validate: bool = True) -> Dict[str, Any]:
    """Load configuration using the global loader."""
    return get_configuration_loader().load_configuration(config_path, validate)


def validate_configuration(config: Dict[str, Any], schema_path: str = None) -> bool:
    """Validate a configuration dictionary.
    
    Args:
        config: Configuration dictionary to validate
        schema_path: Optional path to schema file
        
    Returns:
        True if validation passes, False otherwise
    """
    try:
        # Basic validation
        if not isinstance(config, dict):
            return False
        
        # Check for required fields based on configuration type
        required_fields = ['name', 'version']  # Basic required fields
        
        for field in required_fields:
            if field not in config:
                logging.warning(f"Missing required field: {field}")
                return False
        
        # Additional validation logic would go here
        return True
    
    except Exception as e:
        logging.error(f"Configuration validation error: {e}")
        return False


def load_agent_configuration(agent_name: str) -> Dict[str, Any]:
    """Load configuration for a specific agent."""
    config_path = f"agents/master_agents.yaml"
    agent_config = load_configuration(config_path)
    
    agents = agent_config.get('agents', {})
    return agents.get(agent_name, {})


def load_system_configuration() -> Dict[str, Any]:
    """Load system-wide configuration."""
    return load_configuration("core/configuration_loader.yaml")


def is_configuration_ready() -> bool:
    """Check if configuration system is ready."""
    try:
        loader = get_configuration_loader()
        return len(loader.list_configurations()) > 0
    except Exception:
        return False