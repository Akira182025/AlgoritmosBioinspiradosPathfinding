import csv
import os
import time

from config import ALGORITHMS, POPULATION_SIZE, GENERATIONS, RUNS, SEED
from algorithms.aco import run_aco
from algorithms.cuckoo import run_cuckoo
from algorithms.gwo import run_gwo
from algorithms.ga import run_ga
from algorithms.pso import run_pso
from algorithms.random_search import run_random_search

RUNNERS = {
    "ACO": run_aco,
    "Cuckoo": run_cuckoo,
    "GWO": run_gwo,
    "GA": run_ga,
    "PSO": run_pso,
    "Random": run_random_search,
}


def run_benchmark(grid, runs=RUNS, population_size=POPULATION_SIZE, generations=GENERATIONS):
    os.makedirs("results", exist_ok=True)
    rows = []

    for algorithm in ALGORITHMS:
        print(f"\n>>> {algorithm}")
        runner = RUNNERS[algorithm]

        for run in range(1, runs + 1):
            seed = SEED + run * 100 + ALGORITHMS.index(algorithm)

            start = time.perf_counter()
            result = runner(
                grid,
                seed=seed,
                population_size=population_size,
                generations=generations,
            )
            elapsed = time.perf_counter() - start

            rows.append({
                "algorithm": algorithm,
                "run": run,
                "fitness": result["fitness"],
                "path_length": result["steps"] if result["steps"] is not None else "",
                "success": int(result["success"]),
                "collisions": result["collisions"],
                "time_seconds": elapsed,
                "evaluations": result["evaluations"],
            })

            print(
                f"run {run:02d}/{runs} | fitness={result['fitness']:.2f} | "
                f"success={result['success']} | time={elapsed:.3f}s"
            )

    path = "results/results.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nResultados salvos em: {path}")
    return rows
