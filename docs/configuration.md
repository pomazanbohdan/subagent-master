# Configuration Documentation

## Overview

The SubAgent Master configuration system is designed to be modular, extensible, and maintainable. All configuration files are stored in the `config/` directory and follow a hierarchical structure.

## Configuration Structure

### Knowledge Base (`config/knowledge-base/`)

The knowledge base contains the core logic for agent selection, task categorization, and coordination:

- **agent-selection.yaml** - Implements algorithms for selecting the most appropriate agent based on task characteristics
- **categorization-engine.yaml** - Task categorization system with TF-IDF analysis and ML-based classification  
- **parallel_coordination.yaml** - Manages parallel execution of multiple agents
- **task-analysis.yaml** - Framework for analyzing task complexity and requirements
- **tfidf-system.yaml** - TF-IDF analysis system for text-based task categorization

### Core Configuration (`config/core/`)

Essential system configuration components:

- **configuration_loader.yaml** - Handles loading and validation of all configuration files

### Dynamic Configuration (`config/dynamic/`)

Runtime configuration and agent registry:

- **config_loader.yaml** - Dynamic configuration loading with hot-reload capabilities
- **enhanced_agent_registry.yaml** - Registry of available agents with capabilities and metadata

### Rules Configuration (`config/rules/`)

System rules and constraints:

- **selection_rules.yaml** - Rules governing agent selection process
- **parallel_execution_rules.yaml** - Rules for parallel execution coordination

## Configuration Schema

All YAML configuration files follow a consistent schema:

```yaml
metadata:
  name: string
  version: string
  description: string
  last_modified: datetime

configuration:
  # Configuration-specific content
```

## Hot Reload System

The configuration system supports hot reloading of configuration files. When a configuration file is modified, the system automatically:

1. Validates the new configuration
2. Updates the running system
3. Logs the change
4. Notifies dependent components

## Validation

All configuration files are validated against their respective schemas before being loaded. Invalid configurations will:

1. Prevent system startup
2. Log validation errors
3. Provide detailed error messages
4. Suggest corrections