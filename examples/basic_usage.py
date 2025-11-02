"""
Basic Usage Examples for Master Agent

This file demonstrates common usage patterns for the master agent orchestration system.
"""

# Example 1: Simple Task Delegation
def example_simple_task():
    """Example of simple task delegation to a single agent."""
    
    # Input task description
    task = "Fix authentication bug in login API"
    
    # Expected behavior:
    # - Complexity analysis: Low (0.3)
    # - Agent selection: backend-architect
    # - Execution strategy: Sequential
    # - Result: Direct delegation and execution
    
    print(f"Processing: {task}")
    # result = master_agent.process_task(task)
    # Expected: backend-architect agent handles the bug fix


# Example 2: Complex Multi-Agent Coordination
def example_complex_coordination():
    """Example of complex task requiring multiple agents."""
    
    task = "Design and implement complete authentication system"
    
    # Expected behavior:
    # - Complexity analysis: High (0.9)
    # - Agent selection: backend-architect + security-engineer
    # - Execution strategy: Sequential with coordination
    # - Result: Coordinated multi-agent execution
    
    subtasks = [
        "Design secure authentication architecture",
        "Implement user registration endpoints",
        "Add password security features",
        "Create session management",
        "Add OAuth integration"
    ]
    
    print(f"Processing complex task: {task}")
    # result = master_agent.process_task(task)
    # Expected: Plan created, multiple agents coordinated


# Example 3: Parallel Execution
def example_parallel_execution():
    """Example of parallel task execution."""
    
    task = "Develop e-commerce product management feature"
    
    # Expected behavior:
    # - Complexity analysis: High (0.8)
    # - Parallel potential: High (>0.7)
    # - Task breakdown: Backend API + Frontend UI
    # - Agent selection: backend-architect + frontend-architect
    # - Execution strategy: Parallel
    
    parallel_components = [
        "Design database schema for products",
        "Implement REST API endpoints", 
        "Create responsive frontend interface",
        "Add product image upload"
    ]
    
    backend_tasks = [
        "Design database schema for products",
        "Implement REST API endpoints"
    ]
    
    frontend_tasks = [
        "Create responsive frontend interface", 
        "Add product image upload"
    ]
    
    print(f"Processing parallel task: {task}")
    # result = master_agent.process_task(task, strategy="parallel")
    # Expected: Backend and frontend developed simultaneously


# Example 4: Competitive Execution
def example_competitive_execution():
    """Example of competitive execution for best result selection."""
    
    task = "Create optimal system architecture for high-traffic application"
    
    # Expected behavior:
    # - Complexity analysis: High (0.9)
    # - Ambiguous requirements: Multiple valid approaches
    # - Agent selection: system-architect + backend-architect
    # - Execution strategy: Competitive
    # - Result: Best architecture selected from multiple options
    
    print(f"Processing competitive task: {task}")
    # result = master_agent.process_task(task, strategy="competitive")
    # Expected: Multiple agents create solutions, best selected


# Example 5: Error Handling and Recovery
def example_error_handling():
    """Example of error handling and recovery mechanisms."""
    
    task = "Connect to external API service"
    
    # Scenario: Network failure occurs
    # Expected behavior:
    # - Error classification: Network error
    # - Recovery strategy: Retry with exponential backoff
    # - Fallback: Use cached data or alternative service
    
    error_scenarios = [
        {
            "type": "NetworkError",
            "recovery": "Retry with backoff",
            "max_retries": 3
        },
        {
            "type": "TimeoutError", 
            "recovery": "Increase timeout",
            "factor": 1.5
        },
        {
            "type": "ConfigurationError",
            "recovery": "Reload configuration",
            "validate": True
        }
    ]
    
    print(f"Processing task with error handling: {task}")
    # result = master_agent.process_task(task)
    # Expected: Automatic error recovery


# Example 6: Performance Monitoring
def example_performance_monitoring():
    """Example of performance monitoring setup and analysis."""
    
    from src.utils import monitor_performance, get_performance_summary
    
    # Start monitoring
    monitor = monitor_performance()
    
    # Process various tasks
    tasks = [
        "Simple bug fix",
        "Complex feature development", 
        "Multi-agent coordination",
        "Parallel execution"
    ]
    
    # for task in tasks:
    #     master_agent.process_task(task)
    
    # Get performance metrics
    metrics = get_performance_summary()
    
    performance_analysis = {
        "total_tasks": metrics.get("task_count", 0),
        "success_rate": metrics.get("success_rate", 0),
        "avg_response_time": metrics.get("average_response_time", 0),
        "agent_performance": metrics.get("agent_performance", {})
    }
    
    print("Performance Analysis:")
    for key, value in performance_analysis.items():
        print(f"  {key}: {value}")


# Example 7: Configuration Management
def example_configuration_management():
    """Example of dynamic configuration loading and hot reload."""
    
    from src.configuration import load_configuration, enable_hot_reload
    
    # Load agent configuration
    agent_config = load_configuration("config/agents/master_agents.yaml")
    
    # Load selection rules
    rules_config = load_configuration("config/rules/selection_rules.yaml")
    
    # Enable hot reload for configuration changes
    enable_hot_reload([
        "config/agents/master_agents.yaml",
        "config/rules/selection_rules.yaml",
        "config/dynamic/agent_registry.yaml"
    ])
    
    print("Configuration loaded with hot reload enabled")
    
    # Configuration can now be updated without system restart
    # Changes will be automatically detected and reloaded


# Example 8: Custom Agent Selection
def example_custom_selection():
    """Example of custom agent selection with preferences."""
    
    task = "Optimize database performance"
    
    # Custom agent preferences
    preferred_agents = ["performance-engineer", "backend-architect"]
    
    # Process with preferred agents
    # result = master_agent.process_task(
    #     task,
    #     preferred_agents=preferred_agents
    # )
    
    # Alternative: Specify execution strategy
    # result = master_agent.process_task(
    #     task,
    #     strategy="sequential",
    #     timeout=300  # 5 minutes
    # )
    
    print(f"Processing with custom selection: {task}")
    print(f"Preferred agents: {preferred_agents}")


# Example 9: Multi-Task Processing
def example_multi_task_processing():
    """Example of processing multiple related tasks."""
    
    project_tasks = [
        "Set up development environment",
        "Create project structure",
        "Implement core features",
        "Add testing framework",
        "Deploy to production"
    ]
    
    # Process tasks sequentially with coordination
    # results = master_agent.process_tasks(project_tasks)
    
    # Alternative: Process with specific strategy per task
    task_strategies = {
        "Set up development environment": "sequential",
        "Create project structure": "sequential", 
        "Implement core features": "parallel",
        "Add testing framework": "sequential",
        "Deploy to production": "sequential"
    }
    
    print("Multi-task project execution:")
    for i, task in enumerate(project_tasks, 1):
        strategy = task_strategies.get(task, "sequential")
        print(f"{i}. {task} (Strategy: {strategy})")


# Example 10: System Status and Health Check
def example_system_health_check():
    """Example of system status monitoring and health checks."""
    
    # Check system readiness
    # system_status = master_agent.get_system_status()
    
    health_check_results = {
        "configuration_loaded": True,
        "agents_registered": True,
        "error_system_active": True,
        "performance_monitoring": True,
        "system_ready": True
    }
    
    # Get agent availability
    # agent_status = master_agent.get_agent_status()
    
    agent_availability = {
        "system-architect": "available",
        "backend-architect": "available",
        "frontend-architect": "busy",
        "performance-engineer": "available",
        "security-engineer": "available"
    }
    
    print("System Health Check:")
    for component, status in health_check_results.items():
        print(f"  {component}: {'✓' if status else '✗'}")
    
    print("\nAgent Availability:")
    for agent, status in agent_availability.items():
        print(f"  {agent}: {status}")


# Main execution function
if __name__ == "__main__":
    print("Master Agent Usage Examples")
    print("=" * 50)
    
    # Run all examples
    examples = [
        ("Simple Task", example_simple_task),
        ("Complex Coordination", example_complex_coordination),
        ("Parallel Execution", example_parallel_execution),
        ("Competitive Execution", example_competitive_execution),
        ("Error Handling", example_error_handling),
        ("Performance Monitoring", example_performance_monitoring),
        ("Configuration Management", example_configuration_management),
        ("Custom Selection", example_custom_selection),
        ("Multi-Task Processing", example_multi_task_processing),
        ("System Health Check", example_system_health_check)
    ]
    
    for name, example_func in examples:
        print(f"\n{name}:")
        print("-" * 30)
        example_func()
        print()