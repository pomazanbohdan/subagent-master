"""
Enhanced Agent Selection with TF-IDF Integration
Hybrid scoring system combining ML, TF-IDF, and performance metrics.
"""


def hybrid_scoring_system(ml_score, tfidf_score, performance_score):
    """Combine multiple scoring methods"""
    return {
        'final_score': (ml_score * 0.5) + (tfidf_score * 0.3) + (performance_score * 0.2),
        'ml_confidence': ml_score,
        'tfidf_relevance': tfidf_score,
        'performance_confidence': performance_score,
        'selection_rationale': generate_selection_rationale(ml_score, tfidf_score, performance_score)
    }


def enhanced_agent_selection(task_context, available_agents):
    """Enhanced agent selection with TF-IDF integration"""
    # Calculate ML scores
    ml_scores = calculate_ml_scores(task_context, available_agents)
    
    # Calculate TF-IDF scores
    tfidf_scores = calculate_tfidf_relevance_enhanced(task_context, available_agents)
    
    # Get performance scores
    performance_scores = get_performance_metrics(available_agents)
    
    # Combine scores using hybrid system
    final_scores = {}
    for agent in available_agents:
        agent_name = agent['name']
        hybrid_result = hybrid_scoring_system(
            ml_scores.get(agent_name, 0),
            tfidf_scores.get(agent_name, 0),
            performance_scores.get(agent_name, 0)
        )
        final_scores[agent_name] = hybrid_result
    
    # Sort by final score
    sorted_agents = sorted(final_scores.items(), key=lambda x: x[1]['final_score'], reverse=True)
    
    return {
        'ranked_agents': sorted_agents,
        'selection_confidence': max(score['final_score'] for score in final_scores.values()),
        'recommendation': sorted_agents[0] if sorted_agents else None
    }


def calculate_capability_matches_enhanced(task_context, available_agents):
    """Enhanced capability matching with detailed analysis"""
    matches = {}
    
    for agent in available_agents:
        agent_capabilities = set(agent['capabilities'].lower().split())
        task_requirements = extract_task_requirements(task_context)
        
        # Calculate match percentage
        matches_count = len(agent_capabilities & set(task_requirements))
        total_requirements = len(task_requirements)
        
        match_score = matches_count / total_requirements if total_requirements > 0 else 0
        
        matches[agent['name']] = {
            'match_score': match_score,
            'matched_capabilities': list(agent_capabilities & set(task_requirements)),
            'missing_capabilities': list(set(task_requirements) - agent_capabilities),
            'additional_capabilities': list(agent_capabilities - set(task_requirements))
        }
    
    return matches


# Helper functions (to be implemented)
def generate_selection_rationale(ml_score, tfidf_score, performance_score):
    """Generate rationale for agent selection"""
    # TODO: Implement rationale generation
    rationale = []
    
    if ml_score > 0.8:
        rationale.append(f"High ML confidence ({ml_score:.2f})")
    elif ml_score > 0.6:
        rationale.append(f"Moderate ML confidence ({ml_score:.2f})")
    
    if tfidf_score > 0.7:
        rationale.append(f"Strong TF-IDF relevance ({tfidf_score:.2f})")
    elif tfidf_score > 0.5:
        rationale.append(f"Good TF-IDF relevance ({tfidf_score:.2f})")
    
    if performance_score > 0.8:
        rationale.append(f"Excellent performance record ({performance_score:.2f})")
    elif performance_score > 0.6:
        rationale.append(f"Good performance record ({performance_score:.2f})")
    
    return "; ".join(rationale) if rationale else "Selected based on available criteria"


def calculate_ml_scores(task_context, available_agents):
    """Calculate ML-based scores for agent selection"""
    # TODO: Implement ML scoring logic
    scores = {}
    for agent in available_agents:
        # Placeholder ML scoring logic
        scores[agent['name']] = 0.7  # Default score
    
    return scores


def get_performance_metrics(available_agents):
    """Get performance metrics for agents"""
    # TODO: Implement performance metrics retrieval
    scores = {}
    for agent in available_agents:
        # Placeholder performance scoring
        scores[agent['name']] = 0.8  # Default score
    
    return scores


def extract_task_requirements(task_context):
    """Extract requirements from task context"""
    # TODO: Implement requirement extraction
    description = task_context.get('description', '').lower()
    
    # Simple keyword extraction (to be enhanced)
    common_keywords = [
        'api', 'database', 'ui', 'frontend', 'backend', 'security',
        'performance', 'testing', 'documentation', 'deployment'
    ]
    
    requirements = [word for word in common_keywords if word in description]
    
    # Extract technical terms
    import re
    technical_terms = re.findall(r'\b\w+(?:\.js|\.py|\.java|\.sql|\.html|\.css)\b', description)
    requirements.extend(technical_terms)
    
    return list(set(requirements))


def select_top_candidates_enhanced(matrix, filters):
    """Select top candidates with enhanced filtering"""
    # TODO: Implement enhanced candidate selection
    candidates = sorted(matrix.items(), key=lambda x: x[1]['final_score'], reverse=True)
    return candidates[:3]  # Return top 3


def validate_agent_selection_enhanced(agents, task):
    """Enhanced validation of agent selection"""
    # TODO: Implement enhanced validation
    return {
        'valid': True,
        'confidence': 0.8,
        'validation_notes': []
    }