import numpy as np
from config import MAX_STEPS, POPULATION_SIZE, GENERATIONS
from fitness import evaluate_vector
from utils import random_vector, clip_vector


def run_gwo(grid, seed=42, population_size=POPULATION_SIZE, generations=GENERATIONS):
    rng = np.random.default_rng(seed)
    wolves = np.array([random_vector(rng) for _ in range(population_size)])
    history = []
    evaluations = 0
    best_vector = None
    best_score = np.inf

    for generation in range(generations):
        scores = []

        for wolf in wolves:
            result = evaluate_vector(grid, wolf)
            evaluations += 1
            scores.append(result[0])
            if result[0] < best_score:
                best_score = result[0]
                best_vector = wolf.copy()

        order = np.argsort(scores)
        alpha = wolves[order[0]].copy()
        beta = wolves[order[1]].copy()
        delta = wolves[order[2]].copy()
        history.append(best_score)

        a = 2.0 - 2.0 * generation / max(1, generations - 1)
        new_wolves = []

        for wolf in wolves:
            candidates = []
            for leader in (alpha, beta, delta):
                r1 = rng.random(MAX_STEPS)
                r2 = rng.random(MAX_STEPS)
                A = 2 * a * r1 - a
                C = 2 * r2
                D = np.abs(C * leader - wolf)
                candidates.append(leader - A * D)
            new_wolves.append(np.mean(candidates, axis=0))

        wolves = clip_vector(np.array(new_wolves))

    result = evaluate_vector(grid, best_vector)
    return {
        "algorithm": "GWO", "fitness": result[0], "path": result[1],
        "success": result[2], "steps": result[3], "collisions": result[4],
        "history": history, "evaluations": evaluations,
    }
