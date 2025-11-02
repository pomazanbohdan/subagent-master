"""
Interactive Clarification System
Context-aware clarification with adaptive question generation for ambiguous tasks.
"""


def determine_need_for_clarification(task_description, task_context, complexity_score):
    """Determine if task needs user clarification"""
    ambiguity_indicators = {
        'high_ambiguity': ['unclear', 'maybe', 'possibly', 'think about', 'consider'],
        'missing_requirements': ['requirements', 'specifications', 'details needed'],
        'multiple_approaches': ['ways', 'methods', 'approaches', 'options', 'alternatives'],
        'undefined_scope': ['scope', 'boundaries', 'limitations', 'constraints']
    }

    ambiguity_score = calculate_ambiguity_score(task_description, ambiguity_indicators)

    # Clarification needed for:
    # - Complex tasks (complexity ≥ 3) with high ambiguity
    # - Any tasks with critical missing requirements
    return (complexity_score >= 3 and ambiguity_score > 0.6) or ambiguity_score > 0.8


def generate_contextual_questions(task_description, task_context, complexity_score):
    """Generate context-specific clarification questions"""
    task_type = detect_task_type(task_description)

    question_templates = {
        'development': [
            "Which technology stack should be used for this implementation?",
            "What are the scalability requirements for this solution?",
            "Are there specific coding standards or architectural patterns to follow?",
            "What are the performance constraints or benchmarks?"
        ],
        'analysis': [
            "What specific aspects should be analyzed in detail?",
            "Are there particular metrics or criteria of interest?",
            "What sources or data should be considered in the analysis?",
            "What format should the analysis results take?"
        ],
        'optimization': [
            "What are the current performance metrics or baselines?",
            "Which areas need priority optimization?",
            "Are there constraints on changes to the existing system?",
            "What are the target improvement goals?"
        ],
        'integration': [
            "Which systems or services need to be integrated?",
            "What are the API specifications or data formats?",
            "Are there security or compliance requirements?",
            "What error handling or fallback mechanisms are needed?"
        ]
    }

    return question_templates.get(task_type, generate_general_questions(task_context))


# Helper functions (to be implemented)
def calculate_ambiguity_score(task_description, indicators):
    """Calculate ambiguity score based on task description"""
    # TODO: Implement ambiguity scoring algorithm
    task_lower = task_description.lower()
    score = 0
    
    for category, keywords in indicators.items():
        matches = sum(1 for keyword in keywords if keyword in task_lower)
        if category == 'high_ambiguity':
            score += matches * 0.3
        elif category == 'missing_requirements':
            score += matches * 0.4
        elif category == 'multiple_approaches':
            score += matches * 0.2
        elif category == 'undefined_scope':
            score += matches * 0.3
    
    return min(score, 1.0)  # Cap at 1.0


def detect_task_type(task_description):
    """Detect task type from description"""
    task_lower = task_description.lower()
    
    if any(word in task_lower for word in ['implement', 'develop', 'build', 'create', 'code']):
        return 'development'
    elif any(word in task_lower for word in ['analyze', 'research', 'investigate', 'examine']):
        return 'analysis'
    elif any(word in task_lower for word in ['optimize', 'improve', 'enhance', 'speed up']):
        return 'optimization'
    elif any(word in task_lower for word in ['integrate', 'connect', 'combine', 'merge']):
        return 'integration'
    else:
        return 'general'


def generate_general_questions(task_context):
    """Generate general questions for unspecified task types"""
    return [
        "What are the specific requirements for this task?",
        "What is the expected outcome or deliverable?",
        "Are there any constraints or limitations I should be aware of?",
        "What is the timeline or urgency for this task?"
    ]


def process_user_responses(responses, task_context):
    """Process user responses to clarification questions"""
    # TODO: Implement response processing logic
    return task_context


def refine_task_understanding(task_context, user_responses):
    """Refine task understanding based on user feedback"""
    # TODO: Implement task refinement logic
    return task_context