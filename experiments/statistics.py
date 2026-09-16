import pandas as pd
from scipy.stats import mannwhitneyu


def summarize(csv_path="results/results.csv"):
    df = pd.read_csv(csv_path)

    summary = (
        df.groupby("algorithm")
        .agg(
            fitness_mean=("fitness", "mean"),
            fitness_std=("fitness", "std"),
            time_mean=("time_seconds", "mean"),
            time_std=("time_seconds", "std"),
            success_rate=("success", "mean"),
            path_mean=("path_length", "mean"),
            path_std=("path_length", "std"),
        )
        .reset_index()
    )

    summary["success_rate"] *= 100
    summary.to_csv("results/summary.csv", index=False)

    print("\n=== RESUMO ===")
    print(summary.to_string(index=False, float_format=lambda x: f"{x:.3f}"))

    algorithms = list(df["algorithm"].unique())
    rows = []

    for i in range(len(algorithms)):
        for j in range(i + 1, len(algorithms)):
            a = algorithms[i]
            b = algorithms[j]
            x = df[df.algorithm == a]["fitness"].dropna()
            y = df[df.algorithm == b]["fitness"].dropna()

            stat, p = mannwhitneyu(x, y, alternative="two-sided")
            rows.append({
                "algorithm_a": a,
                "algorithm_b": b,
                "u_statistic": stat,
                "p_value": p,
                "significant_05": p < 0.05,
            })

    tests = pd.DataFrame(rows)
    tests.to_csv("results/statistical_tests.csv", index=False)

    print("\n=== TESTES DE MANN-WHITNEY ===")
    print(tests.to_string(index=False))

    return summary, tests
