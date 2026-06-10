def evaluate_completeness(prompt, response):
    required_words = ["how", "what", "why", "cancel", "update", "reset"]

    coverage = sum(1 for w in required_words if w in response.lower())
    return min(5, 1 + coverage)