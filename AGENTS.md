# LLM Agent Orchestrator Configuration

component:
  name: "llm_agent_orchestrator"
  version: "2.0.0"
  description: "Optimized instruction format for LLM agent orchestrator coordinating specialized subagents"
  category: "coordination"
  priority: 1
  status: "stable"

language_standards:
  user_communication: "Ukrainian"
  code_documentation: "English"

project_objectives:
  primary_goal: "Create optimized instructions for LLM agent orchestrator"
  key_tasks:
- task_complexity_analysis
    - executor_optimization
    - dependency_aware_sequencing
    - effective_coordination

  work_environment:
    primary_file: "agents/master.md"
    scope_limitation: "single_file_only"
    architecture_type: "conceptual_description"

core_principles:
  research_and_information:
    primary_source: "web-search-prime"
    reliability_standard: "evidence_based"
    verification_required: true

  documentation_style:
    format: "natural_language_description"
    complexity_level: "human_readable"
    technical_constructions: "avoid_complex"

  component_development:
    pre_creation_check: "analyze_existing_functionality"
    uniqueness_requirement: "no_duplication"
    optimization_approach: "maximize_existing_resources"

  architectural_principles:
    paradigm: "hybrid_system"
    hybrid_components: ["event_driven", "priorities", "state_machine"]
    integration_focus: true
    scalability_planning: true

  resource_management:
    temporary_files: "immediate_deletion"
    disk_optimization: "minimize_usage"
    workspace_hygiene: "maintain_clean"

  quality_control:
    validation_frequency: "each_stage"
    pre_implementation_testing: true
    documentation_tracking: "capture_all_changes"

prohibitions:
  workspace_boundaries:
    filesystem_scope: "current_project_only"
    external_directory_access: false
    focus_area: "defined_workspace_only"

  content_creation:
    demo_code: "forbidden"
    code_comments: "functional_only"
    alternative_implementations: "forbidden"

  system_files:
    claude_md_editing: "forbidden"
    structure_preservation: "required"
    content_integrity: "maintain_original"

  documentation:
    additional_docs: "forbidden"
    usage_examples: "forbidden"
    instructional_guides: "forbidden"

  communication_style:
    marketing_language: "forbidden"
    tone_requirements: "technical_concise_professional"
    objectivity_standard: "neutral_approach"

  debug_mode:
    auto_activation: "no_queries"
    execution_priority: "highest"
    initiation: "independent_when_needed"

  technical_requirements:
    pseudocode_display: "forbidden"
    demonstrations: "forbidden"
    format_limitation: "text_only"

  configuration_constraints:
    description_field_changes: "forbidden"
    metadata_preservation: "required"
    system_consistency: "maintain"

  task_delegation:
    large_file_analysis: "task_or_delegation_only"
    independent_processing: "forbidden"
    specialized_agents: "required"

  version_control:
    commits: "logical_grouping_only"
    commit_frequency: "completed_stages_only"
    development_integrity: "maintain"

debug_mode:
  analysis_scope:
    phase_coverage: ["initialization", "execution"]
    process_mapping: "complete_flow_required"
    action_discovery: "all_possible_actions"
    transition_analysis: "state_mapping_required"

  process_analysis:
    conflict_detection: "step_conflicts_required"
    dead_end_identification: "branch_analysis_required"
    unused_element_detection: "comprehensive_scan"
    loop_detection: "logical_loops_required"

  execution_protocol:
    first_error_stop: "immediate_stop_required"
    error_description: "detailed_context_required"
    mode_transition: "validation_mode_after_error"

  requirements:
    communication_language: "Ukrainian"
    analysis_depth: "comprehensive_approach"
    rerun_requirement: "mandatory_after_fix"

validation_mode:
  activation_conditions:
    transition_source: "debug_mode"
    user_initiation: "allowed"
    objective: "hypothesis_confirmation"

  process_requirements:
    critical_analysis: "hypothesis_evaluation"
    factual_verification: "code_study_required"
    counterexample_search: "required"
    consequence_analysis: "system_impact_required"

  iterative_process:
    conclusion_formation: "new_conclusion_required"
    conclusion_verification: "re_verification_required"
    iteration_condition: "until_goal_satisfaction"

  success_criteria:
    statement_confirmation: "fact_based_required"
    code_consistency: "no_discrepancies_allowed"
    user_goal_satisfaction: "primary_requirement"

correction_search_mode:
  activation_conditions:
    confirmed_error: "validation_mode_required"
    delegation_method: "self_delegation_only"
    system_approach: "required"

  algorithm_requirements:
    variant_generation: "5_potential_solutions"
    complexity_evaluation: "each_variant_required"
    consequence_prediction: "impact_analysis_required"

  impact_validation:
    compatibility_check: "existing_functionality_required"
    risk_analysis: "system_risks_required"
    change_scale_assessment: "required"

  optimization_process:
    best_element_combination: "required"
    negative_consequence_minimization: "required"
    effectiveness_search: "optimal_approach_required"

  final_selection:
    optimal_choice: "required"
    choice_justification: "required"
    implementation_preparation: "required"

  effectiveness_verification:
    result_modeling: "required"
    functionality_validation: "no_loss_required"
    final_approval: "required"

documentation_requirements:
  format_guide: "@doc/OPTIMIZED_INSTRUCTION_FORMAT_GUIDE.md"
  mandatory_usage: true

file_handling:
  agents_master_md:
    loading_requirement: "full_content_to_memory"
    analysis_method: "memory_based_only"
    tool_restriction: "no_filesystem_tools"

  processing_protocol:
    task_reception: "load_full_file"
    subsequent_actions: "memory_based"
    search_avoidance: "file_search_forbidden"
    reading_avoidance: "filesystem_reading_forbidden"

mode_transitions:
  debug_to_validation: "after_first_error"
  validation_to_correction: "when_error_confirmed"
  correction_to_debug: "after_fix_analysis"
  validation_to_debug: "when_error_not_confirmed"

  transition_rules:
    - source: "debug"
      target: "validation"
      condition: "first_error_identified"
    - source: "validation"
      target: "correction"
      condition: "error_confirmed"
    - source: "correction"
      target: "debug"
      condition: "post_fix_analysis"
    - source: "validation"
      target: "debug"
      condition: "error_not_confirmed"

output:
  format: "structured"
  validation: true
  schema:
    configuration_result: "string"
    optimization_applied: "boolean"
    token_efficiency: "float"
    error_status: "string"

monitoring:
  enabled: true
  metrics:
    - "instruction_clarity"
    - "token_efficiency"
    - "implementation_success"
  targets:
    response_time: 1000
    clarity_score: 0.9
    efficiency_score: 0.85

integration:
  inputs:
    - "project_requirements"
    - "existing_documentation"
    - "optimization_guidelines"
  outputs:
    - "optimized_configuration"
    - "implementation_guidance"
    - "validation_results"
