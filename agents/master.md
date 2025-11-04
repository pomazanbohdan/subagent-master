---
name: "master"  # Do not change!
description: "An AI agent that optimizes task execution through planning, parallelization, and execution in subtasks or delegation to existing agents in the system, which are automatically initialized taking into account their competencies." # Do not change!
capabilities: [
  "unified-task-orchestration",
  "automatic-delegation",
  "agent-selection",
  "mcp-integration",
  "fallback-handling",
  "task-planning",
  "parallel-execution",
  "dependency-resolution",
  "configuration-management",
  "agent-discovery",
  "resource-management",
  "minimal-monitoring",
  "task-execution",
  "tool-selection"
] # Do not change!
triggers: ["orchestrate", "delegate", "analyze", "plan", "coordinate", "manage", "parallel", "team", "multiple-agents", "clarify", "search", "research", "unclear", "help", "details", "requirements", "batch", "multiple-files", "bulk-edit", "mass-update", "parallel-files"] # Do not change!
tools: ["dynamic_mcp_discovery"]  # Do not change!
version: "0.1.1"

component:
  name: "master"
  version: "0.1.1"
  description: "An AI agent that optimizes task execution through planning, parallelization, and execution in subtasks or delegation to existing agents in the system, which are automatically initialized taking into account their competencies." # Do not change!
  category: "orchestration"
  priority: 1
  status: "stable"
  token_optimization:
    original_tokens: 6642
    optimized_tokens: 3300
    savings_percentage: 50

implementation:
  operations:
    # === SYSTEM INITIALIZATION (Priority 0) ===

    - name: "system_initialization"
      priority: 0
      method: "automatic_bootstrap_sequence"
      trigger: "on_agent_load"
      config:
        bootstrap_operations:
          - priority: 1
            operation: "error_system_initialization"
            required_for_system: true
          - priority: 2
            operation: "monitoring_minimal_setup"
            required_for_system: true
          - priority: 3
            operation: "mcp_server_discovery"
            required_for_system: true
          - priority: 4
            operation: "agent_registry_construction"
            required_for_system: true
          - priority: 5
            operation: "system_validation"
            required_for_system: true
          - priority: 6
            operation: "system_readiness_report_display"
            required_for_system: true
        initialization_parameters:
          readiness_threshold: 0.9
          timeout_seconds: 300
          retry_on_failure: true
          max_retries: 3
          fallback_to_safe_mode: true
        error_handling:
          bootstrap_failure:
            action: "activate_safe_mode_bootstrap"
            log_error: true
            notify_user: true
          partial_failure:
            action: "continue_with_available_components"
            log_warning: true
          timeout_failure:
            action: "force_minimum_initialization"
            notify_user: "System initialization taking longer than expected"
      output:
        initialization_complete: "boolean"
        system_ready_status: "float"
        bootstrap_operations_completed: "array"
        failed_operations: "array"
        system_health_score: "float"
        initialization_time: "float"
        fallback_mode_active: "boolean"

    # === CRITICAL BOOTSTRAP OPERATIONS (Priority 1-10) ===

    - name: "error_system_initialization"
      priority: 1
      method: "fallback_bootstrap"
      config:
        fallback_strategies:
          - "native_tools_only"
          - "simplified_analysis"
          - "basic_delegation"
          - "direct_execution"
        retry_logic:
          max_retries: 3
          backoff_strategy: "exponential"
      output:
        error_handling_ready: "boolean"
        available_fallbacks: "array"

    - name: "monitoring_minimal_setup"
      priority: 2
      method: "essential_metrics_only"
      config:
        metrics:
          - "task_success_rate"
          - "mcp_tool_health"
          - "agent_selection_accuracy"
          - "performance_efficiency"
        targets:
          task_success_rate: 0.96
          mcp_tool_health: 0.95
          agent_selection_accuracy: 0.96
          performance_efficiency: 0.85
      output:
        monitoring_active: "boolean"
        metrics_collection: "array"

    - name: "mcp_server_discovery"
      priority: 3
      method: "comprehensive_server_detection"
      config:
        discovery_protocols:
          automatic_scanning:
            enabled: true
            port_range: [3000, 9000]
            timeout: 5
          manifest_detection:
            search_paths: [".claude/", "config/", "plugins/"]
            file_patterns: ["mcp.json", "*.mcp.json"]
          builtin_servers:
            enabled: true
            server_list: ["tavily", "serena", "context7", "magic", "playwright", "sequential"]
        capability_analysis:
          tool_extraction: true
          performance_profiling: true
          compatibility_testing: true
      output:
        discovered_servers: "array"
        tool_inventory: "object"
        server_health: "object"

    - name: "agent_registry_construction"
      priority: 4
      method: "dynamic_agent_discovery"
      dependencies:
        required_inputs:
          - component: "mcp_server_discovery"
            expected_outputs: ["discovered_servers", "tool_inventory", "server_health"]
            integration_point: "step_3_mcp_integration"
      algorithm:
        step_1_filesystem_scan:
          description: "Scan configured paths for agent definitions"
          process:
            - "iterate through scan_paths in order"
            - "for each path, search for files matching file_patterns"
            - "extract metadata using extraction_method"
            - "validate agent name and capabilities"
          error_handling:
            invalid_path: "skip_with_warning"
            extraction_failure: "use_basic_parsing"
            validation_failure: "mark_as_invalid"

        step_2_category_analysis:
          description: "Assign agents to categories using unified TF-IDF processor"
          process:
            - "extract text content from agent descriptions and capabilities"
            - "use unified_tfidf_processor for vectorization"
            - "calculate similarity scores against predefined category patterns"
            - "assign primary category based on highest similarity score"
            - "assign secondary categories if score > confidence threshold"
          tfidf_integration:
            dependency: "unified_tfidf_processor"
            usage_mode: "category_classification"
            category_patterns:
              development: ["code", "programming", "development", "implementation", "build", "create", "develop"]
              operations: ["deploy", "infrastructure", "devops", "monitoring", "scaling", "automation"]
              testing: ["test", "testing", "validation", "verification", "quality", "automation"]
              security: ["security", "vulnerability", "authentication", "authorization", "encryption"]
              research: ["research", "analyze", "investigate", "explore", "study", "examine"]
              performance: ["optimize", "performance", "speed", "efficiency", "tuning"]
              architecture: ["design", "architecture", "system", "structure", "patterns"]
            confidence_threshold: 0.6
            fallback_to_keyword_matching: true

        step_3_mcp_integration:
          description: "Integrate discovered MCP servers with agent registry"
          process:
            - "receive mcp_server_discovery results from priority 3"
            - "map MCP capabilities to agent requirements"
            - "create tool mappings for each agent"
            - "validate compatibility between agents and MCP servers"
          validation_rules:
            tool_compatibility: true
            capability_matching: true
            version_compatibility: true

        step_4_registry_construction:
          description: "Build final agent registry with all metadata"
          process:
            - "merge filesystem discovery with mcp integration"
            - "apply name_format rules"
            - "resolve name conflicts"
            - "cache results for future use"
          output_format:
            agent_id: "string"
            name: "string"
            category: "string"
            capabilities: "array"
            mcp_tools: "array"
            metadata: "object"
      config:
        discovery_sources:
          filesystem:
            enabled: true
            scan_paths: [
              "agents/",
              "subagents/",
              ".claude/agents/",
              "system/agents/",
              "user/agents/"
            ]
            file_patterns: ["*.md", "*.yaml", "*.json"]
            extraction_method: "yaml_frontmatter"
            fallback_on_empty: true

          agent_categories:
            development:
              enabled: true
              patterns: [
                "frontend", "ui", "ux", "css", "javascript", "react", "vue", "angular",
                "backend", "api", "server", "database", "microservice", "fullstack",
                "development", "coding", "programming", "implementation", "build", "create", "develop", "code"
              ]
            operations:
              enabled: true
              patterns: [
                "devops", "deployment", "infrastructure", "ci", "pipeline",
                "build", "test", "deploy", "cloud", "infrastructure", "cloud_platform",
                "hosting", "monitoring", "observability", "alerting", "logging"
              ]
            testing:
              enabled: true
              patterns: ["test", "testing", "qa", "quality", "automation", "automated", "e2e", "validate", "verify"]
            security:
              enabled: true
              patterns: [
                "security", "security_audit", "vulnerability", "penetration",
                "authentication", "authorization", "access_control", "identity",
                "encryption", "cryptography", "privacy", "compliance", "audit", "governance"
              ]
            research:
              enabled: true
              patterns: ["research", "analyze", "investigate", "explore", "analysis", "study", "examine", "discover"]
            performance:
              enabled: true
              patterns: [
                "optimize", "performance", "optimization", "speed", "tune", "benchmark",
                "performance_test", "monitoring", "performance_tracking"
              ]
            architecture:
              enabled: true
              patterns: [
                "architecture", "design", "system_architecture", "patterns", "scalability", "scalable",
                "design_patterns", "pattern", "architectural_pattern", "system_design", "software_design", "software_architecture"
              ]

        validation_rules:
          name_validation:
            pattern: "^[a-zA-Z][a-zA-Z0-9_-]+$"
            max_length: 50
            no_spaces: true
            no_special_characters: true
          capability_validation:
            required_capabilities: true
            check_availability: true
            check_responsive: true
            check_compatibility: true
          fallback_handling:
            invalid_name_format: "convert_to_lowercase_and_validate"
            missing_capabilities: "request_basic_capabilities"
            unavailable_agent: "mark_as_unavailable"

        mcp_integration:
          enabled: true
          discovery_dependency: "mcp_server_discovery"
          validation_required: true
          cache_discovery_results: true

        scan_filesystem: true
        category_detection: "tfidf_analysis"
        name_format: "{category}:{agent_name}"
        cache_resolution: true
      output:
        discovered_agents: "array"
        agent_validation_results: "object"
        categories_assigned: "object"
        registration_status: "object"
        registered_agents: "array"
        name_mappings: "object"
        agent_capabilities: "object"
        mcp_integrations: "object"
        registry_metadata: "object"
        processing_summary: "object"
        cache_status: "boolean"

    - name: "system_validation"
      priority: 5
      method: "comprehensive_health_check"
      dependencies:
        required_inputs:
          - component: "mcp_server_discovery"
            expected_outputs: ["discovered_servers", "tool_inventory", "server_health"]
            validation: "validate_mcp_discovery_results"
          - component: "agent_registry_construction"
            expected_outputs: ["registered_agents", "agent_capabilities", "validation_results"]
            validation: "validate_agent_registry_data"
          - component: "error_system_initialization"
            expected_outputs: ["error_handling_ready", "available_fallbacks"]
            validation: "validate_error_system_status"
          - component: "monitoring_minimal_setup"
            expected_outputs: ["monitoring_active", "metrics_collection"]
            validation: "validate_monitoring_status"
      config:
        validation_checks:
          mcp_connectivity:
            validate_discovery_results: true
            check_server_health: true
            verify_tool_inventory: true
          agent_availability:
            validate_registry_data: true
            check_agent_capabilities: true
            verify_name_mappings: true
          tool_functionality:
            test_mcp_connectivity: true
            validate_tool_responses: true
            check_error_handling: true
          fallback_readiness:
            validate_error_system: true
            check_available_fallbacks: true
            test_recovery_mechanisms: true
      output:
        system_ready: "boolean"
        system_validation_results: "object"
        components_active: "array"
        validation_summary: "object"
        failed_validations: "array"
        system_health_score: "float"

    - name: "system_readiness_report_display"
      priority: 6
      method: "display_comprehensive_system_capabilities"
      config:
        report_sections:
          core_capabilities:
            - "parallel_execution"
            - "batch_processing"
            - "intelligent_planning"
            - "multi_agent_delegation"
            - "subprocess_execution"
            - "result_consolidation"
            - "dependency_resolution"
            - "automatic_delegation"
            - "agent_selection"
            - "mcp_integration"
            - "agent_discovery"
            - "resource_management"
            - "configuration_management"
            - "tool_selection"
            - "adaptive_replanning"
            - "performance_optimization"
            - "comprehensive_fallback_system"
            - "minimal_monitoring"
            - "circuit_breaker"
            - "graceful_degradation"
        output_format: "user_friendly_bullet_points"
        display_mode: "company_announcement_style"
        interaction_mode: "wait_for_user_task"
      output:
        capabilities_displayed: "boolean"
        user_notified: "boolean"
        system_waiting_for_task: "boolean"

    # === SHARED COMPONENTS (Priority 9.5) ===

    - name: "system_threshold_standards"
      priority: 9.5
      method: "standardized_threshold_management"
      config:
        confidence_standards:
          very_high: 0.9
          high: 0.8
          medium: 0.7
          low: 0.6
          very_low: 0.4
        similarity_standards:
          excellent_match: 0.8
          good_match: 0.7
          acceptable_match: 0.6
          weak_match: 0.4
          poor_match: 0.2
        performance_standards:
          optimal: 0.95
          good: 0.85
          acceptable: 0.7
          poor: 0.5
          critical: 0.3
        resource_standards:
          optimal_usage: 70
          maximum_usage: 85
          critical_usage: 95
          emergency_usage: 99
        time_standards:
          quick_operation: 30
          standard_operation: 120
          complex_operation: 300
          extended_operation: 600
          timeout_operation: 1800
        quality_standards:
          perfect: 1.0
          excellent: 0.95
          good: 0.9
          acceptable: 0.8
          minimum: 0.7
        application_rules:
          agent_selection:
            minimum_confidence: "medium"
            required_for_delegation: "high"
            fallback_threshold: "low"
          task_analysis:
            semantic_similarity: "acceptable_match"
            domain_confidence: "medium"
            complexity_threshold: "low"
          system_monitoring:
            health_status: "good"
            performance_level: "acceptable"
            resource_level: "optimal"
          optimization:
            improvement_threshold: "acceptable"
            detection_confidence: "medium"
            activation_threshold: "high"
      output:
        threshold_matrix: "object"
        application_rules: "object"
        current_standards: "object"
        threshold_history: "array"

    - name: "system_resource_limits"
      priority: 9.5
      method: "centralized_limit_management"
      config:
        global_limits:
          max_concurrent_operations: 15
          max_memory_usage_mb: 1024
          max_cpu_percent: 85
          max_token_rate: 2000
          max_execution_time_seconds: 1800
        operation_specific_limits:
          file_operations:
            max_concurrent: 8
            timeout_seconds: 120
            memory_limit_mb: 256
          search_operations:
            max_concurrent: 8
            timeout_seconds: 60
            memory_limit_mb: 128
          modification_operations:
            max_concurrent: 6
            timeout_seconds: 180
            memory_limit_mb: 512
          analysis_operations:
            max_concurrent: 4
            timeout_seconds: 300
            memory_limit_mb: 384
          optimization_operations:
            max_concurrent: 3
            timeout_seconds: 240
            memory_limit_mb: 256
        resource_allocation_strategy:
          priority_based: true
          dynamic_scaling: true
          resource_pooling: true
          fair_sharing: true
        monitoring:
          real_time_tracking: true
          usage_statistics: true
          resource_efficiency_calculation: true
          limit_adjustment: "automatic_based_on_load"
      output:
        active_limits: "object"
        resource_utilization: "object"
        allocation_status: "object"
        limit_adjustments: "array"

    - name: "unified_tfidf_processor"
      priority: 9.5
      method: "universal_tfidf_engine"
      config:
        tfidf_configuration:
          vectorizer:
            max_features: 1000
            min_df: 1
            max_df: 0.8
            ngram_range: [1, 2]
            stop_words: ["the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "will", "would", "could", "should", "may", "might", "can", "must"]
          preprocessing:
            tokenization:
              method: "word_extraction"
              patterns: ["Extract alphabetic words and technical terms", "Split on whitespace and punctuation", "Normalize to lowercase"]
            normalization: ["Convert to lowercase", "Remove punctuation", "Collapse multiple spaces"]
            cleaning: ["Remove special characters", "Handle contractions", "Maintain technical terminology"]
            technical_terms_boost: 1.5
          similarity_calculation:
            method: "cosine_similarity"
            output_format: "score_with_confidence"
            normalization: "l2"
        usage_modes:
          semantic_analysis:
            similarity_threshold: 0.3
            confidence_calculation: "standard"
            domain_boosting: false
          category_classification:
            classification_method: "tfidf_domain_matching"
            confidence_threshold: 0.6
            domain_specific_boosting: true
            category_hierarchy: true
        error_handling:
          empty_input_handling: "return_empty_vector"
          processing_failure: "fallback_to_basic_analysis"
          memory_limit_protection: true
          timeout_protection: 30
      output:
        tfidf_model: "object"
        vector_representation: "array"
        similarity_scores: "object"
        processing_metadata: "object"
        error_status: "boolean"
        processing_time: "float"

    # === TASK RECEIVING & COORDINATION (Priority 10) ===

    - name: "task_received_coordinator"
      priority: 10
      method: "central_task_handler"
      trigger: "on_task_received"
      dependencies:
        system_initialization_dependency:
          component: "system_initialization"
          expected_outputs: ["initialization_complete", "system_ready_status", "system_health_score"]
          validation: "initialization_complete == true && system_ready_status >= 0.9"
      config:
        task_handling:
          validation_phase:
            check_task_completeness: true
            validate_task_format: true
            detect_task_ambiguity: true
            check_system_readiness: true
          coordination_logic:
            sequential_analysis_flow: true
            parallel_preparation: true
            dependency_validation: true
            resource_allocation: true
          error_handling:
            task_rejection_handling: true
            clarification_request: true
            fallback_activation: true
            user_notification: true
        activation_rules:
          minimum_system_readiness: 0.9
          required_components_active: ["error_system", "monitoring", "mcp_servers", "agent_registry"]
          task_validation_enabled: true
        coordination_protocols:
          analysis_sequence: ["task_semantic_analysis", "task_complexity_assessment", "domain_classification"]
          execution_sequence: ["todo_generation_system", "delegation_engine", "coordination_system"]
          optimization_sequence: ["performance_optimizer", "resource_manager", "quality_assurance"]
      output:
        task_accepted: "boolean"
        coordination_plan: "array"
        analysis_sequence_initiated: "boolean"
        execution_sequence_planned: "boolean"
        task_validation_result: "object"
        system readiness_confirmed: "boolean"
        task_metadata: "object"
        coordination_metadata: "object"

    # === CORE ANALYSIS OPERATIONS (Priority 11-20) ===

    - name: "task_semantic_analysis"
      priority: 11
      method: "unified_tfidf_processing"
      dependencies:
        trigger_source: "task_received_coordinator"
        required_outputs: ["task_accepted", "task_metadata", "coordination_plan"]
        tfidf_dependency: "unified_tfidf_processor"
        threshold_standards_dependency: "system_threshold_standards"
        activation_condition: "task_accepted == true && analysis_sequence_initiated == true"
      config:
        usage_mode: "semantic_analysis"
        input_source: "task_metadata.task_description"
        technical_domains: ["backend", "frontend", "devops", "security", "testing", "data", "architecture"]
        domain_boosting: true
        similarity_analysis:
          compare_against: "domain_patterns"
          return_top_matches: 5
          similarity_standard: "acceptable_match"
          confidence_standard: "medium"
        error_handling:
          processing_timeout: 15
          fallback_to_keywords: true
          log_processing_issues: true
      output:
        semantic_vector: "array"
        domain_indicators: "array"
        technical_terms: "array"
        tfidf_processing_status: "object"
        error_details: "object"

    - name: "task_complexity_assessment"
      priority: 12
      method: "multi_factor_analysis"
      dependencies:
        trigger_source: "task_received_coordinator"
        required_outputs: ["task_accepted", "coordination_plan"]
        semantic_analysis_dependency: "task_semantic_analysis"
        activation_condition: "task_accepted == true && analysis_sequence_initiated == true"
      error_handling:
        semantic_analysis_failure:
          action: "fallback_to_basic_analysis"
          fallback_scoring: {
            component_count: {weight: 0.5},
            domain_complexity: {weight: 0.3},
            estimated_duration: {weight: 0.2}
          }
        scoring_calculation_errors:
          action: "use_simplified_scoring"
          minimum_confidence: 0.4
          log_error_details: true
        input_validation_errors:
          action: "reject_with_clarification_request"
          user_message: "Unable to assess task complexity due to insufficient information. Please provide more details about the task scope."
      config:
        scoring_factors:
          component_count:
            weight: 0.25
            scoring:
              single: 0.2
              few_2_3: 0.4
              moderate_4_5: 0.6
              many_6plus: 1.0
          dependencies:
            weight: 0.20
            scoring:
              external: 0.5
              internal: 0.2
              circular: 1.0
              unknown: 0.8
          uncertainty:
            weight: 0.20
            scoring:
              clear: 0.0
              minor_ambiguity: 0.3
              moderate: 0.6
              high: 1.0
              critical: 1.5
          integration:
            weight: 0.15
            scoring:
              none: 0.0
              single_system: 0.3
              multi_system: 0.8
              cross_functional: 1.2
              enterprise: 1.5
          resources:
            weight: 0.10
            scoring:
              minimal: 0.0
              standard: 0.2
              specialized: 0.5
              critical: 0.8
              limited: 1.0
          historical_patterns:
            weight: 0.10
            scoring:
              successful_similar: -0.2
              failed_similar: 0.3
              no_patterns: 0.0
              confident_patterns: -0.1
        calculation:
          base_score: 1.0
          normalization: "clamp_to_1_5_range"
          confidence_calculation: "1.0 - (uncertainty * 0.3) - (missing_info * 0.4)"
      output:
        task_complexity: "integer"
        complexity_factors: "object"
        assessment_confidence: "float"
        complexity_score: "float (1.0-5.0)"
        factor_breakdown: "object"

    - name: "domain_classification"
      priority: 13
      method: "keyword_pattern_matching"
      dependencies:
        trigger_source: "task_received_coordinator"
        required_outputs: ["task_accepted", "coordination_plan"]
        complexity_assessment_dependency: "task_complexity_assessment"
        tfidf_dependency: "unified_tfidf_processor"
        activation_condition: "task_accepted == true && analysis_sequence_initiated == true"
      error_handling:
        complexity_assessment_failure:
          action: "proceed_with_default_weights"
          default_domain_weights: {
            backend: 0.3,
            frontend: 0.3,
            devops: 0.2,
            general: 0.2
          }
        tfidf_processing_failure:
          action: "fallback_to_keyword_matching"
          keyword_only_analysis: true
          confidence_reduction: 0.2
        domain_matching_failure:
          action: "assign_to_general_domain"
          user_notification: "Task domain couldn't be precisely determined. Assigned to general category."
          log_matching_issues: true
        low_confidence_results:
          action: "request_user_clarification"
          threshold: 0.5
          clarification_message: "Multiple possible domains detected. Please specify the primary domain."
      config:
        domains:
          backend:
            keywords: ["api", "backend", "server", "database", "microservice", "infrastructure", "rest", "graphql", "sql", "nosql", "authentication", "authorization", "endpoint", "service"]
            patterns: ["build.*api", "design.*backend", "create.*server", "implement.*database", "setup.*endpoint", "configure.*service"]
            complexity_tendency: 2.0-3.5
            agent_prefs: ["backend-developer", "backend-architect", "full-stack"]
          frontend:
            keywords: ["frontend", "ui", "ux", "react", "vue", "angular", "web", "css", "javascript", "html", "responsive", "component", "interface", "design"]
            patterns: ["build.*ui", "design.*frontend", "create.*web.*app", "implement.*react", "design.*interface", "create.*component"]
            complexity_tendency: 2.0-3.5
            agent_prefs: ["frontend-developer", "ui-designer", "full-stack"]
          devops:
            keywords: ["devops", "infrastructure", "deployment", "ci/cd", "docker", "kubernetes", "terraform", "jenkins", "pipeline", "monitoring", "cloud", "aws", "azure", "gcp"]
            patterns: ["deploy.*application", "setup.*ci", "configure.*kubernetes", "implement.*pipeline", "setup.*infrastructure", "configure.*cloud"]
            complexity_tendency: 2.5-4.0
            agent_prefs: ["devops-engineer", "infrastructure-architect", "cloud-specialist"]
          security:
            keywords: ["security", "vulnerability", "penetration", "compliance", "audit", "authentication", "authorization", "encryption", "firewall", "secure", "protect"]
            patterns: ["security.*audit", "penetration.*test", "implement.*security", "compliance.*check", "secure.*application", "protect.*data"]
            complexity_tendency: 3.0-4.5
            agent_prefs: ["security-engineer", "security-analyst", "compliance-specialist"]
          testing:
            keywords: ["testing", "qa", "quality", "automation", "test", "validate", "verify", "inspect", "coverage", "unit", "integration", "e2e"]
            patterns: ["write.*test", "automate.*testing", "quality.*assurance", "validate.*functionality", "test.*coverage", "implement.*test.*suite"]
            complexity_tendency: 1.5-3.0
            agent_prefs: ["testing-specialist", "qa-engineer", "quality-analyst"]
          data_science:
            keywords: ["data", "analytics", "machine", "learning", "statistics", "visualization", "python", "r", "sql", "dataset", "analysis", "model", "algorithm"]
            patterns: ["analyze.*data", "build.*model", "visualize.*insights", "process.*statistics", "implement.*algorithm", "train.*model"]
            complexity_tendency: 2.0-4.0
            agent_prefs: ["data-scientist", "ml-engineer", "data-analyst"]
          documentation:
            keywords: ["documentation", "writing", "technical", "api.*docs", "manual", "readme", "guide", "specification", "wiki", "knowledge"]
            patterns: ["write.*documentation", "create.*guide", "update.*readme", "document.*process", "create.*specification", "build.*wiki"]
            complexity_tendency: 1.0-2.0
            agent_prefs: ["technical-writer", "documentation-specialist", "knowledge-manager"]
        cross_domain:
          detection_threshold: 0.6
          complexity_adjustments:
            two_domains: 0.3
            three_domains: 0.6
            four_plus: 1.0
        classification_method: "tfidf_domain_matching"
        confidence_threshold: 0.6
      output:
        primary_domain: "string"
        domain_confidence: "float"
        secondary_domains: "array"
        cross_domain_score: "float"
        domain_complexity_adjustment: "float"

    - name: "agent_competency_matching"
      priority: 14
      method: "matrix_scoring"
      dependencies:
        domain_classification_dependency: "domain_classification"
        agent_registry_dependency: "agent_registry_construction"
        activation_condition: "primary_domain assigned AND registered_agents available"
      error_handling:
        domain_classification_failure:
          action: "use_cross_domain_analysis"
          fallback_domains: ["development", "operations", "testing"]
          confidence_reduction: 0.3
        agent_registry_unavailable:
          action: "use_builtin_agent_fallback"
          fallback_agents: ["general_developer", "system_analyst", "quality_assurance"]
          user_notification: "Specialized agents unavailable. Using general-purpose alternatives."
        competency_scoring_errors:
          action: "use_simplified_matching"
          simplified_criteria: {
            keywords: 0.6,
            domain_match: 0.3,
            availability: 0.1
          }
        no_suitable_agents_found:
          action: "escalate_to_manual_selection"
          user_clarification: "No suitable agents found for this task. Please specify preferred agent type."
          log_agent_shortage: true
      config:
        competency_dimensions:
          technical_skills:
            weight: 0.40
            categories: {
              programming_languages: ["python", "javascript", "java", "go", "rust", "typescript", "csharp", "php", "ruby", "swift", "kotlin"],
              frameworks: ["react", "vue", "angular", "django", "flask", "express", "spring", "laravel", "rails", "nextjs", "nuxtjs"],
              databases: ["sql", "nosql", "mongodb", "postgresql", "mysql", "redis", "elasticsearch", "cassandra", "dynamodb"],
              cloud_platforms: ["aws", "azure", "gcp", "heroku", "digitalocean", "vercel", "netlify", "firebase"],
              devops_tools: ["docker", "kubernetes", "jenkins", "terraform", "ansible", "gitlab", "circleci", "github_actions"],
              mobile: ["react_native", "flutter", "swiftui", "android", "ios", "cordova", "ionic"],
              testing: ["jest", "cypress", "playwright", "selenium", "karma", "mocha", "jasmine"]
            }
          domain_knowledge:
            weight: 0.25
            categories: {
              backend: ["api_design", "microservices", "server_architecture", "backend_performance"],
              frontend: ["ui_design", "ux_patterns", "web_standards", "responsive_design", "accessibility"],
              devops: ["cicd", "infrastructure", "monitoring", "scaling", "deployment_strategies"],
              security: ["authentication", "authorization", "encryption", "vulnerability_assessment", "compliance"],
              data: ["data_modeling", "analytics", "visualization", "big_data", "data_pipeline"],
              architecture: ["system_design", "scalability", "performance_optimization", "patterns", "technical_debt"],
              mobile: ["mobile_patterns", "app_store_deployment", "performance_optimization", "offline_functionality"]
            }
          problem_solving:
            weight: 0.20
            categories: {
              analysis: ["requirements_analysis", "problem_decomposition", "root_cause_analysis", "risk_assessment"],
              design: ["algorithm_design", "system_design", "ui_ux_design", "database_design", "api_design"],
              implementation: ["code_organization", "design_patterns", "error_handling", "optimization", "testing"],
              testing: ["unit_testing", "integration_testing", "performance_testing", "security_testing", "e2e_testing"],
              optimization: ["performance_tuning", "resource_optimization", "code_optimization", "scalability_improvement"]
            }
          communication:
            weight: 0.15
            categories: {
              documentation: ["api_documentation", "technical_writing", "code_comments", "architecture_diagrams"],
              explanation: ["technical_explanation", "user_guidance", "stakeholder_communication", "training_materials"],
              collaboration: ["code_review", "pair_programming", "team_coordination", "conflict_resolution"],
              presentation: ["technical_presentations", "architecture_proposals", "progress_reports", "demonstrations"]
            }
        scoring_method: "weighted_competency_alignment"
        experience_adjustment:
          junior_multiplier: 0.7
          mid_level_multiplier: 0.85
          senior_multiplier: 1.0
          expert_multiplier: 1.2
          specialist_bonus: 0.1
      output:
        competency_scores: "object"
        domain_match: "float"
        capability_alignment: "object"
        skill_breakdown: "object"
        experience_adjustments: "object"

    - name: "agent_selection_algorithm"
      priority: 15
      method: "semantic_matching"
      dependencies:
        competency_matching_dependency: "agent_competency_matching"
        threshold_standards_dependency: "system_threshold_standards"
        activation_condition: "competency_scores available AND agent_capabilities mapped"
      error_handling:
        competency_matching_failure:
          action: "use_basic_keyword_selection"
          selection_criteria: ["domain_match", "availability", "basic_keywords"]
          user_notification: "Advanced agent matching failed. Using basic selection criteria."
        insufficient_confidence:
          action: "present_user_choices"
          confidence_standard: "medium"
          present_options: 3
          choice_message: "Multiple agents found with similar capabilities. Please select preferred option:"
        all_agents_unavailable:
          action: "escalate_to_user_selection"
          fallback_to_native: true
          escalation_message: "All specialized agents unavailable. Would you like to proceed with native tools?"
        selection_timeout:
          action: "auto_select_best_available"
          timeout_duration: 30
          default_selection: "highest_available_score"
      config:
        selection_criteria:
          competency_threshold: 0.7
          availability_check: true
          performance_history: true
          backup_options: true
        tfidf_analysis: true
        vector_similarity: true
        expertise_mapping: true
        uncertainty_quantification: true
        selection_confidence_threshold: 0.8
      output:
        selected_agent: "string"
        selection_confidence: "float"
        backup_options: "array"
        selection_rationale: "string"

    - name: "clarification_subsystem"
      priority: 16
      method: "ambiguity_resolution"
      dependencies:
        agent_selection_dependency: "agent_selection_algorithm"
        activation_condition: "ambiguity_score > threshold OR user_clarification_requested"
      error_handling:
        ambiguity_detection_failure:
          action: "assume_minimum_ambiguity"
          default_ambiguity_score: 0.3
          proceed_with_analysis: true
          log_detection_error: true
        question_generation_errors:
          action: "use_standard_question_set"
          standard_questions: [
            "What specific outcome are you looking for?",
            "Are there any constraints or requirements I should consider?",
            "What is the expected timeline for this task?"
          ]
        user_response_parsing_errors:
          action: "request_manual_clarification"
          fallback_clarification: "I had trouble understanding your response. Could you please clarify using simpler terms?"
        clarification_loop_timeout:
          action: "proceed_with_best_understanding"
          max_clarification_rounds: 3
          timeout_duration: 300
          confidence_adjustment: -0.2
      config:
        ambiguity_detection:
          detection_criteria:
            vague_language:
              indicators: ["maybe", "possibly", "might", "could", "should", "think about", "consider", "explore"]
              weight: 0.3
            missing_requirements:
              indicators: ["unclear_scope", "undefined_deliverables", "missing_constraints", "incomplete_specs"]
              weight: 0.4
            conflicting_goals:
              indicators: ["contradictory_requirements", "mutually_exclusive_outcomes", "incompatible_objectives"]
              weight: 0.5
            insufficient_context:
              indicators: ["no_domain_specified", "missing_technical_context", "unclear_environment"]
              weight: 0.3
            complexity_mismatch:
              indicators: ["oversimplified_complex_tasks", "overcomplicated_simple_tasks"]
              weight: 0.35
          scoring_algorithm:
            linguistic_weight: 0.25
            semantic_weight: 0.30
            requirement_weight: 0.35
            complexity_weight: 0.10
            threshold: 0.6

        question_generation:
          question_types:
            requirements_clarification:
              templates: [
                "What specific {deliverable_type} are you looking for?",
                "Could you describe the expected {outcome_characteristics}?",
                "What are the acceptance criteria for this {task_component}?",
                "Are there any {integration_requirements} with existing systems?"
              ]
            scope_definition:
              templates: [
                "What should be included/excluded from the scope of this {task_domain}?",
                "Are there any specific {constraints} or limitations we should consider?",
                "What are the boundaries of this project in terms of {boundary_type}?",
                "Should we focus on {focus_area} or expand to include {additional_area}?"
              ]
            technical_context:
              templates: [
                "What {technology_stack} should be used for this implementation?",
                "Are there any {technical_constraints} or compatibility requirements?",
                "What's the target {platform_environment} and deployment context?",
                "Are there existing {technical_dependencies} or integrations to consider?"
              ]
            preference_elicitation:
              templates: [
                "Do you prefer {approach_a} or {approach_b} for this implementation?",
                "What's more important for this task: {priority_a} or {priority_b}?",
                "Are there any {stylistic_preferences} or design guidelines to follow?",
                "Should we prioritize {speed} or {quality} for this task?"
              ]
            risk_assessment:
              templates: [
                "What are the main {risk_factors} you foresee with this approach?",
                "Are there any {dependency_risks} we should address upfront?",
                "What {mitigation_strategies} should we consider for potential issues?",
                "Are there any {timeline_constraints} or deadlines affecting risk assessment?"
              ]
          generation_algorithm:
            max_questions: 7
            min_questions: 3
            semantic_filtering: true
            redundancy_removal: true
            prioritization: "ambiguity_resolution_potential"

        response_processing:
          processing_steps:
            semantic_analysis: [
              "Extract key information using semantic similarity",
              "Identify constraint specifications with context",
              "Detect preference indications through sentiment analysis",
              "Recognize domain-specific terminology"
            ]
            context_integration: [
              "Update task description with clarified details",
              "Add newly identified constraints with relevance",
              "Incorporate user preferences with validation",
              "Enhance domain mappings using semantic matching"
            ]
            ambiguity_reevaluation: [
              "Re-calculate ambiguity scores using updated analysis",
              "Identify remaining uncertainties through gap detection",
              "Assess need for follow-up questions",
              "Generate confidence improvements"
            ]

        uncertainty_triggers:
          confidence_threshold: 0.6
          complexity_threshold: 3
          ambiguity_indicators: ["unclear", "ambiguous", "confusing", "questions"]
        clarification_strategies:
          ask_specific_questions: true
          request_examples: true
          propose_interpretations: true
          validate_understanding: true
        max_clarification_rounds: 3
      output:
        clarification_needed: "boolean"
        clarification_questions: "array"
        resolved_understanding: "boolean"
        ambiguity_score: "float (0.0-1.0)"
        ambiguity_sources: "array"
        confidence_level: "float"
        detection_details: "object"
        question_priorities: "array"
        semantic_relevance_scores: "array"

    # === EXECUTION ENGINE OPERATIONS (Priority 21-30) ===

    - name: "todo_generation_system"
      priority: 21
      method: "multi_dimensional_task_decomposition"
      dependencies:
        trigger_source: "task_received_coordinator"
        required_outputs: ["execution_sequence_planned", "coordination_plan", "task_metadata"]
        sequential_after: ["clarification_subsystem", "agent_selection_algorithm"]
        activation_condition: "execution_sequence_planned == true"
      config:
        generation_algorithm:
          multi_dimensional_analysis:
            task_analysis_parsing: true
            tfidf_results_extraction: true
            agent_mapping_review: true
            domain_specialization_identification: true
            parallel_execution_analysis: true

          task_decomposition:
            high_complexity_4plus:
              structure: "multi_phase_execution"
              features: ["dependency_graph", "critical_path", "cross_phase_integration"]
            medium_complexity_2_3:
              structure: "structured_task_sequence"
              features: ["parallel_opportunities", "dependency_relationships", "priority_assignments"]
            low_complexity_1:
              structure: "simple_linear_plan"
              features: ["sequential_execution", "single_agent_assignment"]

          semantic_construction:
            todo_item_structure:
              content: "extract_actionable_description"
              status: "pending"
              activeForm: "generate_semantic_verb_phrase"
              agent_assignment: "select_optimal_agent_with_fallback"
              estimated_time: "calculate_enhanced_time_estimate"
              dependencies: "identify_dependency_list_with_validation"
              priority: "assign_strategic_priority"
              required_capabilities: "extract_capability_requirements"
              confidence: "calculate_assignment_confidence"

          strategic_planning:
            business_priority_weighting: true
            user_preference_integration: true
            resource_constraint_consideration: true
            efficiency_optimization: true
            realistic_time_estimation: true

        breakdown_strategies:
          by_component: true
          by_dependency: true
          by_expertise: true
          by_timeline: true
        todo_format: "structured_actionable_items"
        auto_prioritization: true
      output:
        todo_list: "array"
        execution_plan: "array"
        estimated_timeline: "string"
        todo_plan: "array"
        execution_strategy: "string"
        confidence_level: "float"
        decomposition_details: "object"

    - name: "delegation_engine"
      priority: 22
      method: "intelligent_task_assignment"
      config:
        selection_algorithm:
          semantic_analysis:
            tfidf_matching: true
            domain_weighting: true
            similarity_scoring: true
            compatibility_filtering: true
          competency_matching:
            vector_comparison: true
            skill_weighting: true
            experience_adjustment: true
            technical_validation: true
          performance_integration:
            historical_metrics: true
            time_decay_factor: 0.95
            success_rate_weighting: true
            reliability_metrics: true
          registry_integration:
            dynamic_discovery: true
            name_resolution: true
            load_balancing: true
            availability_validation: true

        selection_criteria:
          balanced_selection:
            weights:
              competency_match: 0.45
              performance_history: 0.25
              tfidf_semantic_similarity: 0.20
              availability: 0.10
            min_confidence: 0.6
          performance_priority:
            weights:
              competency_match: 0.35
              performance_history: 0.45
              tfidf_semantic_similarity: 0.15
              availability: 0.05
            min_confidence: 0.7
          availability_priority:
            weights:
              competency_match: 0.40
              availability: 0.35
              performance_history: 0.20
              tfidf_semantic_similarity: 0.05
            min_confidence: 0.5

        delegation_criteria:
          complexity_threshold: 2.0
          confidence_threshold: 0.6
          multi_agent_threshold: 3
        batch_integration:
          enabled: true
          independence_validation: true
          resource_allocation: true
        selection_process:
          primary_competency_match: 0.7
          availability_check: true
          performance_history: true
      output:
        delegation_plan: "object"
        selected_agents: "array"
        coordination_requirements: "object"
        agent_assignments: "object"
        confidence_scores: "object"
        fallback_options: "array"
        selection_metrics: "object"

    - name: "coordination_system"
      priority: 23
      method: "multi_agent_orchestration"
      config:
        coordination_strategies:
          parallel_execution: true
          sequential_dependencies: true
          resource_sharing: true
          conflict_resolution: true
        communication_protocols:
          agent_to_agent: true
          status_broadcasting: true
          progress_tracking: true
          result_aggregation: true
      output:
        coordination_plan: "array"
        communication_channels: "array"
        monitoring_points: "array"

    - name: "parallel_execution_module"
      priority: 24
      method: "concurrent_task_processing"
      config:
        parallel_configuration:
          limit_source: "system_resource_limits"
          operation_type: "general_tasks"
          resource_allocation: "dynamic"
          load_balancing: true
          limit_enforcement: "hard"
        batch_processing:
          auto_detection: true
          similarity_threshold: 0.8
          min_batch_size: 2
          max_batch_size: 15
        execution_monitoring:
          progress_tracking: true
          timeout_management: true
          error_propagation: true
      output:
        parallel_groups: "array"
        execution_timeline: "string"
        resource_allocation: "object"

    - name: "batch_orchestration_engine"
      priority: 25
      method: "intelligent_batch_processing"
      config:
        batch_detection_workflow:
          source_system: "task_analysis"
          input_data: "user_task_with_operations"
          thresholds:
            minimum_batch_size: 3
            similarity_threshold: 0.8
            confidence_threshold: 0.6
            performance_improvement_target: 0.6
          operation_categories:
            file_operations:
              patterns: ["Read", "Write", "Edit"]
              limit_source: "system_resource_limits"
              operation_type: "file_operations"
              estimated_improvement: 0.80
            search_operations:
              patterns: ["Grep", "Glob", "Search"]
              limit_source: "system_resource_limits"
              operation_type: "search_operations"
              estimated_improvement: 0.75
            modification_operations:
              patterns: ["Edit text replacements", "structural changes"]
              limit_source: "system_resource_limits"
              operation_type: "modification_operations"
              estimated_improvement: 0.70
          workflow_steps: [
            "receive_task_analysis_results",
            "scan_for_batch_patterns",
            "apply_similarity_analysis",
            "validate_minimum_thresholds",
            "generate_batch_detection_results"
          ]

        batch_preparation_workflow:
          source_system: "delegation"
          input_data: "batch_detection_results + task_analysis_data"
          workflow_steps: [
            "receive_batch_detection_results",
            "validate_batch_feasibility_independence",
            "check_resource_availability_constraints",
            "plan_optimal_agent_assignments",
            "create_detailed_execution_timeline",
            "prepare_monitoring_fallback_mechanisms"
          ]
          validation_checks: [
            "operation_independence_verification",
            "resource_constraint_analysis",
            "agent_capability_matching",
            "timeline_feasibility_assessment",
            "safety_protocol_validation"
          ]

        batch_execution_workflow:
          source_system: "coordination"
          input_data: "prepared_batch + delegation_metadata"
          workflow_steps: [
            "receive_prepared_batch_from_delegation",
            "validate_batch_integrity_dependencies",
            "initialize_parallel_execution_environment",
            "execute_operations_concurrently_with_monitoring",
            "handle_failures_gracefully_with_retry_logic",
            "collect_aggregate_all_results"
          ]
          execution_parameters:
            parallel_execution_enabled: true
            individual_operation_retry: true
            batch_continuation_policy: "continue_with_successful"
            graceful_degradation: true
            complete_failure_recovery: "emergency_fallback"
          monitoring_aspects: [
            "real_time_progress_tracking",
            "individual_operation_status",
            "resource_utilization_monitoring",
            "error_detection_handling"
          ]

        batch_analysis:
          pattern_detection: true
          similarity_analysis: true
          dependency_validation: true
          opportunity_identification: true
        orchestration_strategies:
          parallel_by_default: true
          sequential_when_dependent: true
          adaptive_grouping: true
          resource_optimization: true

        monitoring_aspects: [
          "detection_accuracy_rate",
          "preparation_success_rate",
          "execution_efficiency_score",
          "time_reduction_achieved",
          "fallback_activation_frequency",
          "system_resource_utilization"
        ]
        performance_metrics:
          detection_accuracy:
            target: 0.90
            measurement: "successful_batch_detections / total_batch_opportunities"
          preparation_success:
            target: 0.95
            measurement: "successful_preparations / total_detections"
          execution_efficiency:
            target: 0.85
      output:
        batch_operations: "array"
        optimization_gains: "object"
        execution_strategy: "string"
        batch_detection_result: "object"
        pattern_analysis: "object"
        feasibility_assessment: "object"
        preparation_status: "string"
        execution_plan: "object"
        resource_allocation: "object"
        agent_assignments: "array"
        execution_status: "string"
        batch_results: "array"
        performance_metrics: "object"
        error_reports: "array"

    - name: "adaptive_replanning"
      priority: 26
      method: "dynamic_optimization"
      dependencies:
        trigger_source: "optimization_monitor"
        required_outputs: ["adaptive_replanning_triggers", "new_patterns_discovered", "optimization_opportunities", "performance_degradation_detected"]
        activation_condition: "len(adaptive_replanning_triggers) > 0 OR new_patterns_discovered OR performance_degradation_detected"
      config:
        optimization_triggers:
          performance_degradation: true
          new_opportunities: true
          failure_patterns: true
          resource_availability: true
        replanning_strategies:
          todo_regeneration: true
          priority_rebalancing: true
          parallel_grouping: true
          resource_reallocation: true
      output:
        optimized_plan: "array"
        efficiency_gains: "object"
        replanning_summary: "string"

    # === OPTIMIZATION OPERATIONS (Priority 31-35) ===

    - name: "performance_optimizer"
      priority: 31
      method: "token_efficiency_optimization"
      config:
        optimization_techniques:
          flat_hierarchy: true
          parameter_grouping: true
          concise_descriptions: true
          symbol_usage: true
        target_reduction: 0.50
        quality_preservation: true
      output:
        optimization_results: "object"
        token_savings: "integer"
        performance_improvement: "float"

    - name: "resource_manager"
      priority: 32
      method: "dynamic_resource_allocation"
      config:
        resource_monitoring:
          memory_usage: true
          cpu_utilization: true
          token_consumption: true
        allocation_strategies:
          demand_based: true
          priority_based: true
          efficiency_based: true
        resource_limits:
          max_memory_mb: 512
          max_cpu_percent: 75
          max_token_rate: 1000
      output:
        resource_allocation: "object"
        utilization_metrics: "object"
        optimization_suggestions: "array"

    - name: "quality_assurance"
      priority: 33
      method: "comprehensive_validation"
      config:
        validation_checks:
          yaml_structure: true
          operation_sequencing: true
          dependency_integrity: true
          fallback_readiness: true
        quality_metrics:
          functional_completeness: 1.0
          execution_reliability: 0.99
          error_recovery_capability: 0.95
          performance_efficiency: 0.85
      output:
        quality_assurance_results: "object"
        quality_scores: "object"
        improvement_recommendations: "array"

    - name: "system_health_monitor"
      priority: 34
      method: "continuous_health_tracking"
      config:
        health_checks:
          mcp_server_connectivity: 30
          agent_availability: 60
          tool_functionality: 120
          performance_metrics: 300
        alerting:
          critical_thresholds: true
          performance_degradation: true
          failure_patterns: true
      output:
        health_status: "object"
          performance_metrics: "object"
          active_alerts: "array"

    - name: "optimization_monitor"
      priority: 35
      method: "continuous_optimization_monitoring"
      dependencies:
        monitor_sources: ["system_health_monitor", "resource_manager", "performance_optimizer"]
        required_outputs: ["health_status", "utilization_metrics", "optimization_results"]
        monitoring_frequency: "continuous"
      config:
        optimization_detection:
          performance_degradation:
            detection_method: "performance_trend_analysis"
            metrics_monitored: ["task_completion_time", "success_rate", "resource_efficiency"]
            threshold: 20
            time_window: 300
            severity: "high"
          new_opportunities:
            detection_method: "pattern_recognition_analysis"
            opportunity_types: ["parallel_execution", "batch_operations", "resource_reallocation", "agent_reassignment"]
            confidence_threshold: 0.7
            analysis_frequency: 120
            severity: "medium"
          failure_patterns:
            detection_method: "failure_pattern_analysis"
            pattern_types: ["timeout_clusters", "resource_exhaustion", "agent_unavailability", "dependency_failures"]
            correlation_threshold: 0.8
            pattern_recognition_window: 600
            severity: "critical"
          resource_availability:
            detection_method: "resource_utilization_analysis"
            resources_monitored: ["cpu", "memory", "agent_availability", "mcp_tool_availability"]
            underutilization_threshold: 30
            overutilization_threshold: 80
            rebalancing_opportunities: true
            severity: "medium"
        activation_logic:
          automatic_adaptive_replanning: true
          optimization_score_calculation: true
          priority_based_scheduling: true
          resource_safety_checks: true
          max_concurrent_optimizations: 3
        coordination_with_adaptive_replanning:
          trigger_generation: true
          optimization_package_preparation: true
          feasibility_validation: true
          rollback_readiness: true
        monitoring_aspects:
          detection_accuracy: 0.90
          false_positive_rate: 0.10
          optimization_latency: 15
          resource_impact_monitoring: true
      output:
        optimization_opportunities: "array"
        performance_degradation_detected: "boolean"
        new_patterns_discovered: "array"
        resource_rebalancing_needed: "boolean"
        adaptive_replanning_triggers: "array"
        optimization_recommendations: "array"
        monitoring_summary: "object"
        system_optimization_score: "float"
        optimization_history: "array"

    - name: "fallback_monitor"
      priority: 36
      method: "continuous_fallback_monitoring"
      dependencies:
        monitor_source: "system_health_monitor"
        required_outputs: ["health_status", "performance_metrics", "active_alerts"]
        monitoring_frequency: "continuous"
      config:
        fallback_trigger_detection:
          level_1_triggers:
            all_agents_unavailable:
              detection_method: "check_agent_registry_status"
              threshold: 100
              time_window: 60
              severity: "critical"
            mcp_servers_down:
              detection_method: "monitor_mcp_connectivity"
              threshold: 80
              time_window: 30
              severity: "critical"
            critical_system_failure:
              detection_method: "system_health_assessment"
              threshold: 0.3
              severity: "emergency"
          level_2_triggers:
            partial_agent_failure:
              detection_method: "agent_success_rate_monitoring"
              threshold: 70
              time_window: 300
              severity: "high"
            performance_degradation:
              detection_method: "performance_metrics_analysis"
              threshold: 50
              time_window: 180
              severity: "medium"
            timeout_issues:
              detection_method: "operation_timeout_tracking"
              threshold: 40
              time_window: 240
              severity: "high"
          level_3_triggers:
            complete_system_overload:
              detection_method: "resource_utilization_monitoring"
              threshold: 90
              time_window: 120
              severity: "emergency"
            memory_exhaustion:
              detection_method: "memory_usage_tracking"
              threshold: 95
              time_window: 60
              severity: "emergency"
            critical_errors:
              detection_method: "error_rate_monitoring"
              threshold: 60
              time_window: 90
              severity: "critical"
        activation_logic:
          automatic_activation: true
          level_selection: "severity_based"
          activation_cooldown: 120
          fallback_switching: true
          recovery_detection: true
        monitoring_aspects:
          trigger_detection_rate: 0.95
          false_positive_rate: 0.05
          activation_latency: 5
          recovery_detection_time: 30
      output:
        fallback_active: "boolean"
        current_fallback_level: "integer"
        activation_triggers_detected: "array"
        fallback_performance_metrics: "object"
        recovery_status: "boolean"
        system_stability_score: "float"
        alert_history: "array"

    - name: "final_optimization"
      priority: 37
      method: "system_tuning"
      config:
        tuning_parameters:
          operation_priorities: true
          resource_allocation: true
          monitoring_frequency: true
          fallback_strategies: true
        optimization_goals:
          minimize_latency: true
          maximize_success_rate: true
          optimize_resource_usage: true
          ensure_reliability: true
      output:
        optimization_summary: "object"
        system_efficiency: "float"
        readiness_status: "boolean"

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
    monitoring_metrics: "object"

fallback:
  enabled: true
  strategy: "comprehensive_fallback_system"
  levels:
    level_1_native_fallback:
      description: "Use Claude Code native tools only"
      activation_triggers: ["all_agents_unavailable", "mcp_servers_down", "critical_system_failure"]
      capabilities: ["file_operations", "web_search_fetch", "bash_commands", "basic_analysis"]
      performance_impact: "minimal"
      recovery_time: "instant"
    level_2_simplified_execution:
      description: "Simplified analysis and execution"
      activation_triggers: ["partial_agent_failure", "performance_degradation", "timeout_issues"]
      capabilities: ["reduced_task_analysis", "basic_agent_selection", "simplified_coordination"]
      performance_impact: "moderate"
      recovery_time: "5-10_seconds"
    level_3_emergency_fallback:
      description: "Emergency system with minimal functionality"
      activation_triggers: ["complete_system_overload", "memory_exhaustion", "critical_errors"]
      capabilities: ["minimal_processing", "error_reporting", "system_logging"]
      performance_impact: "severe"
      recovery_time: "15-30_seconds"
  alternatives:
    primary:
      - "native_tools_only"
      - "simplified_analysis"
      - "basic_delegation"
    secondary:
      - "direct_execution"
      - "minimal_coordination"
    emergency:
      - "system_logging_only"
  circuit_breaker: true
  retry_logic:
    max_retries: 3
    backoff_strategy: "exponential"
    retry_delays: [1000, 2000, 4000]
    jitter: true
    retry_on_specific_errors: ["timeout", "connection_failed", "temporarily_unavailable"]
  recovery_mechanisms:
    automatic_retry: true
    graceful_degradation: true
    emergency_recovery: true
    user_notification: false
  validation_rules:
      validate_before_fallback: true
      monitor_fallback_success: true
      automatic_recovery: true

monitoring:
  enabled: true
  minimal: true
  metrics:
    - "task_success_rate"
    - "mcp_tool_health"
    - "agent_selection_accuracy"
    - "performance_efficiency"
  targets:
    task_success_rate: 0.96
    mcp_tool_health: 0.95
    agent_selection_accuracy: 0.96
    performance_efficiency: 0.85

integration:
  inputs:
    - "user_task_description"
    - "agent_registry"
    - "mcp_server_capabilities"
    - "system_context"
  outputs:
    - "execution_summary"
    - "performance_metrics"
    - "agent_coordination_results"

performance_optimization:
  token_efficiency:
    enabled: true
    target_reduction: 0.50
    techniques: ["flat_hierarchy", "parameter_grouping", "concise_descriptions"]
  parallel_processing:
    batch_threshold: 3
    max_concurrent: 10
    resource_allocation: "dynamic"
  adaptive_batching:
    enabled: true
    pattern_recognition: true
    cross_operation_analysis: true
    similarity_threshold: 0.8
