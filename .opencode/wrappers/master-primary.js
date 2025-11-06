const MasterMCPServer = require('../../agents/master');
const path = require('path');

class MasterPrimaryAgent {
  constructor() {
    this.mcpServer = new MasterMCPServer();
    this.initialized = false;
  }
  
  async initialize() {
    if (this.initialized) return;
    
    console.log('🔧 Initializing Master Primary Agent...');
    
    // Ініціалізувати MCP сервер
    await this.mcpServer.initialize();
    
    this.initialized = true;
    console.log('✅ Master Primary Agent ready');
  }
  
  async processMessage(message) {
    await this.initialize();
    
    console.log(`📝 Processing: ${message}`);
    
    // Аналіз повідомлення та визначення capability
    const capability = this.detectCapability(message);
    
    if (capability) {
      // Виконати через MCP сервер
      const result = await this.mcpServer.callTool(capability, {
        message,
        timestamp: new Date().toISOString()
      });
      
      return this.formatResponse(result);
    }
    
    // Повернути статус якщо немає конкретної дії
    return this.getStatusResponse();
  }
  
  detectCapability(message) {
    const lowerMessage = message.toLowerCase();
    
    // Простий детектор на основі ключових слів
    const capabilities = {
      'orchestrate': 'unified-task-orchestration',
      'delegate': 'automatic-delegation',
      'plan': 'intelligent-task-planning',
      'parallel': 'advanced-parallel-execution',
      'analyze': 'system-validation',
      'optimize': 'resource-optimization'
    };
    
    for (const [keyword, capability] of Object.entries(capabilities)) {
      if (lowerMessage.includes(keyword)) {
        return capability;
      }
    }
    
    return null;
  }
  
  formatResponse(result) {
    return `🎯 **Master Agent Result**

**Capability:** ${result.capability}
**Status:** ${result.success ? '✅ Success' : '❌ Failed'}
**Result:** ${result.result}
**Timestamp:** ${result.timestamp}

${result.args ? `**Args:** ${JSON.stringify(result.args, null, 2)}` : ''}`;
  }
  
  getStatusResponse() {
    const status = this.mcpServer.getStatus();
    
    return `🤖 **Master Agent Status**

**Status:** ${status.initialized ? '🟢 Ready' : '🔴 Not Initialized'}
**Capabilities:** ${status.capabilities}
**Version:** ${status.version}

Available commands:
- \`orchestrate\` - Orchestrate tasks
- \`delegate\` - Delegate to agents  
- \`plan\` - Create execution plan
- \`parallel\` - Parallel execution
- \`analyze\` - System analysis
- \`optimize\` - Resource optimization`;
  }
}

module.exports = MasterPrimaryAgent;