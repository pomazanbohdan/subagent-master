"""
Enhanced Agent Compatibility Matrix with TF-IDF Integration
Advanced agent selection with TF-IDF analysis and adaptive learning.
"""

# Try to import sklearn, fallback to basic implementation if not available
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    # Fallback implementations
    def TfidfVectorizer(**kwargs):
        class SimpleVectorizer:
            def __init__(self, max_features=1000, stop_words='english', ngram_range=(1, 2)):
                self.max_features = max_features
                self.stop_words = stop_words
                self.ngram_range = ngram_range

            def fit_transform(self, documents):
                # Simple TF-IDF implementation
                vocabulary = {}
                for doc in documents:
                    words = doc.lower().split()
                    for n in range(self.ngram_range[0], self.ngram_range[1] + 1)):
                        for i in range(len(words) - n + 1):
                            ngram = ' '.join(words[i:i+n])
                            if ngram not in vocabulary:
                                vocabulary[ngram] = len(vocabulary)

                # Create simple TF-IDF matrix
                import math
                tfidf_matrix = []
                for doc in documents:
                    words = doc.lower().split()
                    vector = [0.0] * len(vocabulary)
                    word_count = len(words)
                    vocab_list = sorted(vocabulary.keys())

                    for i, term in enumerate(vocab_list):
                        tf = doc.count(term) / word_count if word_count > 0 else 0
                        # Simple IDF (log(total_docs / doc_freq))
                        df = sum(1 for d in documents if term in d)
                        idf = math.log(len(documents) / df) if df > 0 else 0
                        vector[i] = tf * idf

                    tfidf_matrix.append(vector)

                return tfidf_matrix

        def cosine_similarity(X, Y=None):
            if Y is None:
                Y = X
            import math
            similarity = []
            for i in range(len(X)):
                row = []
                for j in range(len(Y)):
                    dot = sum(a * b for a, b in zip(X[i], Y[j]))
                    norm_a = math.sqrt(sum(a * a for a in X[i]))
                    norm_b = math.sqrt(sum(b * b for b in Y[j]))
                    if norm_a == 0 or norm_b == 0:
                        similarity = 0.0
                    else:
                        similarity = dot / (norm_a * norm_b)
                    row.append(similarity)
                similarity.append(row)
            return similarity

    # Make fallback functions available at module level
    TfidfVectorizer = TfidfVectorizer
    cosine_similarity = cosine_similarity


def calculate_tfidf_relevance_enhanced(task_context, available_agents):
    """Enhanced TF-IDF analysis with task-agent relevance"""
    try:
        # Extract keywords from task description and agent capabilities
        task_keywords = extract_keywords_from_task(task_context['description'])
        agent_descriptions = [agent['capabilities'] + ' ' + agent['expertise'] for agent in available_agents]

        # Create TF-IDF vectors
        vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',
            ngram_range=(1, 2)
        )

        tfidf_matrix = vectorizer.fit_transform([task_keywords] + agent_descriptions])

        # Calculate similarity scores
        task_vector = tfidf_matrix[0]
        agent_vectors = tfidf_matrix[1:]

        similarity_scores = cosine_similarity(task_vector, agent_vectors).flatten()

        return {
            agent['name']: similarity_scores[i]
            for i, agent in enumerate(available_agents)
        }
    except Exception as e:
        # Fallback to simple keyword matching
        print(f"⚠️ TF-IDF fallback activated due to: {e}")
        return simple_keyword_matching(task_context, available_agents)


def simple_keyword_matching(task_context, available_agents):
    """Simple fallback keyword matching when TF-IDF is not available"""
    task_keywords = set(extract_keywords_from_task(task_context['description']))

    results = {}
    for agent in available_agents:
        agent_keywords = set((agent['capabilities'] + ' + agent['expertise']).lower().split())

        # Calculate simple overlap
        common_keywords = task_keywords & agent_keywords
        total_keywords = task_keywords | agent_keywords

        if total_keywords:
            match_score = len(common_keywords) / len(total_keywords)
            results[agent['name']] = match_score
        else:
            results[agent['name']] = 0.0

    return results


def evolve_categories_with_execution_feedback():
    """Improve categories based on task execution results and TF-IDF analysis"""
    execution_history = get_recent_execution_history()

    for task_result in execution_history:
        task_category = task_result['assigned_category']
        success_rate = task_result['success_rate']
        tfidf_relevance = task_result['tfidf_score']
        user_satisfaction = task_result.get('user_feedback', 0.5)

        # Multi-factor category adjustment
        performance_factor = (success_rate + user_satisfaction) / 2
        relevance_factor = tfidf_relevance

        if performance_factor < 0.7 or relevance_factor < 0.5:
            adjust_category_weights(task_category, -0.1)
            log_category_misalignment(task_category, performance_factor, relevance_factor)
        elif performance_factor > 0.9 and relevance_factor > 0.8:
            adjust_category_weights(task_category, +0.05)
            log_category_success(task_category, performance_factor, relevance_factor)


# Helper functions (to be implemented)
def extract_keywords_from_task(description):
    """Extract relevant keywords from task description"""
    # TODO: Implement keyword extraction logic
    return description.lower()


def get_recent_execution_history():
    """Get recent task execution history for learning"""
    # TODO: Implement execution history retrieval
    return []


def adjust_category_weights(category, adjustment):
    """Adjust category weights based on performance feedback"""
    # TODO: Implement category weight adjustment
    pass


def log_category_misalignment(category, performance, relevance):
    """Log category misalignment for analysis"""
    # TODO: Implement misalignment logging
    pass


def log_category_success(category, performance, relevance):
    """Log successful category matches"""
    # TODO: Implement success logging
    pass