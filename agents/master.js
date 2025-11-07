const fs = require('fs');

class MasterMCPServer {
  constructor() {
    this.name = "master-agent";
    this.version = "0.9.10";
    this.masterConfig = null;
    this.initialized = false;
  }
  
  async initialize() {
    if (this.initialized) return;
    
    console.log('🚀 Initializing Master MCP Server...');
    
    // Load configuration from master.md
    const masterPath = './agents/master.md';
    if (!fs.existsSync(masterPath)) {
      throw new Error(`master.md not found at ${masterPath}`);
    }
    
    const masterContent = fs.readFileSync(masterPath, 'utf8');
    console.log(`📖 Loaded ${masterContent.length} characters from master.md`);
    
    this.masterConfig = this.parseMasterMd(masterContent);
    
    this.initialized = true;
    console.log('✅ Master MCP Server initialized');
  }
  
  parseMasterMd(content) {
    try {
      // Try to extract YAML frontmatter if present
      const yamlMatch = content.match(/^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)/);
      if (yamlMatch) {
        console.log('📋 Extracting YAML frontmatter from master.md');
        return this.parseYamlConfiguration(yamlMatch[1], yamlMatch[2]);
      }
      
      // Fallback: parse as structured content
      console.log('🔧 Parsing structured content from master.md');
      return this.parseStructuredContent(content);
      
    } catch (error) {
      console.error('❌ Error parsing master.md:', error);
      console.log('🔧 Falling back to hardcoded configuration');
      return this.getHardcodedConfig();
    }
  }

  parseYamlConfiguration(frontmatter, body) {
    // Simple YAML parsing for key fields
    const config = {
      name: "master",
      description: "An AI agent that optimizes task execution through intelligent planning, parallelization, and execution in subtasks or delegation to existing agents in system",
      capabilities: [],
      triggers: [],
      tools: ["dynamic_agent_discovery"],
      version: "0.9.10"
    };

    // Extract capabilities from various sections
    const capabilityMatches = body.match(/capabilities:\s*\n((?:\s*-[^\n]*\n)+)/g);
    if (capabilityMatches) {
      capabilityMatches.forEach(match => {
        const capLines = match.match(/\s*-\s*([^\n]+)/g);
        if (capLines) {
          capLines.forEach(line => {
            const cap = line.replace(/\s*-\s*/, '').trim();
            if (cap && !config.capabilities.includes(cap)) {
              config.capabilities.push(cap);
            }
          });
        }
      });
    }

    // Extract triggers
    const triggerMatches = body.match(/triggers:\s*\[(.*?)\]/s);
    if (triggerMatches) {
      const triggers = triggerMatches[1]
        .replace(/["']/g, '')
        .split(',')
        .map(t => t.trim())
        .filter(t => t);
      config.triggers = triggers;
    }

    // Fallback to hardcoded if no capabilities found
    if (config.capabilities.length === 0) {
      config.capabilities = this.getDefaultCapabilities();
    }

    return config;
  }

  parseStructuredContent(content) {
    // Simple extraction from structured sections
    const config = this.getHardcodedConfig();
    
    // Extract from component section if exists
    const componentMatch = content.match(/component:\s*\n[\s\S]*?name:\s*["']([^"']+)["']/);
    if (componentMatch) {
      config.name = componentMatch[1];
    }
    
    // Extract capabilities from component section
    const capabilitiesSection = content.match(/capabilities:\s*\[([\s\S]*?)\]/);
    if (capabilitiesSection) {
      const caps = capabilitiesSection[1]
        .match(/[^\s,]+/g)
        .filter(cap => cap.length > 0);
      config.capabilities = caps.length > 0 ? caps : config.capabilities;
    }
    
    return config;
  }

  getHardcodedConfig() {
    return {
      name: "master",
      description: "An AI agent that optimizes task execution through intelligent planning, parallelization, and execution in subtasks or delegation to existing agents in system",
      capabilities: [
        "unified-task-orchestration",
        "automatic-delegation",
        "agent-selection",
        "mcp-integration",
        "fallback-handling",
        "intelligent-task-planning",
        "advanced-parallel-execution",
        "dependency-resolution",
        "dynamic-scheduling",
        "deadlock-avoidance",
        "resource-optimization",
        "real-time-adaptation",
        "configuration-management",
        "agent-discovery",
        "resource-management",
        "performance-monitoring",
        "system-validation",
        "task-execution",
        "tool-selection",
        "mandatory-tool-enforcement",
        "automatic-tool-selection",
        "compliance-monitoring",
        "execution-authorization",
        "tool-decision-matrix",
        "intelligent-workflow-routing"
      ],
      triggers: [
        "orchestrate", "delegate", "analyze", "plan", "coordinate", "manage", 
        "parallel", "team", "multiple-agents", "clarify", "search", "research"
      ],
      tools: ["dynamic_agent_discovery"],
      version: "0.9.10"
    };
  }

  getDefaultCapabilities() {
    return [
      "unified-task-orchestration",
      "automatic-delegation", 
      "agent-selection",
      "mcp-integration",
      "fallback-handling",
      "intelligent-task-planning",
      "advanced-parallel-execution"
    ];
  }
  
  async listTools() {
    await this.initialize();
    
    return this.masterConfig.capabilities.map(cap => ({
      name: cap,
      description: `Master agent ${cap.replace(/-/g, ' ')} capability`
    }));
  }
  
  async callTool(name, args = {}) {
    await this.initialize();
    
    // Input validation
    if (!name || typeof name !== 'string') {
      throw new Error('Tool name must be a non-empty string');
    }
    
    if (!this.masterConfig || !this.masterConfig.capabilities) {
      throw new Error('Master configuration not loaded');
    }
    
    // Check if capability exists
    if (!this.masterConfig.capabilities.includes(name)) {
      console.warn(`⚠️ Unknown capability: ${name}`);
    }
    
    console.log(`🎯 Executing ${name} with args:`, this.sanitizeArgs(args));
    
    try {
      // Capability execution with improved simulation
      const result = {
        capability: name,
        success: true,
        result: `Executed ${name} successfully`,
        timestamp: new Date().toISOString(),
        args: this.sanitizeArgs(args),
        validation: {
          input_validated: true,
          capability_recognized: this.masterConfig.capabilities.includes(name)
        }
      };
      
      return result;
    } catch (error) {
      console.error(`❌ Error executing ${name}:`, error);
      return {
        capability: name,
        success: false,
        error: error.message,
        timestamp: new Date().toISOString(),
        args: this.sanitizeArgs(args)
      };
    }
  }

  sanitizeArgs(args) {
    // Sanitize arguments to prevent injection
    if (!args || typeof args !== 'object') {
      return {};
    }
    
    const sanitized = {};
    for (const [key, value] of Object.entries(args)) {
      // Only allow safe string values
      if (typeof value === 'string') {
        sanitized[key] = value.replace(/[<>\"']/g, '').substring(0, 1000);
      } else if (typeof value === 'number' && isFinite(value)) {
        sanitized[key] = value;
      } else if (typeof value === 'boolean') {
        sanitized[key] = value;
      } else {
        // Skip potentially dangerous values
        console.warn(`⚠️ Skipping unsafe argument: ${key}`);
      }
    }
    
    return sanitized;
  }
  
  getStatus() {
    return {
      initialized: this.initialized,
      capabilities: this.masterConfig?.capabilities?.length || 0,
      version: "0.9.10"
    };
  }
}

module.exports = MasterMCPServer;