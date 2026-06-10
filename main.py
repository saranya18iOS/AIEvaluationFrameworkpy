import pandas as pd

from evaluators.relevance import evaluate_relevance
from evaluators.correctness import evaluate_correctness
from evaluators.completeness import evaluate_completeness
from evaluators.consistency import evaluate_consistency
from evaluators.toxicity import evaluate_toxicity
from evaluators.metrics import compute_total_score


def load_data():
    prompts = pd.read_csv("data/prompts.csv")
    responses = pd.read_csv("data/responses.csv")
    return prompts, responses


def merge_data(prompts, responses):
    prompts["id"] = prompts["id"].astype(str)
    responses["id"] = responses["id"].astype(str)

    return pd.merge(prompts, responses, on="id")


def evaluate(df):
    df["relevance"] = df.apply(lambda x: evaluate_relevance(x["prompt"], x["response"]), axis=1)
    df["correctness"] = df.apply(lambda x: evaluate_correctness(x["prompt"], x["response"]), axis=1)
    df["completeness"] = df.apply(lambda x: evaluate_completeness(x["prompt"], x["response"]), axis=1)
    df["consistency"] = df.apply(lambda x: evaluate_consistency(x["prompt"], x["response"]), axis=1)
    df["toxicity"] = df.apply(lambda x: evaluate_toxicity(x["response"]), axis=1)

    df["total_score"] = df.apply(
        lambda x: compute_total_score(
            x["relevance"],
            x["correctness"],
            x["completeness"],
            x["consistency"],
            x["toxicity"]
        ),
        axis=1
    )

    return df


def main():
    prompts, responses = load_data()

    print("PROMPTS:\n", prompts)
    print("RESPONSES:\n", responses)

    df = merge_data(prompts, responses)

    print("Loaded Data:\n", df)

    results = evaluate(df)

    print("\nEvaluation Results:\n", results)

    results.to_csv("reports/report.csv", index=False)


if __name__ == "__main__":
    main()