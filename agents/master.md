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
tools: ["dynamic_agent_discovery"]  # Do not change!
version: "0.2.0"

component:
  name: "master"
  version: "0.2.0"
  description: "An AI agent that optimizes task execution through planning, parallelization, and execution in subtasks or delegation to existing agents in the system, which are automatically initialized taking into account their competencies." # Do not change!
  category: "orchestration"
  priority: 1
  status: "stable"
  token_optimization:
    original_tokens: 6642
    optimized_tokens: 3300
    savings_percentage: 50
  latest_update:
    version: "0.2.0"
    changes: ["Added categorized greeting formation engine", "Integrated event-driven system announcements", "Enhanced system readiness display"]
    timestamp: "2025-01-XX"

implementation:
  operations:
    # === SYSTEM INITIALIZATION (Priority 0) ===

    - name: "system_initialization"
      priority: 0
      method: "independent_bootstrap_sequence"
      trigger: "on_agent_load"
      config:
        bootstrap_operations:
          - priority: 1
            operation: "error_system_initialization"
            required_for_system: true
            description: "Setup fallback framework and error handling"
          - priority: 2
            operation: "monitoring_minimal_setup"
            required_for_system: true
            description: "Initialize basic metrics collection framework"
          - priority: 3
            operation: "basic_system_readiness"
            required_for_system: true
            description: "Verify minimum system functionality"
          - priority: 4
            operation: "bootstrap_completion_report"
            required_for_system: true
            description: "Display bootstrap completion status"
        initialization_parameters:
          bootstrap_mode: "independent"
          timeout_seconds: 60
          retry_on_failure: true
          max_retries: 2
          fallback_to_safe_mode: true
          minimum_components_only: true
        error_handling:
          bootstrap_failure:
            action: "activate_emergency_bootstrap"
            log_error: true
            notify_user: true
          partial_failure:
            action: "continue_with_core_components"
            log_warning: true
          timeout_failure:
            action: "force_bootstrap_completion"
            notify_user: "Bootstrap completed with minimal components"
      output:
        bootstrap_complete: "boolean"
        basic_monitoring_active: "boolean"
        system_health_score: "float"
        fallback_systems_ready: "boolean"
        initialization_time: "float"
        bootstrap_operations_summary: "object"

    # === SYSTEM DISCOVERY PHASE (Priority 1) ===

    - name: "system_discovery_phase"
      priority: 1
      method: "discover_system_components"
      dependencies:
        required_inputs:
          - component: "system_initialization"
            expected_outputs: ["bootstrap_complete", "basic_monitoring_active"]
            validation: "bootstrap_complete == true && basic_monitoring_active == true"
      config:
        discovery_operations:
          - priority: 1
            operation: "mcp_server_discovery"
            description: "Real-time discovery and analysis of MCP servers using ListMcpResourcesTool"
            implementation:
              tool: "ListMcpResourcesTool"
              parallel_execution: true
              timeout: 30
              retry_count: 3
              servers: ["all_available"]
              error_handling:
                timeout_action: "continue_with_discovered"
                failure_action: "log_error_continue"
                partial_success_action: "use_available_servers"
          - priority: 2
            operation: "agent_registry_construction"
            description: "Build registry of available agents through multiple discovery methods"
            implementation:
              tool: "Task"
              parallel_execution: true
              timeout: 25
              methods:
                - discover_subagent_types
                - query_agent_capabilities
          - priority: 2.5
            operation: "dynamic_agent_discovery"
            description: "Dynamic discovery of all available agents with real tool calls"
            implementation:
              discovery_methods:
                - name: "task_tool_api_discovery"
                  tool: "Task"
                  method: "enumerate_subagent_types"
                  parallel: true
                - name: "persona_instruction_scan"
                  tool: "Read"
                  method: "scan_persona_instructions"
                  paths: ["/home/user/.claude/"]
                  patterns: ["*.md"]
                - name: "filesystem_agent_search"
                  tool: "Glob"
                  method: "find_agent_files"
                  patterns: ["agents/**/*", "*/agents/*"]
                - name: "mcp_server_agent_enumeration"
                  tool: "ListMcpResourcesTool"
                  method: "extract_mcp_capabilities"
                  parallel: true
                - name: "configuration_based_discovery"
                  tool: "Read"
                  method: "parse_config_files"
                  patterns: ["*.yaml", "*.json"]
        discovery_parameters:
          scan_timeout: 120
          retry_on_failure: true
          max_discovery_retries: 3
          parallel_discovery: true
        error_handling:
          discovery_failure:
            action: "continue_with_builtin_servers"
            log_warning: true
            notify_user: "Some components not found, using built-in alternatives"
          partial_discovery:
            action: "continue_with_available_components"
            log_info: true
      output:
        discovery_complete: "boolean"
        mcp_servers_discovered: "array"
        agents_registry_built: "boolean"
        discovered_agents: "array"
        mcp_tool_inventory: "object"
        discovery_summary: "object"
        discovery_time: "float"

    # === DYNAMIC TEXT ANALYSIS AND CATEGORIZATION PHASE (Priority 2.6) ===

    - name: "dynamic_text_analysis_phase"
      priority: 2.6
      method: "real_time_text_processing"
      dependencies:
        required_inputs:
          - component: "system_discovery_phase"
            expected_outputs: ["discovery_complete", "mcp_servers_discovered", "discovered_agents"]
            validation: "discovery_complete == true"
      config:
        text_analysis_operations:
          - priority: 1
            operation: "text_extraction_and_parsing"
            description: "Extract and parse descriptions from MCP servers and agents"
            implementation:
              parallel_processing: true
              text_sources:
                - mcp_server_descriptions
                - agent_descriptions
                - persona_instructions
              preprocessing:
                - lowercase_conversion
                - stop_word_removal
                - lemmatization
                - ngram_extraction: [1, 2, 3]

          - priority: 2
            operation: "tfidf_vectorization"
            description: "Create TF-IDF vectors for semantic analysis"
            implementation:
              vectorizer: "TfidfVectorizer"
              parameters:
                max_features: 1000
                ngram_range: [1, 3]
                min_df: 2
                max_df: 0.8
                norm: "l2"
              parallel_execution: true

          - priority: 3
            operation: "dynamic_clustering"
            description: "Perform clustering on extracted features"
            implementation:
              clustering_algorithm: "kmeans"
              cluster_count_method: "auto_determine"
              similarity_metric: "cosine"
              validation_methods: ["silhouette", "elbow", "gap_statistic"]
              category_generation:
                method: "top_keywords_extraction"
                format: "semantic_category_names"

          - priority: 4
            operation: "competency_matrix_construction"
            description: "Build dynamic competency matrix from analysis results"
            implementation:
              matrix_structure: "agents × competencies"
              scoring_method: "weighted_confidence"
              confidence_calculation: "multi_source_validation"
              dynamic_updates: true
            method: "instruction_parsing"
            source: "persona_analysis"
          - priority: 3
            operation: "filesystem_agent_search"
            description: "Scan filesystem for agent definitions"
            method: "pattern_based_search"
            source: "file_system_scan"
          - priority: 4
            operation: "mcp_server_agent_enumeration"
            description: "Enumerate agents from MCP servers"
            method: "server_based_discovery"
            source: "mcp_integration"
          - priority: 5
            operation: "agent_capability_analysis"
            description: "Analyze discovered agents' capabilities"
            method: "semantic_competency_extraction"
            source: "capability_analysis"
        discovery_parameters:
          parallel_execution: true
          scan_timeout: 180
          confidence_threshold: 0.7
          semantic_analysis: true
          competency_extraction: true
        validation_parameters:
          agent_availability_check: true
          capability_validation: true
          duplicate_detection: true
          conflict_resolution: true
        error_handling:
          discovery_failure:
            action: "continue_with_available_agents"
            log_warning: true
            notify_user: "Some agent discovery methods failed, using available agents"
          partial_discovery:
            action: "continue_with_partial_registry"
            log_info: true
          validation_failure:
            action: "use_best_effort_analysis"
            log_warning: true
      output:
        dynamic_discovery_complete: "boolean"
        discovered_agents: "array"
        agent_capabilities_mapped: "boolean"
        agent_registry_enhanced: "object"
        discovery_summary: "object"
        confidence_scores: "object"
        duplicate_agents_removed: "integer"

    # === SYSTEM INTEGRATION PHASE (Priority 3) ===

    - name: "system_integration_phase"
      priority: 2
      method: "integrate_discovered_components"
      dependencies:
        required_inputs:
          - component: "system_discovery_phase"
            expected_outputs: ["discovery_complete", "mcp_servers_discovered", "agents_registry_built"]
            validation: "discovery_complete == true && agents_registry_built == true"
      config:
        integration_operations:
          - priority: 1
            operation: "system_validation"
            description: "Validate discovered components and system integrity"
            source: "moved_from_system_initialization"
          - priority: 2
            operation: "component_integration_testing"
            description: "Test component interactions and compatibility"
          - priority: 3
            operation: "capability_mapping"
            description: "Map agent capabilities to MCP tools"
        integration_parameters:
          validation_timeout: 60
          integration_testing: true
          capability_analysis: true
          cross_component_validation: true
        error_handling:
          integration_failure:
            action: "continue_with_partial_integration"
            log_warning: true
            notify_user: "Some components not fully integrated"
          validation_failure:
            action: "continue_with_available_validations"
            log_info: true
      output:
        integration_complete: "boolean"
        system_validated: "boolean"
        capability_mappings_created: "boolean"
        integration_summary: "object"
        validation_results: "object"
        integration_time: "float"

    # === SYSTEM READINESS PHASE (Priority 3) ===

    - name: "system_readiness_phase"
      priority: 3
      method: "finalize_system_readiness"
      dependencies:
        required_inputs:
          - component: "system_integration_phase"
            expected_outputs: ["integration_complete", "system_validated"]
            validation: "integration_complete == true && system_validated == true"
      config:
        readiness_operations:
          - priority: 1
            operation: "final_readiness_check"
            description: "Perform comprehensive system readiness assessment"
          - priority: 2
            operation: "greeting_formation_engine"
            description: "Generate categorized system greeting with dynamic agent and MCP server lists"
            implementation:
              data_sources:
                agent_categories: "from_dynamic_analysis_results"
                mcp_categories: "from_dynamic_analysis_results"
                agent_count: "from_discovered_agents"
                mcp_count: "from_mcp_servers_discovered"
              format_template: "Категорій агентів: {agent_categories}\\nКількість Агентів: {agent_count}\\nКатегорій MCP серверов: {mcp_categories}\\nКількість MCP серверів: {mcp_count}"
              validation:
                ensure_data_availability: true
                format_validation: true
                error_handling: "fallback_to_basic_message"
          - priority: 3
            operation: "integrated_system_readiness_display"
            description: "Display comprehensive system announcement with dynamically categorized content"
            implementation:
              display_format: "structured_with_categories"
              content_sources:
                - "system_readiness_status"
                - "discovered_capabilities"
                - "dynamic_categories"
                - "competency_summary"
              error_handling:
                incomplete_data: "display_available_only"
                formatting_errors: "use_basic_template"
            dependencies: ["greeting_formation_engine"]
          - priority: 4
            operation: "capability_announcement"
            description: "Announce system capabilities to user"
            dependencies: ["integrated_system_readiness_display"]
        readiness_parameters:
          readiness_threshold: 0.9
          comprehensive_check: true
          capability_announcement: true
        error_handling:
          readiness_failure:
            action: "announce_basic_readiness"
            log_warning: true
            notify_user: "System ready with basic capabilities"
        output:
        system_ready: "boolean"
        readiness_complete: "boolean"
        greeting_generated: "boolean"
        greeting_data: "object"
        capabilities_announced: "boolean"
        readiness_report: "object"
        final_health_score: "float"
        system_waiting_for_task: "boolean"

    # === CRITICAL BOOTSTRAP OPERATIONS (Priority 4-10) ===

    - name: "error_system_initialization"
      priority: 4
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

    # MOVED: mcp_server_discovery → system_discovery_phase (priority 1)

    # MOVED: agent_registry_construction → system_discovery_phase (priority 1)

    # MOVED: system_validation → system_integration_phase (priority 2)

    # MOVED: system_readiness_report_display → system_readiness_phase (priority 3)

    # === GREETING FORMATION ENGINE (Priority 3.1) ===

    - name: "greeting_formation_engine"
      priority: 3.1
      method: "event_driven_greeting_generation"
      event_subscription:
        listen_to: "system.readiness.verified"
        correlation_field: "system_id"
        processing_mode: "sequential"
      dependencies:
        system_readiness_dependency: "final_readiness_check"
        agent_registry_dependency: "agent_registry_enhancement"
        mcp_discovery_dependency: "system_discovery_phase"
        required_outputs: ["system_ready", "enhanced_agent_registry", "mcp_servers_discovered"]
        validation: "system_ready == true && enhanced_agent_registry != null && mcp_servers_discovered != null"
      config:
        greeting_generation:
          data_sources:
            agent_registry: "enhanced_agent_registry"
            mcp_servers: "mcp_servers_discovered"
            system_capabilities: "final_readiness_check_results"
            performance_metrics: "monitoring_minimal_setup_results"

          agent_categorization:
            categories:
              development_agents:
                criteria: ["backend", "frontend", "fullstack", "developer"]
                priority: 1
                description: "Software development and implementation specialists"
              system_agents:
                criteria: ["devops", "infrastructure", "system", "architect"]
                priority: 2
                description: "System architecture and infrastructure specialists"
              data_agents:
                criteria: ["data", "analytics", "ml", "science", "database"]
                priority: 3
                description: "Data processing and analytics specialists"
              quality_agents:
                criteria: ["testing", "qa", "quality", "validation", "security"]
                priority: 4
                description: "Quality assurance and security specialists"
              support_agents:
                criteria: ["documentation", "technical", "writer", "support"]
                priority: 5
                description: "Documentation and support specialists"

            agent_matching:
              method: "semantic_capability_matching"
              confidence_threshold: 0.7
              fallback_to_general: true
              uncategorized_handling: "general_category"

          mcp_server_processing:
            categories:
              core_platforms:
                criteria: ["context7", "magic", "sequential", "serena"]
                priority: 1
                description: "Core platform services"
              specialized_tools:
                criteria: ["playwright", "tavily", "chrome-devtools"]
                priority: 2
                description: "Specialized tool integrations"

            server_analysis:
              method: "capability_based_categorization"
              health_check_integration: true
              availability_validation: true

          template_engine:
            message_format: "structured_with_categories"
            dynamic_content: true
            localization_support: false
            performance_summary: true
            availability_indicators: true

            template_structure:
              greeting_section:
                type: "welcome_message"
                dynamic_content: true
              capabilities_section:
                type: "categorized_summary"
                show_counts: true
                show_health: true
              availability_section:
                type: "status_overview"
                show_performance: true
              next_steps_section:
                type: "guidance_message"
                contextual: true

        event_integration:
          input_events:
            - "system.readiness.verified"
            - "agent.registry.updated"
            - "mcp.discovery.completed"

          output_events:
            - "greeting.generated"
            - "system.announcement.ready"

          event_data_mapping:
            greeting_data: "generated_greeting_content"
            system_status: "readiness_assessment_results"
            agent_summary: "categorized_agent_counts"
            mcp_summary: "server_capability_summary"

        performance_optimization:
          caching_enabled: true
          cache_duration: 300  # 5 minutes
          incremental_updates: true
          background_refresh: true

        error_handling:
          categorization_failure:
            action: "use_general_category"
            fallback_categories: ["general", "uncategorized"]
            log_warning: true
          template_failure:
            action: "use_basic_template"
            preserve_core_information: true
            log_error: true
          data_source_unavailable:
            action: "use_cached_data"
            partial_generation: true
            notify_user: "System ready with partial information"

      output:
        greeting_generated: "boolean"
        greeting_content: "object"
        categorized_agents: "object"
        categorized_mcp_servers: "object"
        system_status_summary: "object"
        generation_metadata: "object"
        template_used: "string"
        event_published: "boolean"

    # === INTEGRATED SYSTEM READINESS DISPLAY (Priority 3.2) ===

    - name: "integrated_system_readiness_display"
      priority: 3.2
      method: "greeting_enhanced_system_display"
      dependencies:
        greeting_dependency: "greeting_formation_engine"
        readiness_dependency: "final_readiness_check"
        required_outputs: ["greeting_generated", "greeting_content", "system_ready"]
        validation: "greeting_generated == true && system_ready == true"
      config:
        display_integration:
          greeting_integration:
            use_categorized_agents: true
            use_categorized_mcp_servers: true
            dynamic_template_selection: true
            performance_summary_inclusion: true

          readiness_enhancement:
            incorporate_system_health: true
            include_performance_metrics: true
            availability_status_display: true
            capability_summary_integration: true

          template_system:
            base_template: "comprehensive_system_announcement"
            sections:
              welcome_section:
                source: "greeting_content.greeting_section"
                priority: 1
                dynamic_content: true
              capabilities_summary:
                source: "greeting_content.categorized_agents"
                include_counts: true
                include_health_status: true
                priority: 2
              infrastructure_status:
                source: "greeting_content.categorized_mcp_servers"
                include_availability: true
                include_performance: true
                priority: 3
              system_performance:
                source: "readiness_assessment.performance_metrics"
                include_health_score: true
                include_efficiency_ratings: true
                priority: 4
              next_steps_guidance:
                source: "greeting_content.next_steps_section"
                contextual_recommendations: true
                priority: 5

        output_format:
          structure: "hierarchical_categories_with_counts"
          include_performance_indicators: true
          availability_status_format: "health_based"
          categorization_method: "semantic_capability_grouping"

        dynamic_content_generation:
          agent_list_formatting:
            show_specialization: true
            show_confidence_scores: true
            group_by_category: true
            sort_by_priority: true

          mcp_server_formatting:
            show_capability_summary: true
            show_health_status: true
            group_by_platform_type: true
            availability_indicators: true

          system_metrics_formatting:
            show_performance_scores: true
            show_resource_utilization: true
            show_health_indicators: true
            trend_analysis: true

        error_handling:
          greeting_data_missing:
            action: "use_basic_readiness_template"
            fallback_content: "standard_system_capabilities"
            log_warning: true
          categorization_incomplete:
            action: "display_available_categories"
            note_uncategorized_items: true
            partial_display: true
          template_generation_failure:
            action: "use_simple_text_format"
            preserve_core_information: true
            log_error: true

        performance_optimization:
          result_caching: true
          cache_duration: 600  # 10 minutes
          incremental_refresh: true
          background_updates: true

      output:
        integrated_display_generated: "boolean"
        display_content: "object"
        agent_categories_summary: "object"
        mcp_servers_summary: "object"
        system_performance_summary: "object"
        template_metadata: "object"
        generation_time: "float"
        user_ready_content: "string"

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

  # === DYNAMIC AGENT DISCOVERY OPERATIONS (Priority 15-20) ===

    - name: "task_tool_agent_discovery"
      priority: 15
      method: "api_based_agent_enumeration"
      dependencies:
        system_discovery_dependency: "system_discovery_phase"
      config:
        api_discovery:
          task_tool_interface:
            enumeration_method: "subagent_type_discovery"
            capability_extraction: "description_parsing"
            validation_method: "availability_check"
          discovery_patterns:
            known_subagent_types:
              - "backend-architect"
              - "frontend-developer"
              - "security-engineer"
              - "devops-engineer"
              - "data-scientist"
              - "testing-specialist"
              - "ui-designer"
              - "technical-writer"
              - "performance-optimizer"
              - "api-specialist"
            dynamic_type_detection:
              pattern_matching: true
              semantic_analysis: true
              capability_inference: true
          validation_criteria:
            availability_check: true
            capability_verification: true
            response_time_threshold: 30
      output:
        task_tool_agents: "array"
        agent_capabilities: "object"
        discovery_metadata: "object"
        validation_results: "object"

    - name: "persona_instruction_discovery"
      priority: 16
      method: "instruction_based_persona_extraction"
      config:
        instruction_analysis:
          search_locations:
            - "/home/user/.claude/"
            - "/home/user/.claude/MODE_*.md"
            - "/home/user/.claude/MCP_*.md"
            - "/home/user/tools/subagent-master/CLAUDE.md"
          search_patterns:
            - "agent.*activation"
            - "persona.*specialist"
            - "expert.*activation"
            - "specialist.*agent"
            - "subagent.*type"
          extraction_patterns:
            persona_definitions:
              - "Backend Architect"
              - "Frontend Developer"
              - "Security Engineer"
              - "DevOps Engineer"
              - "Data Scientist"
              - "Testing Specialist"
              - "UI Designer"
              - "Technical Writer"
              - "Performance Optimizer"
              - "API Specialist"
              - "Business Analyst"
              - "System Integrator"
          capability_extraction:
            trigger_keywords: true
            domain_expertise: true
            tool_preferences: true
            methodology_patterns: true
        analysis_parameters:
          semantic_matching: true
          confidence_threshold: 0.6
          duplicate_detection: true
      output:
        persona_agents: "array"
        persona_capabilities: "object"
        instruction_mappings: "object"
        extraction_confidence: "float"

    - name: "filesystem_agent_search"
      priority: 17
      method: "pattern_based_filesystem_discovery"
      config:
        filesystem_scan:
          search_directories:
            - "/home/user/tools/subagent-master/agents/"
            - "/home/user/tools/*/agents/"
            - "/home/user/*agents*/"
            - "/home/user/*specialist*/"
          file_patterns:
            - "*.md"
            - "*.yaml"
            - "*.yml"
            - "agent.*"
            - "specialist.*"
            - "expert.*"
          content_patterns:
            agent_indicators:
              - "name:"
              - "description:"
              - "capabilities:"
              - "triggers:"
              - "component:"
              - "subagent_type:"
            expertise_indicators:
              - "backend"
              - "frontend"
              - "security"
              - "devops"
              - "data"
              - "testing"
              - "ui"
              - "api"
          analysis_methods:
            semantic_parsing: true
            competency_extraction: true
            capability_mapping: true
            availability_inference: true
        filtering_criteria:
          min_capability_count: 3
          description_length_min: 50
          trigger_presence_required: true
      output:
        filesystem_agents: "array"
        agent_files_found: "array"
        capability_mappings: "object"
        scan_summary: "object"

    - name: "mcp_server_agent_enumeration"
      priority: 18
      method: "server_based_agent_discovery"
      dependencies:
        mcp_discovery_dependency: "system_discovery_phase"
      config:
        mcp_server_analysis:
          server_capabilities:
            context7_agents:
              search_method: "tool_capability_analysis"
              capability_patterns:
                - "documentation_specialist"
                - "research_analyst"
                - "knowledge_manager"
            magic_agents:
              search_method: "ui_component_analysis"
              capability_patterns:
                - "frontend_developer"
                - "ui_designer"
                - "component_specialist"
            playwright_agents:
              search_method: "testing_capability_analysis"
              capability_patterns:
                - "testing_engineer"
                - "automation_specialist"
                - "e2e_tester"
            sequential_agents:
              search_method: "analysis_capability_inference"
              capability_patterns:
                - "system_analyst"
                - "architect"
                - "problem_solver"
            serena_agents:
              search_method: "symbol_operation_analysis"
              capability_patterns:
                - "code_analyst"
                - "symbol_specialist"
                - "project_manager"
            tavily_agents:
              search_method: "research_capability_analysis"
              capability_patterns:
                - "research_specialist"
                - "information_analyst"
                - "data_researcher"
          agent_inference:
            capability_to_agent_mapping: true
            expertise_extraction: true
            availability_assessment: true
      output:
        mcp_based_agents: "array"
        server_capability_mappings: "object"
        inferred_agent_types: "array"

    - name: "agent_capability_analysis"
      priority: 19
      method: "semantic_competency_extraction_and_analysis"
      dependencies:
        discovery_inputs: ["task_tool_agent_discovery", "persona_instruction_discovery", "filesystem_agent_search", "mcp_server_agent_enumeration"]
        tfidf_dependency: "unified_tfidf_processor"
      config:
        capability_analysis:
          semantic_extraction:
            tfidf_vectorization: true
            competency_keyword_extraction: true
            domain_classification: true
            expertise_level_assessment: true
          competency_dimensions:
            technical_skills:
              categories: ["programming", "frameworks", "databases", "cloud", "devops"]
              extraction_method: "keyword_pattern_matching"
            domain_expertise:
              categories: ["backend", "frontend", "security", "data", "testing"]
              extraction_method: "semantic_domain_analysis"
            problem_solving:
              categories: ["analysis", "design", "implementation", "optimization"]
              extraction_method: "capability_inference"
            tool_specialization:
              categories: ["mcp_tools", "native_tools", "framework_tools"]
              extraction_method: "tool_preference_analysis"
          confidence_scoring:
            multi_source_validation: true
            cross_reference_checking: true
            consistency_verification: true
        duplicate_detection:
          similarity_threshold: 0.8
          capability_overlap_analysis: true
          name_variation_handling: true
          priority_resolution: "most_capable"
      output:
        analyzed_agents: "array"
        competency_matrix: "object"
        confidence_scores: "object"
        duplicate_groups: "array"
        final_agent_registry: "object"

    - name: "agent_registry_enhancement"
      priority: 20
      method: "registry_consolidation_and_optimization"
      dependencies:
        analysis_dependency: "agent_capability_analysis"
      config:
        registry_operations:
          consolidation:
            merge_duplicate_agents: true
            resolve_conflicts: true
            optimize_structure: true
          enhancement:
            add_missing_metadata: true
            calculate_compatibility_scores: true
            generate_usage_recommendations: true
          validation:
            capability_consistency_check: true
            availability_verification: true
            performance_baseline_establishment: true
        registry_structure:
          agent_entries:
            required_fields: ["name", "type", "capabilities", "confidence", "source"]
            optional_fields: ["description", "triggers", "tools", "expertise_level", "availability"]
          capability_format:
            standardized_categories: true
            confidence_scores: true
            source_attribution: true
      output:
        enhanced_agent_registry: "object"
        registry_statistics: "object"
        optimization_summary: "object"

    # === TASK RECEIVING & COORDINATION (Priority 21) ===

    - name: "task_received_coordinator"
      priority: 21
      method: "central_task_handler"
      trigger: "on_task_received"
      dependencies:
        system_readiness_dependency:
          component: "system_readiness_phase"
          expected_outputs: ["system_ready", "readiness_complete", "final_health_score"]
          validation: "system_ready == true && readiness_complete == true && final_health_score >= 0.9"
        agent_discovery_dependency:
          component: "dynamic_agent_discovery_phase"
          expected_outputs: ["dynamic_discovery_complete", "enhanced_agent_registry"]
          validation: "dynamic_discovery_complete == true && enhanced_agent_registry != null"
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
          required_phases_complete: ["system_initialization", "system_discovery_phase", "dynamic_agent_discovery_phase", "system_integration_phase", "system_readiness_phase"]
          required_components_active: ["error_system", "monitoring", "mcp_servers", "enhanced_agent_registry"]
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

    # === PARALLEL TASK ANALYSIS COORDINATION (Priority 10.5) ===

    - name: "task_analysis_coordinator"
      priority: 10.5
      method: "parallel_analysis_orchestrator"
      dependencies:
        trigger_source: "task_received_coordinator"
        required_outputs: ["task_accepted", "task_metadata", "coordination_plan"]
        activation_condition: "task_accepted == true && analysis_sequence_initiated == true"
        event_system_dependency: "event_system"
      config:
        analysis_types:
          - name: "semantic_analysis"
            handler: "semantic_analysis_handler"
            parallel_group: "task_analysis"
            timeout: 15
            priority: "high"
            event_publish: "task.analysis.started"

          - name: "complexity_assessment"
            handler: "complexity_assessment_handler"
            parallel_group: "task_analysis"
            timeout: 20
            priority: "high"
            event_publish: "task.analysis.started"

          - name: "domain_classification"
            handler: "domain_classification_handler"
            parallel_group: "task_analysis"
            timeout: 15
            priority: "high"
            event_publish: "task.analysis.started"

        coordination_strategy:
          trigger_all: true
          wait_for_completion: false  # Fire-and-forget parallel execution
          correlation_id: "task_id"
          completion_handler: "analysis_completion_aggregator"

        parallel_execution:
          enabled: true
          max_concurrent: 3
          timeout_handling: "proceed_with_available_analyses"
          partial_results_handling: "use_available_proceed_with_selection"

        event_generation:
          correlation_id_source: "task_metadata.task_id"
          timestamp_generation: true
          performance_tracking: true

        error_handling:
          analysis_failure_handling: "continue_with_other_analyses"
          timeout_handling: "use_partial_proceed_with_selection"
          error_events: true

      output:
        analysis_jobs_started: "array"
        correlation_id: "string"
        analysis_timeout: "integer"
        parallel_execution_status: "object"
        event_generation_summary: "object"

    # === EVENT-DRIVEN ANALYSIS HANDLERS (Priority 11-13) ===

    - name: "semantic_analysis_handler"
      priority: 11
      method: "event_driven_semantic_analysis"
      event_subscription:
        listen_to: "task.received"
        correlation_field: "task_id"
        processing_mode: "parallel"
        event_filter: "handler == 'semantic_analysis_handler'"
      dependencies:
        tfidf_dependency: "unified_tfidf_processor"
        threshold_standards_dependency: "system_threshold_standards"
      config:
        usage_mode: "semantic_analysis"
        input_source: "event.description"
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
          error_event_publish: true
        event_output:
          event_type: "task.semantic.completed"
          data_mapping:
            task_id: "correlation_id"
            semantic_vector: "processing_results.vector"
            domain_indicators: "processing_results.domains"
            confidence: "processing_results.confidence"
            processing_time: "execution_time"
            correlation_id: "correlation_id"
      output:
        analysis_completed: "boolean"
        event_published: "boolean"
        processing_results: "object"
        execution_time: "float"

    - name: "complexity_assessment_handler"
      priority: 12
      method: "event_driven_complexity_analysis"
      event_subscription:
        listen_to: "task.received"
        correlation_field: "task_id"
        processing_mode: "parallel"
        event_filter: "handler == 'complexity_assessment_handler'"
      error_handling:
        processing_timeout: 20
        fallback_to_basic_scoring: true
        error_event_publish: true
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
        event_output:
          event_type: "task.complexity.completed"
          data_mapping:
            task_id: "correlation_id"
            complexity_score: "processing_results.score"
            factors: "processing_results.factor_breakdown"
            confidence: "processing_results.confidence"
            processing_time: "execution_time"
            correlation_id: "correlation_id"
      output:
        analysis_completed: "boolean"
        event_published: "boolean"
        processing_results: "object"
        execution_time: "float"

    - name: "domain_classification_handler"
      priority: 13
      method: "event_driven_domain_classification"
      event_subscription:
        listen_to: "task.received"
        correlation_field: "task_id"
        processing_mode: "parallel"
        event_filter: "handler == 'domain_classification_handler'"
      dependencies:
        tfidf_dependency: "unified_tfidf_processor"
        threshold_standards_dependency: "system_threshold_standards"
      error_handling:
        processing_timeout: 15
        fallback_to_keyword_matching: true
        confidence_reduction: 0.2
        error_event_publish: true
      config:
        domains:
          backend:
            keywords: ["api", "backend", "server", "database", "microservice", "infrastructure", "rest", "graphql", "sql", "nosql", "authentication", "authorization", "endpoint", "service"]
            patterns: ["build.*api", "design.*backend", "create.*server", "implement.*database", "setup.*endpoint", "configure.*service"]
            complexity_tendency: 2.0-3.5
            agent_prefs: ["backend-developer", "backend-architect", "fullstack"]
          frontend:
            keywords: ["frontend", "ui", "ux", "react", "vue", "angular", "web", "css", "javascript", "html", "responsive", "component", "interface", "design"]
            patterns: ["build.*ui", "design.*frontend", "create.*web.*app", "implement.*react", "design.*interface", "create.*component"]
            complexity_tendency: 2.0-3.5
            agent_prefs: ["frontend-developer", "ui-designer", "fullstack"]
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
        event_output:
          event_type: "task.domain.completed"
          data_mapping:
            task_id: "correlation_id"
            primary_domain: "processing_results.primary_domain"
            confidence: "processing_results.confidence"
            secondary_domains: "processing_results.secondary_domains"
            cross_domain_score: "processing_results.cross_domain_score"
            processing_time: "execution_time"
            correlation_id: "correlation_id"
      output:
        analysis_completed: "boolean"
        event_published: "boolean"
        processing_results: "object"
        execution_time: "float"

    # === LEGACY SEQUENTIAL OPERATIONS (Priority 14-20) ===

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
        # DEPRECATED: domain_classification moved to event-driven handler

    - name: "agent_competency_matching"
      priority: 14
      method: "matrix_scoring"
      dependencies:
        domain_classification_dependency: "domain_classification"
        agent_registry_dependency: "agent_registry_enhancement"
        activation_condition: "primary_domain assigned AND enhanced_agent_registry available"
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

    # === ANALYSIS COMPLETION AGGREGATOR (Priority 15.5) ===

    - name: "analysis_completion_aggregator"
      priority: 15.5
      method: "event_based_analysis_coordinator"
      event_subscription:
        listen_to: ["task.semantic.completed", "task.complexity.completed", "task.domain.completed"]
        correlation_field: "task_id"
        completion_strategy: "wait_for_all_events"
        timeout_handling: "proceed_with_available_analyses"
      dependencies:
        event_system_dependency: "event_system"
      config:
        completion_criteria:
          required_events: ["semantic_completed", "complexity_completed", "domain_completed"]
          minimum_confidence_threshold: 0.6
          timeout: 300  # 5 minutes max
          partial_analysis_handling: "use_available_proceed_with_selection"

        event_aggregation:
          data_mapping_strategy: "merge_analysis_results"
          confidence_calculation: "weighted_average"
          correlation_timeout_recovery: "use_partial_proceed_with_selection"

        validation:
          cross_result_validation: true
          consistency_check: true
          anomaly_detection: true

        error_handling:
          missing_events_handling: "use_available_analyses"
          timeout_handling: "partial_analysis_proceed"
          error_events: true
          recovery_events: true

        event_output:
          when_complete:
            event_type: "task.agent.selection.ready"
            data: "aggregated_analysis_results"
          when_partial:
            event_type: "task.agent.selection.ready"
            data: "partial_analysis_results"
            warning: "Some analyses failed - proceeding with available data"

      output:
        aggregation_complete: "boolean"
        analysis_results: "object"
        partial_analysis_detected: "boolean"
        timeout_occurred: "boolean"
        aggregated_confidence: "float"
        processing_summary: "object"
        events_received: "array"
        correlation_id: "string"

    # === EVENT-DRIVEN AGENT SELECTION (Priority 15.6) ===

    - name: "event_driven_agent_selection"
      priority: 15.6
      method: "agent_selection_on_analysis_complete"
      event_subscription:
        listen_to: "task.agent.selection.ready"
        correlation_field: "task_id"
        processing_mode: "sequential"
      dependencies:
        agent_registry_dependency: "agent_registry_construction"
        competency_matching_dependency: "agent_competency_matching"
        threshold_standards_dependency: "system_threshold_standards"
      config:
        input_data:
          semantic_analysis: "event.data.semantic_results"
          complexity_assessment: "event.data.complexity_results"
          domain_classification: "event.data.domain_results"
          aggregated_confidence: "event.data.aggregated_confidence"

        selection_process:
          competency_matching:
            use_domain_classification: true
            complexity_adjustment: true
            semantic_boosting: true
            aggregated_confidence_weighting: true

          selection_algorithm:
            scoring_method: "weighted_competency_score"
            backup_option_generation: true
            confidence_threshold_adjustment: true

          validation:
            cross_reference_check: true
            availability_verification: true
            compatibility_validation: true

        event_output:
          event_type: "task.agent.selected"
          data_mapping:
            task_id: "correlation_id"
            selected_agent: "selection_results.agent"
            confidence: "selection_results.confidence"
            backup_options: "selection_results.backup_options"
            selection_rationale: "selection_results.rationale"
            analysis_summary: "input_data"

        error_handling:
          selection_failure:
            fallback_to: "basic_keyword_selection"
            confidence_adjustment: -0.3
            error_event_publish: true

          insufficient_agents:
            fallback_to: "builtin_agent_pool"
            user_notification: "Limited agents available - using alternatives"
            error_event_publish: true

          timeout_handling:
            auto_select_best_available: true
            timeout_warning: true

      output:
        selection_completed: "boolean"
        event_published: "boolean"
        selection_results: "object"
        processing_time: "float"

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

    # === ENHANCED ERROR HANDLING & RECOVERY SYSTEM (Priority 36) ===

    - name: "error_recovery_handler"
      priority: 36
      method: "event_based_error_recovery"
      event_subscription:
        listen_to: ["task.analysis.error", "task.selection.error", "task.processing.timeout", "task.agent.unavailable"]
        correlation_field: "task_id"
        error_handling_priority: "critical"
      dependencies:
        fallback_system_dependency: "error_system_initialization"
        monitoring_dependency: "monitoring_minimal_setup"
      config:
        recovery_strategies:
          semantic_analysis_failure:
            fallback_to: "keyword_based_analysis"
            confidence_adjustment: -0.2
            processing_time_adjustment: "+5s"
            recovery_event: "task.analysis.recovered"

          complexity_assessment_failure:
            fallback_to: "basic_complexity_scoring"
            use_domain_heuristics: true
            confidence_adjustment: -0.3
            recovery_event: "task.analysis.recovered"

          domain_classification_failure:
            fallback_to: "keyword_domain_matching"
            confidence_adjustment: -0.3
            recovery_event: "task.analysis.recovered"

          agent_selection_failure:
            fallback_to: "builtin_agent_fallback"
            available_agents: ["general_developer", "system_analyst", "quality_assurance"]
            user_notification: "Specialized agents unavailable. Using general-purpose alternatives."
            recovery_event: "task.agent.fallback_selected"

          timeout_handling:
            partial_analysis_proceed: true
            missing_analysis_estimation: "domain_based_defaults"
            timeout_extension: false
            recovery_event: "task.processing.timeout_resolved"

        recovery_events:
          event_type: "task.analysis.recovered"
          data_mapping:
            task_id: "correlation_id"
            recovered_analysis: "recovery_results"
            original_error: "error_data"
            recovery_method: "strategy_used"
            adjusted_confidence: "confidence_level"
            processing_time: "recovery_processing_time"

        error_analysis:
          pattern_recognition: true
          failure_trend_analysis: true
          root_cause_identification: true
          prevention_recommendations: true

        monitoring_integration:
          error_logging: true
          performance_impact_tracking: true
          recovery_success_metrics: true
          failure_pattern_alerts: true

      output:
        error_handled: "boolean"
        recovery_successful: "boolean"
        error_details: "object"
        recovery_strategy_used: "string"
        adjusted_confidence: "float"
        recovery_processing_time: "float"

    - name: "timeout_handler"
      priority: 36.1
      method: "event_based_timeout_resolution"
      event_subscription:
        listen_to: "task.processing.timeout"
        correlation_field: "task_id"
        timeout_handling_priority: "high"
      config:
        timeout_types:
          analysis_timeout:
            threshold: 60  # 1 minute
            action: "proceed_with_available_analyses"
            partial_results_handling: true

          selection_timeout:
            threshold: 30  # 30 seconds
            action: "auto_select_best_available"
            confidence_adjustment: -0.1

          execution_timeout:
            threshold: 600  # 10 minutes
            action: "escalate_to_user"
            provide_partial_results: true

        timeout_recovery:
          graceful_degradation: true
          partial_result_utilization: true
          user_notification: true
          alternative_execution_paths: true

        monitoring:
          timeout_pattern_detection: true
          performance_optimization_suggestions: true
          resource_adjustment_recommendations: true

      output:
        timeout_resolved: "boolean"
        partial_results_provided: "boolean"
        recovery_action_taken: "string"
        remaining_timeout_adjustment: "float"

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
    # Task execution outputs
    selected_agent: "string"
    execution_plan: "array"
    confidence_score: "float"
    estimated_time: "string"
    parallel_groups: "array"
    mcp_tools_required: "array"
    monitoring_metrics: "object"

    # System readiness outputs
    system_greeting: "object"
    agent_categories: "object"
    mcp_server_categories: "object"
    system_capabilities: "object"
    readiness_summary: "object"

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

# === HYBRID EVENT-DRIVEN ARCHITECTURE ===

event_system:
  enabled: true
  hybrid_mode: true  # Priority-based for system phases, event-driven for task processing

  # System Lifecycle Events (Priority-based execution)
  system_lifecycle_events:
    system.readiness.verified:
      description: "System readiness check completed successfully"
      data_fields: ["system_id", "readiness_score", "health_status", "timestamp", "components_ready"]
      handlers: ["greeting_formation_engine", "capability_announcement"]
      priority: "critical"
      activation_condition: "final_readiness_check.complete"

    system.discovery.completed:
      description: "System component discovery phase completed"
      data_fields: ["discovery_id", "agents_found", "mcp_servers_found", "registry_status", "timestamp"]
      handlers: ["system_integration_phase", "monitoring_system"]
      priority: "high"

    system.integration.complete:
      description: "System integration and validation completed"
      data_fields: ["integration_id", "integration_results", "validation_status", "timestamp"]
      handlers: ["system_readiness_phase", "performance_optimizer"]
      priority: "high"

    greeting.generation.started:
      description: "Greeting formation process initiated"
      data_fields: ["greeting_id", "data_sources", "template_type", "timestamp"]
      handlers: ["monitoring_system", "performance_tracker"]
      priority: "medium"

    greeting.categorization.completed:
      description: "Agent and MCP server categorization completed"
      data_fields: ["greeting_id", "agent_categories", "mcp_categories", "uncategorized_items", "timestamp"]
      handlers: ["template_engine", "performance_optimizer"]
      priority: "high"

    greeting.template.generated:
      description: "Greeting template generated with categorized content"
      data_fields: ["greeting_id", "template_content", "category_counts", "performance_summary", "timestamp"]
      handlers: ["integrated_system_readiness_display", "capability_announcement"]
      priority: "high"

    greeting.display.ready:
      description: "Integrated system display ready for user presentation"
      data_fields: ["greeting_id", "display_content", "ready_content", "generation_metadata", "timestamp"]
      handlers: ["capability_announcement", "user_interface_system"]
      priority: "critical"

  task_processing_events:
    # Core task lifecycle events
    task.received:
      description: "Task received from user, starts parallel analysis"
      data_fields: ["task_id", "description", "metadata", "timestamp", "user_id"]
      handlers: ["task_analysis_coordinator", "monitoring_system"]
      priority: "high"

    # Agent discovery events
    agent.discovery.started:
      description: "Dynamic agent discovery process started"
      data_fields: ["discovery_id", "methods", "timestamp", "scope"]
      handlers: ["dynamic_agent_discovery_phase", "monitoring_system"]
      priority: "medium"

    agent.discovery.method.completed:
      description: "Individual discovery method completed"
      data_fields: ["discovery_id", "method_name", "agents_found", "confidence", "processing_time"]
      handlers: ["agent_capability_analysis", "progress_tracker"]
      priority: "medium"

    agent.registry.updated:
      description: "Agent registry updated with new discoveries"
      data_fields: ["registry_version", "agents_added", "agents_removed", "optimizations"]
      handlers: ["agent_competency_matching", "system_integration_phase"]
      priority: "high"

    task.analysis.started:
      description: "Individual analysis component started"
      data_fields: ["task_id", "analysis_type", "start_time", "correlation_id"]
      handlers: ["monitoring_system", "performance_tracker"]
      priority: "medium"

    # Analysis completion events (parallel processing)
    task.semantic.completed:
      description: "Semantic analysis completed successfully"
      data_fields: ["task_id", "semantic_vector", "domain_indicators", "confidence", "processing_time"]
      handlers: ["analysis_completion_aggregator", "domain_validator"]
      priority: "high"

    task.complexity.completed:
      description: "Complexity assessment completed successfully"
      data_fields: ["task_id", "complexity_score", "factors", "confidence", "processing_time"]
      handlers: ["analysis_completion_aggregator", "resource_planner"]
      priority: "high"

    task.domain.completed:
      description: "Domain classification completed successfully"
      data_fields: ["task_id", "primary_domain", "confidence", "secondary_domains", "processing_time"]
      handlers: ["analysis_completion_aggregator", "competency_matcher"]
      priority: "high"

    # Agent selection events
    task.agent.selection.ready:
      description: "All analyses completed, ready for agent selection"
      data_fields: ["task_id", "analysis_complete", "selection_ready", "aggregated_results"]
      handlers: ["event_driven_agent_selection"]
      priority: "critical"

    task.agent.selected:
      description: "Agent selected for task execution"
      data_fields: ["task_id", "selected_agent", "confidence", "backup_options", "selection_rationale"]
      handlers: ["clarification_subsystem", "delegation_engine", "monitoring_system"]
      priority: "critical"

    task.clarification.completed:
      description: "Clarification process completed"
      data_fields: ["task_id", "clarified_requirements", "confidence_level", "ambiguity_resolved"]
      handlers: ["todo_generation_system", "execution_planner"]
      priority: "high"

    # Error and recovery events
    task.analysis.error:
      description: "Error occurred during analysis"
      data_fields: ["task_id", "analysis_type", "error_code", "error_message", "timestamp"]
      handlers: ["error_recovery_handler", "fallback_system"]
      priority: "critical"

    task.processing.timeout:
      description: "Task processing exceeded timeout"
      data_fields: ["task_id", "timeout_type", "elapsed_time", "completed_analyses"]
      handlers: ["timeout_handler", "partial_analysis_processor"]
      priority: "critical"

  event_correlation:
    task_id_based:
      strategy: "correlation_by_task_id"
      timeout: 300  # 5 minutes max for all analyses
      completion_criteria: "semantic_completed && complexity_completed && domain_completed"
      correlation_field: "task_id"

    parallel_analysis_coordination:
      strategy: "parallel_then_select"
      max_parallel_analyses: 3
      coordination_logic: "wait_for_all_analyses_before_selection"
      timeout_handling: "proceed_with_available_analyses"

    event_aggregation:
      data_mapping_strategy: "merge_analysis_results"
      confidence_calculation: "weighted_average"
      timeout_recovery: "use_partial_proceed_with_selection"

  event_routing:
    priority_based_routing:
      enabled: true
      critical_events: ["task.agent.selected", "task.processing.timeout", "task.analysis.error"]
      high_priority_queue: true

    correlation_routing:
      enabled: true
      correlation_field: "task_id"
      routing_strategy: "same_task_id_to_same_handler"

    load_balancing:
      enabled: true
      strategy: "round_robin_within_priority"
      handler_health_monitoring: true
