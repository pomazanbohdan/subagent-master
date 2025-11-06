const MasterPrimaryAgent = require('../wrappers/master-primary');

async function testMasterAgent() {
  console.log('🧪 Testing Master Primary Agent...\n');
  
  const agent = new MasterPrimaryAgent();
  
  // Тест 1: Ініціалізація
  console.log('=== Test 1: Initialization ===');
  await agent.initialize();
  console.log('✅ Initialization test passed\n');
  
  // Тест 2: Статус
  console.log('=== Test 2: Status ===');
  const statusResponse = await agent.processMessage('status');
  console.log(statusResponse);
  console.log('\n');
  
  // Тест 3: Орестрація
  console.log('=== Test 3: Orchestration ===');
  const orchResponse = await agent.processMessage('orchestrate task deployment');
  console.log(orchResponse);
  console.log('\n');
  
  // Тест 4: Паралельне виконання
  console.log('=== Test 4: Parallel Execution ===');
  const parallelResponse = await agent.processMessage('parallel process multiple files');
  console.log(parallelResponse);
  console.log('\n');
  
  console.log('🎉 All tests completed!');
}

// Запустити тест якщо викликано напряму
if (require.main === module) {
  testMasterAgent().catch(console.error);
}

module.exports = testMasterAgent;