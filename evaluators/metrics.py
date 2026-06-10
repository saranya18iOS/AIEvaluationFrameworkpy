def clamp(score, min_val=1, max_val=5):
    return max(min_val, min(max_val, score))


def normalize_score(scores):
    return sum(scores) / len(scores) if scores else 0


def compute_total_score(relevance, correctness, completeness, consistency, toxicity):
    scores = [
        relevance,
        correctness,
        completeness,
        consistency,
        toxicity
    ]

    return normalize_score(scores)