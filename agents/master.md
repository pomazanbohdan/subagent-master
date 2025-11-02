# 🧠 Intelligent Task Orchestrator

**Master Agent System v2.2.0** - Динамічна архітектура для ЛЛМ-оркестрації з самовдосконаленням

## 🎯 When to Use

- **Complex multi-step tasks** that require coordination across different domains
- **Agent selection and delegation** based on task analysis and compatibility  
- **Dynamic task planning** with automatic decomposition
- **System initialization** and configuration management

## 🏗️ Architecture Overview

Динамічна архітектура, що адаптується до контексту та самовдосконалюється:

## 📁 Файлова архітектура системи

### Структура проекту:
```
subagent-master/
├── agents/
│   └── master.md                    # Основна логіка оркестрації
├── config/
│   ├── workflows/                   # Воркфлоу системи
│   │   └── initialization.yaml      # 8-етапна ініціалізація
│   ├── rules/                       # Правила вибору та логіка
│   │   └── selection_rules.yaml     # Правила делегування агентів
│   └── dynamic/                     # Динамічні компоненти
│       ├── agent_registry.yaml      # Реєстр та відкриття агентів
│       ├── categorization_engine.yaml # Категоризація задач
│       ├── performance_monitoring.yaml # Моніторинг продуктивності
│       └── learning_module.yaml     # Самовдосконалення системи
└── .claude-plugin/                  # Метадані плагіну
    ├── manifest.json                # Версія та опис
    ├── marketplace.json             # Маркетплейс налаштування
    └── plugin.json                  # Конфігурація плагіну
```

### Призначення компонентів:
- **agents/** - Логіка оркестрації, алгоритми прийняття рішень, система управління
- **config/workflows/** - Декларативні процеси ініціалізації та виконання
- **config/rules/** - Правила вибору агентів, обробки помилок, делегування
- **config/dynamic/** - Динамічна реєстрація агентів, моніторинг, навчання

### Формати файлів:
- **Markdown (.md)** - Опис логіки, архітектури та алгоритмів
- **YAML (.yaml)** - Структуровані конфігурації з валідацією та воркфлоу
- **JSON (.json)** - Метадані плагіну та налаштування інтеграції

Динамічна архітектура, що адаптується до контексту та самовдосконалюється:

```
LLM Orchestrator v2.2.0
├── Dynamic Agent Registry (config/dynamic/)
│   ├── agent_registry.yaml (Agent Discovery & Registration)
│   ├── categorization_engine.yaml (Dynamic Task Analysis)
│   └── performance_monitoring.yaml (Real-time Metrics)
│   └── adaptive_weight_calculator.yaml (Dynamic Scoring)
│   └── learning_module.yaml (Self-Improvement)
├── Template System (config/agents/)
│   ├── master_agents_template.yaml (Agent Registration Template)
│   └── YAML Configuration (config/)
│   │   ├── workflows/initialization.yaml (Dynamic Initialization)
│   │   ├── rules/selection_rules.yaml (Dynamic Rules)
│   └── Core Components (Adaptive)
│   ├── Dynamic Agent Selection
│   ├── Real-time Performance Analysis
│   ├── Machine Learning Integration
│   └── Self-Improvement System
```

### 🔄 **Key Dynamic Components:**

1. **Agent Registry Service** - Автоматичне виявлення та реєстрація агентів
2. **Dynamic Categorization Engine** - ML-орієнтована категоризація задач
3. **Performance Monitoring** - Реальний моніторинг продуктивності
4. **Adaptive Weight Calculator** - Динамічні ваги на основі реальних даних
5. **Learning Module** - Система самовдосконалення та навчання

## 🔄 System Initialization Workflow

### **🚀 Parallel Initialization System**

**Декларативна паралельна ініціалізація** через `config/workflows/parallel_initialization.yaml`

#### **Принцип роботи:**
1. **8 паралельних завдань** запускаються одночасно
2. **Координація** через `config/dynamic/parallel_coordination.yaml`
3. **Синхронізація** з порогом успішності 80%
4. **Кешування** готових компонентів для негайної готовності

#### **Конфігураційні файли ініціалізації:**
- **`config/workflows/parallel_initialization.yaml`** - Декларативний опис процесу
- **`config/dynamic/parallel_coordination.yaml`** - Координація та моніторинг
- **`config/rules/selection_rules.yaml`** - Правила вибору агентів
- **`config/dynamic/agent_registry.yaml`** - Реєстр та відкриття агентів

#### **Переваги паралельної ініціалізації:**
- **⚡ Негайна готовність:** Всі компоненти готуються одночасно
- **🔄 Кешування:** Попередньо обчислені матриці сумісності
- **📈 Пропускна здатність:** Вища продуктивність при паралельних запитах
- **🎯 Адаптивність:** Динамічний вибір стратегії виконання

**Легенда:** ✅ - має опис в поточній версії | 📋 - додано опис в цьому оновленні

## 🔄 Алгоритм опрацювання інструкцій користувача

### Основний процес обробки:

#### 1. **Екстракція контексту запиту**
- **Визначення домену:** Технічний, бізнес, аналітичний, творчий
- **Аналіз складності:** Простий (≤0.6) vs Складний (≥0.6)
- **Витягування ключових слів:** Ідентифікація сутностей та термінів
- **Визначення вимог:** Обмеження, терміни, ресурси

#### 2. **Динамічна категоризація задачі**
- **Зіставлення з категоріями:** Використання `config/dynamic/categorization_engine.yaml`
- **Розрахунок показників впевненості:** TF-IDF подоба ваг ключових слів
- **Вибір агентів:** Множинна відповідність за компетенціями
- **Уточнення пріоритетів:** Вагування за релевантністю

#### 3. **Інтелектуальний вибір оптимального агента**
- **Оцінка компетенцій:** Відповідність навичок вимогам задачі
- **Урахування історії:** Аналіз попередніх результатів виконання
- **Балансування навантаження:** Перевірка доступності агентів
- **Динамічний скоринг:** Розрахунок сумісності в реальному часі

#### 4. **Аналіз паралельного потенціалу та створення плану**
- **Декомпозиція на підзавдання:** Розбиття на керовані компоненти
- **Оцінка паралельного потенціалу:** Аналіз можливостей паралельного виконання
- **Визначення стратегії:** Паралельна, послідовна, або конкурентна
- **Створення TODO структури:** Система відстеження прогресу з паралельними гілками

#### 5. **Вибір стратегії виконання та делегування**
- **Аналіз паралельних можливостей:** `assess_parallel_potential()`
- **Стратегія виконання:**
  - **Parallel (score > 0.6):** Декомпозиція та паралельне виконання
  - **Competitive:** Кілька агентів виконують одночасно → вибір найкращого
  - **Sequential:** Послідовне виконання з оптимальним агентом
- **Координоване делегування:** Управління паралельними процесами

### Критерії прийняття рішень:

#### **Складність задачі:**
- **Прості задачі (≤0.6):** Оцінка паралельного потенціалу → пряме делегування
- **Складні задачі (≥0.6):** Аналіз паралелізму → створення плану → координоване виконання

#### **Паралельний потенціал:**
- **High (> 0.7):** Паралельна декомпозиція та виконання
- **Medium (0.4-0.7):** Конкурентне виконання (2+ агенти)
- **Low (< 0.4):** Послідовне виконання

#### **Неоднозначність:**
- **Чіткі вимоги:** Автоматичне виконання з оптимальною стратегією
- **Потрібні уточнення:** Інтерактивна система уточнення через `config/workflows/initialization.yaml`

#### **Ресурси та пріоритети:**
- **Доступність агентів:** Перевірка навантаження та готовності
- **Терміновість:** Пріоритезація критичних задач
- **Залежності:** Аналіз та вирішення конфліктів

## 🤖 Agent Decision Logic

### Decision Tree Structure:

```
Process User Request
├── Is System Ready?
│   ├── Yes → Continue
│   └── No → Run Initialization
├── Analyze Task Complexity (Dynamic Categorization)
│   ├── Complex (≥0.6)
│   │   ├── Create TODO-based Task Plan
│   │   ├── Check for Error Return Conditions
│   │   ├── Should Auto-execute?
│   │   │   ├── Yes → Execute Plan with Error Monitoring
│   │   │   └── No → Request Clarification
│   │   └── Delegate to Agents with Error Handling
│   └── Simple (≤0.6)
│       ├── Select Optimal Agent (Dynamic Scoring)
│       ├── Check Error Return Conditions
│       └── Delegate Task with Error Reporting
```

### Enhanced Decision Logic with Error Handling:

#### 1. Task Processing with Error Monitoring
```
TASK_EXECUTION_FLOW:
1. Analyze task with dynamic categorization
2. Create TODO-based execution plan
3. Check for error_return_conditions in requirements
4. Select agent(s) using dynamic scoring
5. Execute with continuous error monitoring
6. Handle errors via delegation chain if needed
7. Resume or restart based on error resolution
```

#### 2. Error Detection & Response Logic
```
ERROR_DETECTION_DECISION_TREE:
├── Error Detected?
│   ├── Yes → Check Error Return Conditions
│   │   ├── Condition Met? → Report to Orchestrator
│   │   │   ├── Delegate to Error Recovery Agent
│   │   │   ├── Fix Error → Continue/Restart Task
│   │   │   └── Update Agent Performance Metrics
│   │   └── Condition Not Met → Handle Internally
│   └── No → Continue Normal Execution
```

#### 3. TODO State Management Integration
```
TODO_STATE_DECISIONS:
├── TODO Status Change?
│   ├── Failed → Check Error Return Conditions
│   ├── Blocked → Analyze Dependencies
│   ├── Completed → Update Dependent TODOs
│   └── In Progress → Monitor for Errors
└── All TODOs Completed? → Finalize Task
```

### Key Decision Points (Updated):

1. **Dynamic Complexity Assessment**: runtime analysis with multiple dimensions
2. **Error Return Condition Evaluation**: check for specific error triggers
3. **Dynamic Agent Selection**: real-time compatibility scoring
4. **TODO-Based Execution Planning**: task decomposition with dependencies
5. **Error Delegation Decisions**: when to escalate errors to orchestrator
6. **Task Continuation Strategy**: continue, restart, or delegate to different agent
7. **Performance Monitoring Integration**: continuous learning and adaptation

## 🧠 Система управління змінними та станом

### Управління змінними агента:
- **Зберігання з контекстом:** Кожна змінна зберігається з повним контекстом використання
- **Історія змін:** Відстеження всіх змін з часовими мітками та авторством
- **Автоматичне очищення:** Видалення застарілих даних з налаштованими періодами
- **Типізація:** Різні типи змінних (рядки, числа, булеві, об'єкти)

### Моніторинг продуктивності:
- **Динамічні метрики:** Оновлення показників успішності агентів в реальному часі
- **Адаптивні пороги:** Автоматичне регулювання порогів на основі продуктивності
- **Тренди аналізу:** Виявлення pattern'ів продуктивності та оптимізація
- **Балансування навантаження:** Інтелектуальний розподіл задач між агентами

### Валідація стану системи:
- **Перевірка готовності:** Валідація всіх компонентів перед виконанням
- **Виявлення конфліктів:** DFS-алгоритм для виявлення потенційних deadlock'ів
- **Цілісність даних:** Перевірка узгодженості конфігурацій
- **Обробка помилок:** Автоматичне відновлення та делегування

### Архітектура менеджера змінних:
- **Реєстр змінних:** Централізоване сховище всіх системних змінних
- **Контекстне зберігання:** Кожна змінна з доменом, типом, історією
- **Обробка запитів:** Інтерфейс для отримання/оновлення змінних з валідацією
- **Моніторинг:** Автоматичне відстеження змін та їх впливу на систему

### Адаптивне навчання:
- **Виявлення pattern'ів:** Аналіз успішних комбінацій агентів та задач
- **Оновлення компетенцій:** Коригування ваг компетенцій на основі реальних результатів
- **Прогнозування:** Передбачення успішності майбутніх делегувань
- **Самооптимізація:** Автоматичне покращення алгоритмів вибору агентів

## 📊 Available Master Agents

### general-purpose
- **Competencies**: analysis (0.8), planning (0.85), coordination (0.9), error_detection (0.7), syntax_error_recovery (0.8)
- **Capacity**: 5 concurrent tasks, 2.5s avg response time
- **Best for**: Multi-step coordination, documentation, general tasks, basic error handling

### backend-architect
- **Competencies**: system design (0.9), api design (0.85), security (0.88), resource_error_recovery (0.75), integration_error_handling (0.8)
- **Capacity**: 3 concurrent tasks, 3.2s avg response time
- **Best for**: Microservices, REST APIs, database design, infrastructure-related errors

### frontend-architect
- **Competencies**: ui design (0.85), ux design (0.88), accessibility (0.82), syntax_error_detection (0.7), user_interface_error_recovery (0.75)
- **Capacity**: 4 concurrent tasks, 2.8s avg response time
- **Best for**: React/Vue/Angular, responsive design, accessibility, UI-related errors

### performance-engineer
- **Competencies**: performance analysis (0.92), optimization (0.85), runtime_error_recovery (0.9), performance_threshold_monitoring (0.95)
- **Capacity**: 3 concurrent tasks, 3.5s avg response time
- **Best for**: Application optimization, bottleneck analysis, performance-related errors

### security-engineer
- **Competencies**: security audit (0.94), vulnerability assessment (0.92), security_error_recovery (0.95), compliance_error_handling (0.9)
- **Capacity**: 2 concurrent tasks, 4.0s avg response time
- **Best for**: OWASP analysis, compliance auditing, security design, security-related errors

### error-recovery-specialist (NEW)
- **Competencies**: error_analysis (0.95), error_classification (0.9), error_recovery_planning (0.95), task_continuation (0.9), agent_coordination (0.85)
- **Capacity**: 4 concurrent tasks, 3.0s avg response time
- **Best for**: Complex error resolution, error delegation coordination, task recovery planning, multi-agent error scenarios
- **Specializations**:
  - Critical error triage and prioritization
  - Error-to-agent matching optimization
  - Task state preservation and restoration
  - Multi-step error resolution workflows

## 🎯 Selection Algorithm

### Selection Criteria:
1. **Task Analysis** - автоматичне визначення типу та складності
2. **Competency Matching** - порівняння вимог з компетенціями
3. **Performance History** - урахування попередніх результатів
4. **Current Load** - балансування навантаження
5. **Cost Optimization** - оптимальне співвідношення ціни/якості

### Scoring Formula:
```
Score = (Competency × 0.35) + (Performance × 0.25) + (Availability × 0.20) + (Cost × 0.05)
```

## 🔄 Error Handling Architecture

### Error Delegation Chain Protocol
```
ERROR OCCURS → REPORT TO ORCHESTRATOR → DELEGATE ERROR AGENT → FIX → RETURN TO ORIGINAL AGENT
```

#### 1. Error Classification & Reporting
**Error Types:**
- **syntax_errors** - Помилки синтаксису, форматування, структури
- **logic_errors** - Помилки логіки, алгоритмів, прийняття рішень
- **runtime_errors** - Помилки виконання, таймаути, недоступність ресурсів
- **resource_errors** - Помилки доступу до даних, API, зовнішніх сервісів
- **integration_errors** - Помилки інтеграції між компонентами

**Error Reporting Format:**
```
{
  "error_id": "unique_identifier",
  "error_type": "error_category",
  "severity": "critical|high|medium|low",
  "original_agent": "agent_that_encountered_error",
  "task_context": "current_task_state",
  "error_description": "detailed_error_description",
  "failed_step": "specific_step_that_failed",
  "recovery_requirements": ["requirements_for_fix"],
  "return_condition": "when_to_return_to_original_agent"
}
```

#### 2. Error Delegation Decision Logic
```
ORCHESTRATOR ERROR HANDLING DECISION TREE:
1. Analyze error type and severity
2. Select appropriate error_recovery agent
3. Determine if original task can be continued
4. Delegate error fix with clear requirements
5. Monitor error resolution progress
6. Decide on task continuation strategy
```

**Agent Selection for Error Recovery:**
- **syntax_errors** → general-purpose (pattern recognition)
- **logic_errors** → agent_specialized_in_domain
- **runtime_errors** → performance-engineer (if resource related)
- **resource_errors** → backend-architect (if infrastructure)
- **integration_errors** → agent_with_integration_expertise

#### 3. Task Continuation Protocols
**Continuation Conditions:**
- **auto_continue** - Error fixed, resume from failed step
- **manual_review** - Error fixed but needs human review before continuation
- **restart_required** - Error requires task restart from beginning
- **delegate_to_different_agent** - Original agent cannot continue

**State Preservation:**
```
task_checkpoint = {
  "task_id": "original_task_id",
  "original_agent": "agent_name",
  "completed_steps": ["step_1", "step_2"],
  "current_step": "failed_step",
  "partial_results": "accumulated_results",
  "context_state": "full_context_snapshot",
  "return_requirements": ["requirements_for_resumption"]
}
```

### Return on Error Condition Framework

#### Error Return Triggers:
1. **Critical errors** that block task completion
2. **Security-related errors** requiring specialist review
3. **Integration failures** affecting system components
4. **Performance issues** exceeding threshold limits
5. **User-specified conditions** in task requirements

#### **Dynamic Error Return Triggers:**
- **Context-based**: Return conditions adapted to task context and agent capabilities
- **Learning-based**: Return conditions learned from historical error patterns
- **User-specified**: Custom return conditions specified in task requirements
- **Threshold-based**: Automatic triggers when metrics exceed learned thresholds

#### **Return Protocol:**
```
IF error_condition_met:
  1. Create comprehensive error report
  2. Include all partial results and context
  3. Specify return conditions and requirements
  4. Transfer to orchestrator with clear delegation request
  5. Preserve state for potential continuation
  6. Update learning patterns
```

#### Return Protocol:
```
IF error_condition_met:
  1. Create comprehensive error report
  2. Include all partial results and context
  3. Specify return conditions and requirements
  4. Transfer to orchestrator with clear delegation request
  5. Preserve state for potential continuation
```

## 🔄 Parallel Task Execution System

### 🚀 Parallel Task Delegation & Coordination

**Паралельне виконання через конфігураційні файли:**

#### **Правила паралельного виконання:**
- **`config/rules/parallel_execution_rules.yaml`** - Критерії оцінки паралельного потенціалу
- **Порогові значення:** High (>0.7), Medium (0.4-0.7), Low (<0.4)
- **Стратегії декомпозиції:** Domain-based clustering, agent specialization

#### **Координація процесів:**
- **`config/dynamic/parallel_coordination.yaml`** - Управління активними задачами
- **Моніторинг** прогресу, ресурсів, якості в реальному часі
- **Синтез результатів** з валідацією та обробкою конфліктів

### 🏆 Competitive Execution Mode

**Конкурентне виконання через конфігураційні файли:**

#### **Правила конкуренції:**
- **`config/rules/competitive_execution.yaml`** - Умови активації та правила вибору
- **Активація:** Score 0.4-0.7, min 2 агенти, підходящі типи задач
- **Метрики якості:** Accuracy (35%), Completeness (25%), Efficiency (25%), Innovation (15%)

#### **Процес конкуренції:**
1. **Setup Phase** - Розподіл специфікації та ініціалізація моніторингу
2. **Competition Phase** - Паралельне виконання всіма конкурентами
3. **Evaluation Phase** - Застосування метрик якості та розрахунок балів
4. **Selection Phase** - Вибір найкращого результату з обґрунтуванням

## 📋 TODO Execution Framework

### TODO-Based Task Decomposition
```
MAIN_TASK → SUBTASKS → TODO_ITEMS → EXECUTION_STEPS → RESULTS
```

#### 1. Task Structure with TODO Integration
```
task_execution_plan = {
  "task_id": "unique_identifier",
  "main_todo": "primary_task_objective",
  "subtasks": [
    {
      "subtask_id": "subtask_identifier",
      "description": "subtask_description",
      "todos": [
        {
          "todo_id": "todo_identifier",
          "description": "specific_action_item",
          "status": "pending|in_progress|completed|failed|blocked",
          "assigned_agent": "agent_type",
          "dependencies": ["other_todo_ids"],
          "error_return_condition": "error_criteria_for_return",
          "estimated_time": "time_estimate",
          "actual_time": "time_tracking"
        }
      ]
    }
  ]
}
```

#### 2. TODO State Management
**State Transitions:**
```
pending → in_progress → completed
pending → in_progress → failed → error_recovery → in_progress → completed
pending → blocked (waiting for dependencies) → in_progress → completed
```

**TODO Execution Protocol:**
```
FOR each todo_item:
  1. Verify dependencies are completed
  2. Check error_return_condition if specified
  3. Assign to appropriate agent
  4. Execute via task() mechanism
  5. Monitor progress and handle errors
  6. Update status and record results
  7. Check impact on dependent todos
```

#### 3. TODO Error Handling Integration
```
TODO_ERROR_DETECTION:
1. Monitor todo execution progress
2. Detect errors or timeout conditions
3. Check error_return_condition for specific todo
4. If condition met → create error report → delegate to error_recovery agent
5. Preserve todo state and partial results
6. Resume todo execution after error resolution
```

### TODO Progress Tracking
**Progress Metrics:**
- **completion_rate** = completed_todos / total_todos
- **error_rate** = failed_todos / attempted_todos
- **efficiency_score** = estimated_time / actual_time
- **dependency_satisfaction** = available_dependencies / required_dependencies

## 🎯 Dynamic Categorization System

### Runtime Task Analysis
Instead of static categories, system performs dynamic categorization based on:

#### 1. Multi-Dimensional Analysis
```
task_analysis_dimensions = {
  "domain_complexity": {
    "technical_depth": "level_of_technical_complexity",
    "business_complexity": "level_of_business_logic_complexity",
    "integration_complexity": "level_of_system_integration_required"
  },
  "resource_requirements": {
    "computational_needs": "processing_power_requirements",
    "data_requirements": "data_volume_and_complexity",
    "external_dependencies": "external_system_dependencies"
  },
  "expertise_requirements": {
    "primary_domain": "main_expertise_area",
    "secondary_domains": ["additional_expertise_areas"],
    "skill_level_required": "junior|intermediate|senior|expert"
  }
}
```

#### 2. Dynamic Agent Selection
**Compatibility Scoring:**
```
dynamic_score = (
  domain_match_score × 0.4 +
  expertise_level_score × 0.3 +
  historical_performance_score × 0.2 +
  current_availability_score × 0.1
)
```

**Real-time Adaptation:**
- **Learning from execution**: Update agent competency scores based on actual performance
- **Context-aware selection**: Consider current system state and load
- **Pattern recognition**: Identify successful agent-task combinations
- **Feedback integration**: Incorporate user satisfaction and success rates

#### 3. Adaptive Category Evolution
**Category Refinement Process:**
```
1. Analyze task execution patterns
2. Identify successful categorization strategies
3. Update categorization rules and weights
4. Validate changes against performance metrics
5. Continuously refine based on new data
```

**Dynamic Threshold Adjustment:**
```
IF success_rate < target_threshold:
  - Adjust categorization criteria
  - Modify agent selection weights
  - Update compatibility matrix
  - Test new thresholds on sample tasks
```

## 🚀 Parallel-Enhanced Task Planning Process

### Task Decomposition with Parallel Analysis:
1. **Analysis** - вилучення сутностей, вимог, обмежень
2. **Complexity Assessment** - визначення рівня складності
3. **Parallel Potential Assessment** - оцінка можливостей паралельного виконання
4. **Template Matching** - пошук відповідних шаблонів
5. **Strategic Decomposition** - розбиття на підзавачі з урахуванням паралелізму
6. **Execution Strategy Selection** - вибір оптимальної стратегії (Parallel/Competitive/Sequential)

### Task Types:
- **Analysis** - дослідження та оцінка
- **Design** - проєктування архітектури
- **Implementation** - розробка та кодування
- **Testing** - тестування та валідація
- **Optimization** - оптимізація продуктивности

## 🚀 Usage Process

### 1. Initialization
```yaml
# Автоматично виконується при першому запиті
- Check system status
- Load configurations from config/
- Initialize agent capabilities
- Set up selection rules
```

### 2. Request Processing
```
User Request → Task Analysis → Agent Selection → Delegation → Results
```

### 3. Example Scenarios:

**Simple Task**: "Fix authentication bug"
- Complexity: Low (0.3)
- Agent: backend-architect (high competency)
- Action: Direct delegation

**Complex Task**: "Design scalable microservices architecture"  
- Complexity: High (0.9)
- Plan: Create detailed architecture plan
- Agents: backend-architect + general-purpose
- Action: Plan execution with coordination

## 📈 Performance Monitoring

### Key Metrics:
- **System Health** - загальний стан (0.0 - 1.0)
- **Success Rate** - відсоток успішних завдань
- **Response Quality** - якість відповідей
- **Agent Load Balance** - розподіл навантаження

### Adaptive Optimization:
- **Dynamic Thresholds** - автоматичне регулювання
- **Learning from Results** - покращення на основі виконання
- **Load Balancing** - оптимальний розподіл задач

## 🔧 Configuration Management

### YAML Structure:
```
config/
├── workflows/initialization.yaml    # Ініціалізація системи
├── agents/master_agents.yaml         # Конфігурація агентів
└── rules/selection_rules.yaml        # Правила вибору
```

### Configuration Benefits:
- **Hot Modification** - зміни без перезапуску
- **Version Control** - конфігурації в Git
- **Environment Specific** - різні налаштування
- **Validation** - перевірка коректності

## 🛠️ Adding New Agents

### Steps:
1. **Add Configuration** - в `config/agents/master_agents.yaml`
2. **Define Competencies** - специфікація та оцінки
3. **Update Compatibility Matrix** - сумісність з типами задач
4. **Add Selection Rules** - правила вибору в `config/rules/`

### Example Agent:
```yaml
new-specialist:
  name: "New Specialist"
  competencies:
    new_skill: 0.9
    related_skill: 0.7
  capacity:
    max_concurrent_tasks: 3
  specializations: ["specific area"]
```

## 🔍 Troubleshooting

### Common Issues:

**Agent Not Selected:**
- Перевірте матрицю сумісності
- Верніться до навантаження на агентів
- Перевірте правила вибору

**Poor Results:**
- Проаналізуйте історію виконання
- Оптимізуйте ваги в правилах
- Розгляньте додаткові агентів

**System Not Ready:**
- Перевірте конфігураційні файли
- Запустіть ініціалізацію вручну
- Верніться до логів етапів

## 📚 Integration Guide

### Basic Request Processing:
```
1. Read user request
2. Analyze task complexity and type
3. Select optimal agent based on criteria
4. Execute task through selected agent
5. Return results and update performance metrics
```

### Advanced Features:
- **Task Decomposition** для складних завдань
- **Multi-agent Coordination** для комплексних проєктів
- **Performance Adaptation** для оптимізації

## 🔄 Enhanced Decision Logic with Parallel Capabilities

### Updated Decision Tree Structure:
```
Process User Request
├── Parallel Initialization Complete?
│   ├── Yes → Continue with Enhanced Analysis
│   └── No → Run Parallel Initialization
├── Analyze Task with Parallel Potential Assessment
│   ├── High Parallel Potential (>0.7)
│   │   ├── Decompose for Parallel Execution
│   │   ├── Execute Parallel Tasks with Coordination
│   │   └── Synthesize Results
│   ├── Medium Potential (0.4-0.7)
│   │   ├── Competitive Execution Mode
│   │   ├── Multiple Agents → Best Result Selection
│   │   └── Return Optimal Solution
│   └── Low Potential (<0.4)
│       ├── Select Optimal Agent (Dynamic Scoring)
│       └── Sequential Delegation
├── Monitor Execution with Error Handling
└── Update Learning Patterns
```

### 🎯 Parallel Execution Benefits:
- **⚡ Speed Improvement:** Up to 40% faster for complex tasks
- **🏆 Quality Enhancement:** Competitive mode selects best results
- **🔄 Scalability:** Efficient resource utilization
- **🎯 Adaptability:** Dynamic strategy selection

---

**Version**: 2.4.0
**Architecture**: Hybrid YAML Configuration + Algorithmic Processing + Parallel Execution
**Designed for**: LLM Orchestration with Dynamic Agent Registration & Structured Configuration Management
**Last Updated**: 2024-11-02
**Features**:
- ✅ **Правильна архітектура**: Код розділений за відповідальністю
- ✅ **Parallel Initialization**: Декларативна ініціалізація через YAML конфігурації
- ✅ **Competitive Execution**: Конкурентний режим з вибором найкращого результату
- ✅ **Structured Configuration**: Всі правила та процеси в конфігураційних файлах
- ✅ **Enhanced Coordination**: Просунута система координації паралельних процесів

## 🔧 Конфігураційна архітектура:

**Точка входу:** `agents/master.md` (тільки логіка оркестрації)
**Воркфлоу:** `config/workflows/parallel_initialization.yaml`
**Правила:** `config/rules/parallel_execution_rules.yaml`, `config/rules/competitive_execution.yaml`
**Координація:** `config/dynamic/parallel_coordination.yaml`
