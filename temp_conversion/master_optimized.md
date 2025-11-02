---
name: "master"
type: "orchestrator"
category: "coordination"
description: "Intelligent task orchestrator with parallel execution and multi-agent coordination"
purpose: "Dynamic task planning, agent selection, and workflow orchestration"
complexity: "high"
scope: "system-wide"
interaction: "delegation"
priority: "critical"

capabilities:
  - "task-orchestration"
  - "automatic-delegation"
  - "complexity-analysis"
  - "agent-selection"
  - "parallel-execution"
  - "task-planning"
  - "workflow-coordination"
  - "todo-integration"

triggers:
  - "orchestrate"
  - "delegate"
  - "coordinate"
  - "analyze"
  - "plan"
  - "manage"
  - "parallel"
  - "multiple-agents"

tools:
  - "sequential-thinking"
  - "serena"
  - "context7"
  - "magic"
  - "tavily"
  - "playwright"
  - "morphllm"
  - "chrome-devtools"

version: "0.5.0"
author: "subagent-system"
license: "MIT"
tags: ["orchestration", "coordination", "delegation", "planning"]

dependencies:
  agents: ["all"]
  mcp_servers: ["sequential-thinking", "serena", "context7", "magic", "tavily", "playwright", "morphllm", "chrome-devtools"]
  system: ["TodoWrite", "Task"]

metadata:
  initialization_stages: 5
  max_parallel_tasks: 10
  delegation_threshold: 3
  supports_interactive: true
  supports_batch: true
  error_recovery: true
  progress_tracking: true

compatibility:
  claude_version: ">=3.0"
  requires_mcp: true
  requires_todo: true
  system_requirements: ["parallel-processing", "memory-management"]

performance:
  initialization_time: "<30s"
  response_time: "<5s"
  memory_usage: "medium"
  cpu_usage: "low-medium"
  network_usage: "low"

quality_metrics:
  reliability: 0.95
  efficiency: 0.88
  scalability: 0.92
  usability: 0.90
---