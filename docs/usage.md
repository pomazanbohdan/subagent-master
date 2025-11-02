# Usage Documentation

## Getting Started

The SubAgent Master is an orchestration system that coordinates task execution between specialized sub-agents. It analyzes tasks, categorizes them, and delegates to appropriate agents.

## Basic Usage

### 1. Agent Selection

The system automatically selects the most appropriate agent based on:

- Task complexity and requirements
- Agent capabilities and expertise
- Historical performance
- Resource availability

### 2. Task Categorization

Tasks are categorized using:

- TF-IDF analysis for text-based tasks
- Machine learning classification
- Rule-based categorization
- Pattern matching

### 3. Parallel Execution

Multiple agents can work in parallel when:

- Tasks are independent
- Resources are available
- Coordination requirements are met

## Configuration

### Loading Configuration

```yaml
# The system automatically loads configuration from:
config/knowledge-base/
config/core/
config/dynamic/
config/rules/
```

### Agent Registry

Agents are registered in `config/dynamic/enhanced_agent_registry.yaml` with their:
- Capabilities
- Resource requirements
- Performance metrics
- Availability

## Task Flow

1. **Task Submission** - User submits a task
2. **Analysis** - System analyzes task complexity and requirements
3. **Categorization** - Task is categorized using multiple algorithms
4. **Agent Selection** - Most appropriate agent(s) are selected
5. **Execution** - Task is delegated and executed
6. **Monitoring** - Progress is monitored and logged
7. **Completion** - Results are collected and returned

## Performance Optimization

### Caching

- Task analysis results are cached
- Agent performance metrics are stored
- Configuration is cached for fast access

### Load Balancing

- Tasks are distributed across available agents
- Resource usage is monitored
- Bottlenecks are identified and resolved

## Error Handling

The system handles errors through:

- Graceful degradation
- Automatic retry mechanisms
- Fallback agent selection
- Detailed error logging

## Monitoring

### Metrics Collected

- Task completion time
- Agent performance
- Resource utilization
- Error rates

### Logs

All operations are logged with:

- Timestamp
- Operation details
- Agent information
- Results

## Troubleshooting

### Common Issues

1. **Agent Selection Failure**
   - Check agent registry configuration
   - Verify agent availability
   - Review selection rules

2. **Task Categorization Errors**
   - Validate categorization engine configuration
   - Check training data for ML models
   - Review TF-IDF system setup

3. **Performance Issues**
   - Monitor resource utilization
   - Check for bottlenecks
   - Optimize agent allocation

### Debug Mode

Enable debug mode for detailed logging:
- Set log level to DEBUG
- Enable detailed task tracing
- Monitor system performance in real-time