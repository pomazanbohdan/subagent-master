"""
Performance Analysis System

Performance analysis and optimization recommendations.
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import statistics
import logging


class PerformanceAnalyzer:
    """Analyzes performance metrics and provides optimization recommendations."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def analyze_performance(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze performance metrics and return insights.
        
        Args:
            metrics: Performance metrics dictionary
            
        Returns:
            Dictionary containing analysis results and recommendations
        """
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'overall_health': self._assess_overall_health(metrics),
            'bottlenecks': self._identify_bottlenecks(metrics),
            'recommendations': self._generate_recommendations(metrics),
            'trends': self._analyze_trends(metrics),
            'agent_analysis': self._analyze_agent_performance(metrics)
        }
        
        return analysis
    
    def _assess_overall_health(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Assess overall system health."""
        success_rate = metrics.get('success_rate', 0)
        avg_response_time = metrics.get('average_response_time', 0)
        error_count = metrics.get('error_count', 0)
        
        # Health score calculation (0-100)
        health_score = 100
        
        # Deduct points for low success rate
        if success_rate < 0.95:
            health_score -= (0.95 - success_rate) * 200
        
        # Deduct points for slow response times
        if avg_response_time > 5.0:  # 5 seconds threshold
            health_score -= min((avg_response_time - 5.0) * 10, 30)
        
        # Deduct points for high error count
        if error_count > metrics.get('task_count', 1) * 0.1:
            health_score -= 20
        
        health_score = max(0, min(100, health_score))
        
        # Determine health status
        if health_score >= 90:
            status = "excellent"
        elif health_score >= 75:
            status = "good"
        elif health_score >= 60:
            status = "fair"
        else:
            status = "poor"
        
        return {
            'score': round(health_score, 1),
            'status': status,
            'success_rate': success_rate,
            'average_response_time': avg_response_time,
            'error_rate': error_count / max(metrics.get('task_count', 1), 1)
        }
    
    def _identify_bottlenecks(self, metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify performance bottlenecks."""
        bottlenecks = []
        
        # Check response time bottleneck
        avg_response_time = metrics.get('average_response_time', 0)
        max_response_time = metrics.get('max_response_time', 0)
        
        if avg_response_time > 10.0:
            bottlenecks.append({
                'type': 'response_time',
                'severity': 'high',
                'description': f'Average response time is {avg_response_time:.2f}s',
                'impact': 'Poor user experience and system throughput'
            })
        elif max_response_time > 30.0:
            bottlenecks.append({
                'type': 'response_time_spikes',
                'severity': 'medium',
                'description': f'Maximum response time is {max_response_time:.2f}s',
                'impact': 'Intermittent performance issues'
            })
        
        # Check success rate bottleneck
        success_rate = metrics.get('success_rate', 1.0)
        if success_rate < 0.9:
            bottlenecks.append({
                'type': 'success_rate',
                'severity': 'high' if success_rate < 0.8 else 'medium',
                'description': f'Success rate is {success_rate:.1%}',
                'impact': 'High failure rate affecting reliability'
            })
        
        # Check agent-specific bottlenecks
        agent_performance = metrics.get('agent_performance', {})
        for agent, data in agent_performance.items():
            agent_success_rate = data.get('successes', 0) / max(data.get('count', 1), 1)
            if agent_success_rate < 0.8:
                bottlenecks.append({
                    'type': 'agent_performance',
                    'severity': 'medium',
                    'description': f'Agent {agent} has low success rate ({agent_success_rate:.1%})',
                    'impact': 'Specific agent reliability issues'
                })
        
        return bottlenecks
    
    def _generate_recommendations(self, metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate optimization recommendations."""
        recommendations = []
        
        success_rate = metrics.get('success_rate', 1.0)
        avg_response_time = metrics.get('average_response_time', 0)
        
        # Response time recommendations
        if avg_response_time > 5.0:
            recommendations.append({
                'category': 'performance',
                'priority': 'high',
                'action': 'optimize_response_time',
                'description': 'Implement caching and optimize algorithms',
                'expected_impact': '30-50% reduction in response time'
            })
        
        # Success rate recommendations
        if success_rate < 0.95:
            recommendations.append({
                'category': 'reliability',
                'priority': 'high',
                'action': 'improve_error_handling',
                'description': 'Enhance error handling and add retry mechanisms',
                'expected_impact': '5-10% improvement in success rate'
            })
        
        # Agent-specific recommendations
        agent_performance = metrics.get('agent_performance', {})
        for agent, data in agent_performance.items():
            agent_success_rate = data.get('successes', 0) / max(data.get('count', 1), 1)
            if agent_success_rate < 0.85:
                recommendations.append({
                    'category': 'agent_optimization',
                    'priority': 'medium',
                    'action': f'optimize_{agent}_performance',
                    'description': f'Review and optimize {agent} agent configuration',
                    'expected_impact': f'Improved {agent} reliability'
                })
        
        return recommendations
    
    def _analyze_trends(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze performance trends (placeholder for future implementation)."""
        # This would implement trend analysis over time
        return {
            'trend_analysis': 'Not implemented yet',
            'data_points': 1
        }
    
    def _analyze_agent_performance(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze individual agent performance."""
        agent_performance = metrics.get('agent_performance', {})
        analysis = {}
        
        for agent, data in agent_performance.items():
            count = data.get('count', 0)
            successes = data.get('successes', 0)
            errors = data.get('errors', 0)
            total_time = data.get('total_time', 0)
            
            if count > 0:
                analysis[agent] = {
                    'task_count': count,
                    'success_rate': successes / count,
                    'error_rate': errors / count,
                    'average_response_time': total_time / successes if successes > 0 else 0,
                    'reliability_score': (successes / count) * 100,
                    'performance_score': min(100, (successes / count) * 100 * (5.0 / max(total_time / successes, 1))) if successes > 0 else 0
                }
        
        return analysis


def analyze_performance(metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze performance metrics using the global analyzer."""
    analyzer = PerformanceAnalyzer()
    return analyzer.analyze_performance(metrics)


def get_performance_insights(metrics: Dict[str, Any]) -> str:
    """Get human-readable performance insights."""
    analysis = analyze_performance(metrics)
    
    insights = []
    
    # Overall health
    health = analysis['overall_health']
    insights.append(f"System Health: {health['status'].upper()} ({health['score']}/100)")
    
    # Bottlenecks
    bottlenecks = analysis['bottlenecks']
    if bottlenecks:
        insights.append(f"\nIdentified Bottlenecks: {len(bottlenecks)}")
        for bottleneck in bottlenecks[:3]:  # Show top 3
            insights.append(f"- {bottleneck['description']}")
    
    # Recommendations
    recommendations = analysis['recommendations']
    if recommendations:
        insights.append(f"\nTop Recommendations: {len(recommendations)}")
        for rec in recommendations[:2]:  # Show top 2
            insights.append(f"- {rec['description']}")
    
    return '\n'.join(insights)