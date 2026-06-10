def evaluate_relevance(prompt, response):
    if not response:
        return 1

    keywords = prompt.lower().split()
    match_count = sum(1 for k in keywords if k in response.lower())

    score = 1 + min(4, match_count)
    return score