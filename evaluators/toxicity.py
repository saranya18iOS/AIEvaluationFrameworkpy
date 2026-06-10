def evaluate_toxicity(response):
    bad_words = ["stupid", "idiot", "hate", "dumb"]

    if any(word in response.lower() for word in bad_words):
        return 1  # toxic
    return 5  # safe