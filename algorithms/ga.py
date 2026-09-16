import numpy as np
from config import MAX_STEPS, POPULATION_SIZE, GENERATIONS
from fitness import evaluate_moves
from utils import random_moves


def run_ga(grid, seed=42, population_size=POPULATION_SIZE, generations=GENERATIONS):
    rng = np.random.default_rng(seed)
    population = [random_moves(rng) for _ in range(population_size)]
    history = []
    evaluations = 0
    best = None

    for _ in range(generations):
        scored = []
        for individual in population:
            result = evaluate_moves(grid, individual)
            evaluations += 1
            scored.append((result[0], individual.copy(), result))

        scored.sort(key=lambda z: z[0])
        if best is None or scored[0][0] < best[0]:
            best = scored[0]
        history.append(best[0])

        elite_count = max(2, population_size // 5)
        elites = [x[1].copy() for x in scored[:elite_count]]
        new_population = elites.copy()

        while len(new_population) < population_size:
            limit = max(5, population_size // 2)
            p1 = scored[rng.integers(0, limit)][1]
            p2 = scored[rng.integers(0, limit)][1]

            cut = int(rng.integers(1, MAX_STEPS - 1))
            child = np.concatenate([p1[:cut], p2[cut:]]).copy()

            mask = rng.random(MAX_STEPS) < 0.04
            child[mask] = rng.integers(0, 4, size=mask.sum())
            new_population.append(child)

        population = new_population

    result = evaluate_moves(grid, best[1])
    return {
        "algorithm": "GA", "fitness": result[0], "path": result[1],
        "success": result[2], "steps": result[3], "collisions": result[4],
        "history": history, "evaluations": evaluations,
    }
