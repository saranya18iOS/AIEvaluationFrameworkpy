def evaluate_consistency(prompt, response):
    # simple heuristic: repetition penalty
    words = response.lower().split()
    unique_ratio = len(set(words)) / len(words)

    if unique_ratio > 0.9:
        return 5
    elif unique_ratio > 0.7:
        return 4
    elif unique_ratio > 0.5:
        return 3
    return 2