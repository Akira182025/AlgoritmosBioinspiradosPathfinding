import numpy as np
from config import MAX_STEPS, POPULATION_SIZE, GENERATIONS
from fitness import evaluate_vector
from utils import random_vector, clip_vector


def run_pso(grid, seed=42, population_size=POPULATION_SIZE, generations=GENERATIONS):
    rng = np.random.default_rng(seed)
    positions = np.array([random_vector(rng) for _ in range(population_size)])
    velocities = np.zeros_like(positions)

    personal_best = positions.copy()
    personal_scores = np.full(population_size, np.inf)
    global_best = None
    global_score = np.inf
    history = []
    evaluations = 0

    for generation in range(generations):
        for i in range(population_size):
            result = evaluate_vector(grid, positions[i])
            evaluations += 1
            score = result[0]

            if score < personal_scores[i]:
                personal_scores[i] = score
                personal_best[i] = positions[i].copy()

            if score < global_score:
                global_score = score
                global_best = positions[i].copy()

        history.append(global_score)

        w = 0.85 - 0.55 * generation / max(1, generations - 1)
        c1, c2 = 1.6, 1.8
        r1 = rng.random(positions.shape)
        r2 = rng.random(positions.shape)

        velocities = (
            w * velocities
            + c1 * r1 * (personal_best - positions)
            + c2 * r2 * (global_best - positions)
        )
        positions = clip_vector(positions + velocities)

    result = evaluate_vector(grid, global_best)
    return {
        "algorithm": "PSO", "fitness": result[0], "path": result[1],
        "success": result[2], "steps": result[3], "collisions": result[4],
        "history": history, "evaluations": evaluations,
    }
