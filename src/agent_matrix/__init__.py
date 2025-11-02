"""
Agent Matrix Module
Enhanced agent compatibility matrix with TF-IDF integration and adaptive scoring.
"""

from .enhanced_compatibility import (
    calculate_tfidf_relevance_enhanced,
    evolve_categories_with_execution_feedback
)

from .enhanced_scoring import (
    hybrid_scoring_system,
    enhanced_agent_selection,
    calculate_capability_matches_enhanced
)

__all__ = [
    'calculate_tfidf_relevance_enhanced',
    'evolve_categories_with_execution_feedback',
    'hybrid_scoring_system',
    'enhanced_agent_selection',
    'calculate_capability_matches_enhanced'
]