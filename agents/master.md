---
name: "master"
description: "Task orchestration system with agent coordination and MCP integration"
capabilities: [
  "task-orchestration",
  "automatic-delegation",
  "agent-selection",
  "mcp-integration",
  "error-handling",
  "task-planning",
  "parallel-execution",
  "dependency-resolution",
  "configuration-management",
  "agent-discovery",
  "resource-management",
  "monitoring",
  "task-execution",
  "tool-selection",
  "fallback-strategies"
]
triggers: ["orchestrate", "delegate", "analyze", "plan", "coordinate", "manage", "parallel", "team", "multiple-agents", "clarify", "search", "research", "unclear", "help", "details", "requirements", "batch", "multiple-files", "bulk-edit", "mass-update", "parallel-files"]
tools: []
version: "0.3.3"
imports: [
  "config/core/mcp_server_discovery.yaml",
  "config/core/configuration_base.yaml",
  "config/core/error_handling_initialization.yaml",
  "config/core/monitoring_system.yaml",
  "config/core/performance_optimization.yaml",
  "config/core/system_health_check.yaml",
  "config/analysis/task_analysis.yaml",
  "config/analysis/agent_selection.yaml",
  "config/analysis/clarification.yaml",
  "config/execution/todo_engine.yaml",
  "config/execution/coordination.yaml",
  "config/execution/delegation.yaml",
  "config/discovery/agent_registry.yaml",
  "config/orchestration/batch_orchestrator.yaml",
  "config/validation/validation_rules.yaml",
  "config/template/component_template.yaml",
  "config/template/trigger_system.yaml"
]

component:
  name: "master"
  version: "0.3.3"
  description: "Task orchestration system with agent coordination and MCP integration"
  category: "orchestration"
  priority: 1
  status: "stable"
  token_optimization:
    original_tokens: 8000
    optimized_tokens: 3300
    savings_percentage: 59

triggers:
  primary:
    keywords: ["orchestrate", "delegate", "analyze", "plan", "coordinate"]
    patterns: [".*orchestrate.*", ".*delegate.*to.*", ".*coordinate.*"]
    score: 1.0
  secondary:
    keywords: ["manage", "parallel", "team", "multiple-agents", "clarify"]
    score: 0.7
  contextual:
    conditions: ["task_complexity > 2", "multi_domain_detected", "uncertainty > 0.5"]
    score: 0.5

implementation:
  operations:
    - name: "system_initialization"
      priority: 1
      method: "phase_based_bootstrapping"
      config:
        phases: [0, 1, 2, 3, 4, 5]
        parallel_init: true
        timeout: 75
        mcp_discovery: true
      output:
        system_ready: "boolean"
        components_active: "array"
        mcp_servers: "array"

    - name: "agent_discovery"
      priority: 2
      method: "dynamic_name_resolution"
      config:
        scan_filesystem: true
        category_detection: "tfidf_analysis"
        name_format: "{category}:{agent_name}"
        cache_resolution: true
      output:
        registered_agents: "array"
        name_mappings: "object"

    - name: "task_analysis"
      priority: 3
      method: "ml_categorization"
      config:
        tfidf:
          max_features: 1000
          similarity_threshold: 0.3
        complexity_scoring: true
        domain_classification: true
        uncertainty_detection: true
        adaptive_replanning: true
        pattern_analysis: true
      output:
        task_complexity: "integer"
        domain_tags: "array"
        delegation_required: "boolean"
        confidence_score: "float"
        parallel_opportunities: "array"
        batch_operations: "object"
        adaptive_replanning_needed: "boolean"
        data_collection_phase: "boolean"

    - name: "dynamic_pattern_recognition"
      priority: 3.5
      method: "adaptive_batch_analysis"
      trigger: "after_data_collection"
      config:
        pattern_detection:
          file_operations: true
          api_calls: true
          data_processing: true
          validation_tasks: true
        batch_analysis:
          similarity_threshold: 0.8
          min_batch_size: 2
          max_batch_size: 15
        cross_operation_analysis: true
        parallel_opportunity_detection: true
      output:
        parallel_opportunities: "array"
        batch_operations: "object"
        optimization_suggestions: "array"
        adaptive_replanning_needed: "boolean"

    - name: "agent_selection"
      priority: 4
      method: "semantic_matching"
      config:
        tfidf_analysis: true
        vector_similarity: true
        expertise_mapping: true
        uncertainty_quantification: true
        backup_options: true
        batch_aware_selection: true
      output:
        selected_agent: "string"
        confidence_score: "float"
        backup_options: "array"
        parallel_grouping: "object"

    - name: "todo_execution"
      priority: 5
      method: "automated_delegation"
      config:
        auto_batch_detection: true
        batch_threshold: 3
        parallel_execution: true
        circuit_breaker: true
        resource_optimization: true
        adaptive_batching: true
      output:
        execution_plan: "array"
        parallel_groups: "array"
        estimated_time: "string"
        batch_optimizations: "array"

    - name: "adaptive_replanning"
      priority: 5.5
      method: "todo_optimization"
      trigger: "on_new_patterns_discovered"
      config:
        todo_regeneration: true
        batch_formation: true
        priority_rebalancing: true
        parallel_grouping: true
        optimization_targets:
          - "parallel_execution"
          - "resource_efficiency"
          - "completion_time"
      output:
        optimized_todo_list: "array"
        new_parallel_groups: "array"
        efficiency_gains: "object"
        replanning_summary: "string"

    - name: "mcp_integration"
      priority: 6
      method: "automatic_tool_matching"
      config:
        server_discovery: true
        capability_extraction: true
        performance_profiling: true
        health_monitoring: true
        fallback_strategies: true
      output:
        available_tools: "array"
        tool_task_mapping: "object"
        server_health: "object"

dependencies:
  required:
    - component: "task_analysis"
      version: ">=1.0.0"
      reason: "Complexity assessment and categorization"
    - component: "agent_registry"
      version: ">=1.0.0"
      reason: "Dynamic agent discovery"
    - component: "mcp_server_discovery"
      version: ">=1.0.0"
      reason: "MCP tool integration"
  optional:
    - component: "performance_tracker"
      version: ">=1.0.0"
      fallback: "use_estimated_times"
    - component: "batch_orchestrator"
      version: ">=1.0.0"
      fallback: "sequential_execution"

output:
  format: "structured"
  validation: true
  schema:
    selected_agent: "string"
    execution_plan: "array"
    confidence_score: "float"
    estimated_time: "string"
    parallel_groups: "array"
    mcp_tools_required: "array"

fallback:
  enabled: true
  strategy: "graceful_degradation"
  alternatives:
    - "direct_execution"
    - "simplified_analysis"
    - "basic_delegation"
    - "native_tools_only"
  circuit_breaker: true
  retry_logic: "exponential_backoff"
  max_retries: 3

monitoring:
  enabled: true
  metrics:
    - "task_distribution_accuracy"
    - "agent_selection_success_rate"
    - "clarification_resolution_rate"
    - "system_initialization_time"
    - "mcp_server_health"
    - "batch_processing_efficiency"
    - "token_optimization_success"
  targets:
    accuracy: 0.96
    response_time: 1500
    success_rate: 0.99
    token_efficiency: 0.59

integration:
  inputs:
    - "user_task_description"
    - "agent_registry"
    - "mcp_server_capabilities"
    - "system_context"
    - "operation_patterns"
    - "batch_analysis_results"
  outputs:
    - "delegation_instructions"
    - "execution_summary"
    - "performance_metrics"
    - "token_usage_report"
    - "optimization_recommendations"
  events:
    subscribe:
      - "task_orchestration_requested"
      - "data_collection_completed"
      - "parallel_opportunities_detected"
      - "batch_analysis_ready"
    publish:
      - "orchestration_complete"
      - "adaptive_replanning_triggered"
      - "parallel_groups_formed"
      - "optimization_applied"

performance_optimization:
  token_efficiency:
    enabled: true
    target_reduction: 0.59
    techniques: ["flat_hierarchy", "parameter_grouping", "concise_descriptions"]
  parallel_processing:
    batch_threshold: 3
    max_concurrent: 10
    resource_allocation: "dynamic"
  adaptive_batching:
    enabled: true
    pattern_recognition: true
    cross_operation_analysis: true
    dynamic_todo_regeneration: true
    similarity_threshold: 0.8
    auto_optimization: true
  caching:
    agent_resolution: true
    mcp_capabilities: true
    task_analysis_results: true
    pattern_cache: true
    batch_analysis_cache: true

quality_assurance:
  validation_rules:
    - "yaml_structure_valid"
    - "required_components_present"
    - "token_efficiency_achieved"
    - "functionality_preserved"
  testing_required:
    - "agent_selection_accuracy"
    - "mcp_integration_stability"
    - "fallback_mechanisms"
    - "parallel_execution_reliability"
