def evaluate_correctness(prompt, response):
    # placeholder heuristic (replace later with LLM judge)
    if len(response) < 20:
        return 2
    if "how" in prompt.lower() and "you" in response.lower():
        return 4
    return 3