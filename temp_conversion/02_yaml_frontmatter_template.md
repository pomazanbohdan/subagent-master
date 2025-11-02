---
# YAML Frontmatter Template for Master Agent
# Optimize metadata structure while maintaining all essential information

# Basic Information
name: "{{AGENT_NAME}}"
description: "{{COMPACT_DESCRIPTION}}"
version: "{{VERSION_NUMBER}}"
author: "{{AUTHOR_NAME}}"

# Capabilities - Grouped by category for better organization
capabilities:
  orchestration:
    - "task-orchestration"
    - "automatic-delegation"
    - "agent-selection"
    - "workflow-management"

  planning:
    - "task-planning"
    - "complexity-analysis"
    - "task-breakdown"
    - "dependency-analysis"

  execution:
    - "parallel-execution"
    - "interactive-workflow"
    - "hybrid-workflow"
    - "todo-coordination"

  intelligence:
    - "dynamic-categorization"
    - "conflict-resolution"
    - "adaptive-algorithms"
    - "self-correction"

# Trigger patterns - Organized by intent type
triggers:
  orchestration: ["orchestrate", "delegate", "coordinate", "manage"]
  analysis: ["analyze", "plan", "breakdown", "complexity"]
  execution: ["execute", "parallel", "team", "multiple"]
  optimization: ["optimize", "improve", "enhance", "streamline"]

# Tool dependencies - Essential tools only
tools:
  core: ["sequential-thinking", "serena"]
  optional: ["context7"]
  fallback: ["native-reasoning"]

# Performance metrics
optimization:
  original_size: "{{ORIGINAL_SIZE_KB}}KB"
  optimized_size: "{{OPTIMIZED_SIZE_KB}}KB"
  reduction: "{{REDUCTION_PERCENTAGE}}%"
  functionality_preserved: true

# Metadata
created: "{{CREATION_DATE}}"
updated: "{{LAST_UPDATE_DATE}}"
tags: {{TAGS_ARRAY}}
category: "{{AGENT_CATEGORY}}"
---

# Template Notes:
# 1. Keep descriptions concise but informative
# 2. Group related capabilities together
# 3. Organize triggers by intent patterns
# 4. Specify essential vs optional tools
# 5. Include optimization metrics
# 6. Use consistent naming conventions
# 7. Maintain backward compatibility