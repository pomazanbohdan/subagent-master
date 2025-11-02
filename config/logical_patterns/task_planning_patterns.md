# Task Planning Patterns

## Enhanced Task Decomposition Framework

### 1. Comprehensive Analysis
```python
def analyze_task_requirements(description, system_state):
    entities = extract_technical_entities(description)
    requirements = extract_functional_requirements(description)
    complexity = assess_complexity_indicators(description)
    constraints = identify_resource_constraints(system_state)

    return {
        'entities': entities,
        'requirements': requirements,
        'complexity': complexity,
        'estimated_effort': calculate_effort(entities, requirements, complexity),
        'resource_constraints': constraints,
        'priority_level': determine_priority(description, system_state),
        'dependencies': identify_external_dependencies(description)
    }
```

### 2. Resource-Aware Template Matching
```python
def find_applicable_template(task_analysis, available_resources):
    template_patterns = {
        'system_design': {
            'keywords': ['architecture', 'design', 'system'],
            'subtasks': ['requirements_analysis', 'architecture_design', 'component_design'],
            'typical_duration': 4.0,
            'resource_requirements': {'agents': 2, 'time': 240},
            'complexity_threshold': 0.7
        },
        'implementation': {
            'keywords': ['implement', 'build', 'create'],
            'subtasks': ['core_functionality', 'supporting_components', 'testing'],
            'typical_duration': 6.0,
            'resource_requirements': {'agents': 1-3, 'time': 360},
            'complexity_threshold': 0.5
        },
        'optimization': {
            'keywords': ['optimize', 'performance', 'efficiency'],
            'subtasks': ['analysis', 'implementation', 'validation'],
            'typical_duration': 5.0,
            'resource_requirements': {'specialized_agents': 1, 'time': 300},
            'complexity_threshold': 0.8
        }
    }

    # Match based on keyword overlap, complexity, AND resource availability
    return match_template_with_constraints(template_patterns, task_analysis, available_resources)
```

### 3. Constraint-Aware Subtask Generation
```python
def generate_subtasks_with_constraints(task_analysis, template, available_resources):
    base_subtasks = template.get('subtasks', [])

    # Validate resource feasibility
    if not validate_resource_feasibility(template, available_resources):
        return create_minimal_feasible_plan(task_analysis, available_resources)

    # Customize based on task specifics and constraints
    customized_subtasks = []
    for subtask in base_subtasks:
        subtask_plan = {
            'title': adapt_title(subtask, task_analysis),
            'type': determine_subtask_type(subtask),
            'dependencies': identify_dependencies(subtask, base_subtasks),
            'estimated_duration': calculate_duration(subtask, task_analysis),
            'resource_requirements': calculate_resource_needs(subtask, template),
            'priority': calculate_subtask_priority(subtask, task_analysis),
            'risk_level': assess_subtask_risk(subtask, available_resources)
        }

        # Validate subtask feasibility
        if validate_subtask_feasibility(subtask_plan, available_resources):
            customized_subtasks.append(subtask_plan)
        else:
            # Adapt subtask to available resources
            adapted_plan = adapt_subtask_to_resources(subtask_plan, available_resources)
            if adapted_plan:
                customized_subtasks.append(adapted_plan)

    return customized_subtasks
```

### 4. Dependency Management
```python
def manage_dependencies_with_constraints(subtasks, available_resources):
    dependency_graph = build_dependency_graph(subtasks)

    # Check for circular dependencies
    if has_circular_dependencies(dependency_graph):
        dependency_graph = resolve_circular_dependencies(dependency_graph)

    # Optimize execution order based on resource availability
    execution_plan = optimize_execution_order(dependency_graph, available_resources)

    # Identify parallel execution opportunities
    parallel_groups = identify_parallelizable_subtasks(execution_plan, available_resources)

    return {
        'execution_plan': execution_plan,
        'parallel_groups': parallel_groups,
        'total_duration': calculate_total_duration(execution_plan),
        'resource_utilization': calculate_resource_utilization(execution_plan, available_resources)
    }
```

### 5. Resource Validation and Adaptation
```python
def validate_and_adapt_plan(plan, available_resources):
    validation_results = {
        'is_valid': True,
        'issues': [],
        'adaptations': []
    }

    # Check resource availability
    for subtask in plan['subtasks']:
        if not has_sufficient_resources(subtask, available_resources):
            validation_results['issues'].append(f"Insufficient resources for {subtask['title']}")

            # Try to adapt subtask
            adapted_subtask = adapt_subtask_resources(subtask, available_resources)
            if adapted_subtask:
                validation_results['adaptations'].append(adapted_subtask)
            else:
                validation_results['is_valid'] = False

    # Check timeline feasibility
    if plan['total_duration'] > get_max_acceptable_duration(available_resources):
        validation_results['issues'].append("Plan duration exceeds acceptable limits")
        plan = compress_plan_timeline(plan)
        validation_results['adaptations'].append("Timeline compressed")

    return validation_results, plan
```

## Enhanced Planning Patterns with Error Handling

### 1. Analysis Tasks (Enhanced)
**Characteristics**: Investigation, research, evaluation
**Pattern**:
```
1. Information Gathering
   - Validate source availability
   - Check data accessibility
   - Handle missing information gracefully
2. Analysis & Evaluation
   - Cross-validate findings
   - Handle contradictory data
   - Identify uncertainty levels
3. Synthesis & Reporting
   - Address knowledge gaps
   - Provide confidence levels
   - Suggest further research if needed
4. Recommendations
   - Validate recommendation feasibility
   - Consider resource constraints
   - Provide fallback options
```
**Duration**: 2-4 hours
**Dependencies**: Sequential with validation points
**Error Handling**: Missing data → Use estimates & flag uncertainty

### 2. Design Tasks (Enhanced)
**Characteristics**: Architecture, planning, specification
**Pattern**:
```
1. Requirements Analysis
   - Validate requirements completeness
   - Identify missing requirements
   - Handle conflicting requirements
   - Engage stakeholders for clarification
2. High-Level Design
   - Multiple design options
   - Trade-off analysis
   - Risk assessment
   - Fallback designs for critical risks
3. Detailed Design
   - Technical feasibility checks
   - Resource requirement validation
   - Integration compatibility checks
   - Alternative approaches for blockers
4. Review & Validation
   - Stakeholder feedback loops
   - Design iteration handling
   - Acceptance criteria validation
```
**Duration**: 4-8 hours
**Dependencies**: Sequential with feedback loops
**Error Handling**: Conflicts → Trade-off analysis, Stakeholder engagement

### 3. Implementation Tasks (Enhanced)
**Characteristics**: Development, coding, building
**Pattern**:
```
1. Core Implementation
   - Progress milestone validation
   - Technical risk identification
   - Alternative approaches for blockers
   - Incremental delivery strategy
2. Supporting Components (parallel when possible)
   - Dependency validation
   - Integration testing checkpoints
   - Resource allocation adjustments
3. Integration Testing
   - Test environment setup
   - Test case validation
   - Bug triage and prioritization
   - Rollback planning
4. Documentation
   - Progress documentation
   - Knowledge transfer planning
   - Maintenance documentation
```
**Duration**: 6-12 hours
**Dependencies**: Mixed sequential/parallel with checkpoints
**Error Handling**: Technical blockers → Alternative approaches, Risk mitigation

### 4. Testing Tasks (Enhanced)
**Characteristics**: Validation, verification, quality assurance
**Pattern**:
```
1. Test Planning
   - Risk-based test prioritization
   - Resource constraint consideration
   - Test environment validation
   - Fallback testing strategies
2. Test Environment Setup
   - Environment validation
   - Data preparation
   - Tool availability checks
   - Alternative environments for failures
3. Test Execution (parallel by type with coordination)
   - Test execution monitoring
   - Result validation
   - Defect triage and management
   - Regression testing planning
4. Results Analysis
   - Quality metrics calculation
   - Risk assessment
   - Release readiness evaluation
   - Post-launch monitoring plan
```
**Duration**: 3-6 hours
**Dependencies**: Mixed with parallel execution and coordination
**Error Handling**: Environment issues → Alternative environments, Tool problems

### 5. Optimization Tasks (Enhanced)
**Characteristics**: Performance, efficiency, improvement
**Pattern**:
```
1. Performance Analysis
   - Baseline measurement
   - Bottleneck identification
   - Root cause analysis
   - Measurement validation
2. Bottleneck Identification
   - Multiple analysis techniques
   - Cross-validation of findings
   - Prioritization based on impact
3. Optimization Implementation
   - Incremental improvements
   - A/B testing setup
   - Rollback capabilities
   - Impact measurement
4. Validation & Measurement
   - Before/after comparison
   - Statistical significance testing
   - Long-term monitoring
   - Continuous optimization planning
```
**Duration**: 5-10 hours
**Dependencies**: Sequential with iterative refinement
**Error Handling**: Optimization failures → Rollback, Alternative approaches

## Emergency Planning Patterns

### Minimal Viable Plan
```
When resources are extremely limited:
1. Core Requirement Only (skip nice-to-haves)
2. Single Agent Assignment
3. Basic Validation Only
4. Essential Documentation
5. Minimal Testing Strategy
```

### Crisis Response Plan
```
When critical issues arise:
1. Immediate Risk Assessment
2. Stabilization Actions First
3. Communication Protocols
4. Recovery Planning
5. Post-Crisis Analysis
```

### Resource Constraint Adaptation
```
When facing resource limitations:
1. Prioritize Critical Path Only
2. Combine Related Subtasks
3. Extend Timelines Appropriately
4. Increase Quality Gates
5. Stakeholder Communication
```

## Execution Strategies

### 1. Sequential Strategy
- **Best for**: Simple tasks, strong dependencies
- **Pattern**: Complete one subtask before starting next
- **Advantage**: Clear progress, easy tracking
- **Disadvantage**: Longer total duration

### 2. Parallel Strategy  
- **Best for**: Independent subtasks, resource availability
- **Pattern**: Execute compatible subtasks simultaneously
- **Advantage**: Faster completion
- **Disadvantage**: Complex coordination

### 3. Mixed Strategy
- **Best for**: Complex projects with mixed dependencies
- **Pattern**: Sequential phases with parallel subtasks
- **Advantage**: Optimal balance
- **Disadvantage**: Requires careful planning

## Quality Assurance Patterns

### Review Points
- **After requirements analysis**
- **After design completion**  
- **Before implementation**
- **Before delivery**

### Validation Criteria
- Requirements completeness
- Design feasibility
- Implementation correctness
- Performance requirements met

### Documentation Requirements
- Task definition and scope
- Design decisions and rationale
- Implementation approach
- Test results and validation
