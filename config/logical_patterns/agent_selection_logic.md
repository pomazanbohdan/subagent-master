# Agent Selection Logic Patterns

## Core Selection Algorithm

### 1. Task Analysis
```python
def analyze_task_complexity(description):
    complexity_indicators = {
        'very_complex': ['enterprise', 'scalable', 'distributed', 'system-wide'],
        'complex': ['design', 'implement', 'optimize', 'integrate'],
        'medium': ['create', 'build', 'develop', 'configure'],
        'simple': ['fix', 'update', 'modify', 'adjust']
    }
    # Count indicators and calculate complexity score
```

### 2. Competency Matching
```python
def calculate_compatibility_score(agent, task_requirements):
    competency_score = sum(1 for req in task_requirements 
                         if req in agent.specialties) / len(task_requirements)
    performance_score = agent.success_rate * agent.competency_score
    load_score = max(0, (agent.max_capacity - agent.current_load) / agent.max_capacity)
    
    # Weighted combination
    total_score = (performance_score * 0.4 + 
                   load_score * 0.3 + 
                   competency_score * 0.3)
    return total_score
```

### 3. Dynamic Thresholds
```python
def update_selection_dynamically(current_performance, system_load):
    quality_threshold = current_performance * (1 - system_load)
    complexity_threshold = system_load
    
    return {
        'quality_threshold': quality_threshold,
        'complexity_threshold': complexity_threshold
    }
```

## Selection Patterns

### High Priority Tasks
- System critical errors
- Security vulnerabilities  
- Performance bottlenecks
- **Agent**: Most competent available
- **Threshold**: Lower performance requirements for availability

### Complex Projects
- Multi-system integration
- Architecture design
- Feature development
- **Process**: Create task plan → Multi-agent coordination
- **Duration**: Extended timeline with milestones

### Simple Requests  
- Bug fixes
- Documentation updates
- Minor adjustments
- **Agent**: Available agent with basic competency
- **Response**: Direct execution

## Load Balancing Strategy

### Agent Availability Check
```python
def check_agent_availability(agent):
    load_ratio = agent.current_load / agent.max_capacity
    return {
        'available': load_ratio < 0.8,
        'load_ratio': load_ratio,
        'can_accept_task': agent.current_load < agent.max_capacity
    }
```

### Dynamic Distribution
- **Prefer underutilized agents** (load < 0.3)
- **Balance workload** across available agents
- **Consider specialization** for complex tasks
- **Use general-purpose** for overflow handling
