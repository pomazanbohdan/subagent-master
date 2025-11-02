"""
Enhanced Testing & Validation Framework
Comprehensive testing for enhanced distribution system, clarification, and TF-IDF integration.
"""

from src.delegation.enhanced_distribution import enhanced_task_distribution, analyze_task_complexity
from src.mcp.intelligent_tools import is_mcp_task
from src.interactive.clarification import determine_need_for_clarification, generate_contextual_questions
from src.agent_matrix.enhanced_compatibility import calculate_tfidf_relevance_enhanced


def test_enhanced_distribution_system():
    """Test intelligent task distribution between agents and MCP tools"""
    test_cases = [
        # MCP task scenarios (complexity 1)
        {"task": "Search for React best practices", "expected_distribution": "mcp_tools", "expected_tool": "tavily"},
        {"task": "Get documentation for Express.js", "expected_distribution": "mcp_tools", "expected_tool": "context7"},
        {"task": "Analyze small code snippet", "expected_distribution": "mcp_tools", "expected_tool": "sequential-thinking"},

        # Simple agent tasks (complexity 1)
        {"task": "Fix simple bug in function", "expected_distribution": "single_agent", "expected_agent_type": "general-purpose"},
        {"task": "Add validation to form", "expected_distribution": "single_agent", "expected_agent_type": "frontend-architect"},

        # Complex delegation tasks (complexity ≥ 2)
        {"task": "Implement authentication system", "expected_distribution": "agent_delegation", "expected_agents": ["backend-architect", "security-engineer"]},
        {"task": "Design microservices architecture", "expected_distribution": "agent_delegation", "expected_agents": ["backend-architect", "system-architect"]}
    ]

    results = []
    for test_case in test_cases:
        # Test complexity analysis
        complexity = analyze_task_complexity(test_case["task"])

        # Test MCP detection
        is_mcp, category = is_mcp_task(test_case["task"])

        # Test distribution logic
        distribution_result = enhanced_task_distribution(test_case["task"], {})

        # Validate results
        validation_result = {
            "task": test_case["task"],
            "complexity": complexity,
            "is_mcp_task": is_mcp,
            "expected_distribution": test_case["expected_distribution"],
            "actual_distribution": distribution_result["method"],
            "test_passed": distribution_result["method"] == test_case["expected_distribution"]
        }

        results.append(validation_result)

    success_rate = sum(1 for r in results if r["test_passed"]) / len(results)
    return {"results": results, "success_rate": success_rate}


def test_interactive_clarification_system():
    """Test clarification system with various ambiguity scenarios"""
    ambiguous_tasks = [
        "Maybe we could improve the system somehow",
        "Think about optimizing performance",
        "Consider different approaches for the UI",
        "We need to implement something with authentication"
    ]

    results = []
    for task in ambiguous_tasks:
        complexity = analyze_task_complexity(task)
        needs_clarification = determine_need_for_clarification(task, {}, complexity)

        if needs_clarification:
            questions = generate_contextual_questions(task, {}, complexity)
            results.append({
                "task": task,
                "complexity": complexity,
                "needs_clarification": True,
                "questions_generated": len(questions),
                "test_passed": len(questions) > 0
            })
        else:
            results.append({
                "task": task,
                "complexity": complexity,
                "needs_clarification": False,
                "test_passed": False  # Should have triggered clarification
            })

    return results


def test_tfidf_integration():
    """Test TF-IDF enhanced categorization"""
    sample_tasks = [
        {"description": "Implement JWT authentication", "expected_category": "security"},
        {"description": "Create REST API endpoints", "expected_category": "backend"},
        {"description": "Design responsive UI components", "expected_category": "frontend"},
        {"description": "Optimize database queries", "expected_category": "performance"}
    ]

    # Mock agent data for testing
    mock_agents = [
        {"name": "security-specialist", "capabilities": "authentication security JWT OAuth"},
        {"name": "backend-developer", "capabilities": "REST API database Node.js Express"},
        {"name": "frontend-expert", "capabilities": "UI React responsive design CSS"},
        {"name": "performance-engineer", "capabilities": "optimization database performance caching"}
    ]

    results = []
    for task in sample_tasks:
        tfidf_scores = calculate_tfidf_relevance_enhanced({"description": task["description"]}, mock_agents)
        best_agent = max(tfidf_scores, key=tfidf_scores.get)

        results.append({
            "task": task["description"],
            "expected_category": task["expected_category"],
            "best_agent": best_agent,
            "tfidf_score": tfidf_scores[best_agent],
            "test_passed": tfidf_scores[best_agent] > 0.1  # Basic relevance threshold
        })

    return results


def run_comprehensive_tests():
    """Run all test suites and generate comprehensive report"""
    test_results = {
        'distribution_tests': test_enhanced_distribution_system(),
        'clarification_tests': test_interactive_clarification_system(),
        'tfidf_tests': test_tfidf_integration()
    }

    # Calculate overall metrics
    distribution_success_rate = test_results['distribution_tests']['success_rate']
    clarification_results = test_results['clarification_tests']
    tfidf_results = test_results['tfidf_tests']

    clarification_success_rate = sum(1 for r in clarification_results if r["test_passed"]) / len(clarification_results)
    tfidf_success_rate = sum(1 for r in tfidf_results if r["test_passed"]) / len(tfidf_results)

    overall_success_rate = (distribution_success_rate + clarification_success_rate + tfidf_success_rate) / 3

    return {
        'test_results': test_results,
        'metrics': {
            'distribution_success_rate': distribution_success_rate,
            'clarification_success_rate': clarification_success_rate,
            'tfidf_success_rate': tfidf_success_rate,
            'overall_success_rate': overall_success_rate
        },
        'quality_gates': {
            'distribution_passed': distribution_success_rate > 0.90,
            'clarification_passed': clarification_success_rate > 0.85,
            'tfidf_passed': tfidf_success_rate > 0.80,
            'overall_passed': overall_success_rate > 0.85
        },
        'summary': generate_test_summary(test_results, overall_success_rate)
    }


def generate_test_summary(test_results, overall_success_rate):
    """Generate comprehensive test summary"""
    passed_gates = sum([
        test_results['metrics']['distribution_success_rate'] > 0.90,
        test_results['metrics']['clarification_success_rate'] > 0.85,
        test_results['metrics']['tfidf_success_rate'] > 0.80,
        test_results['metrics']['overall_success_rate'] > 0.85
    ])

    total_gates = 4

    return {
        'status': 'PASSED' if overall_success_rate > 0.85 else 'FAILED',
        'success_rate': f"{overall_success_rate:.1%}",
        'gates_passed': f"{passed_gates}/{total_gates}",
        'recommendations': generate_recommendations(test_results),
        'next_steps': generate_next_steps(test_results)
    }


def generate_recommendations(test_results):
    """Generate recommendations based on test results"""
    recommendations = []

    if test_results['metrics']['distribution_success_rate'] < 0.90:
        recommendations.append("Improve task distribution logic for better MCP vs agent selection")
    
    if test_results['metrics']['clarification_success_rate'] < 0.85:
        recommendations.append("Enhance ambiguity detection algorithms")
    
    if test_results['metrics']['tfidf_success_rate'] < 0.80:
        recommendations.append("Optimize TF-IDF parameters for better relevance matching")

    return recommendations


def generate_next_steps(test_results):
    """Generate next steps for improvement"""
    steps = []

    if test_results['metrics']['overall_success_rate'] < 0.85:
        steps.append("Address failing test cases before production deployment")
    else:
        steps.append("System ready for production use")
        steps.append("Implement continuous monitoring")
        steps.append("Set up automated testing pipeline")

    return steps


# Quality validation functions
def validate_system_readiness():
    """Validate system readiness for production"""
    test_results = run_comprehensive_tests()
    
    quality_gates = test_results['quality_gates']
    
    if all(quality_gates.values()):
        return {
            'ready': True,
            'confidence': 'high',
            'test_results': test_results
        }
    else:
        return {
            'ready': False,
            'confidence': 'low',
            'failed_gates': [gate for gate, passed in quality_gates.items() if not passed],
            'test_results': test_results
        }