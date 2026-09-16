import math
import numpy as np
from config import MAX_STEPS, POPULATION_SIZE, GENERATIONS
from fitness import evaluate_vector
from utils import random_vector, clip_vector


def levy_flight(rng, shape, beta=1.5):
    sigma_u = (
        math.gamma(1 + beta) * math.sin(math.pi * beta / 2)
        / (math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))
    ) ** (1 / beta)

    u = rng.normal(0, sigma_u, size=shape)
    v = rng.normal(0, 1, size=shape)
    return u / (np.abs(v) ** (1 / beta))


def run_cuckoo(grid, seed=42, population_size=POPULATION_SIZE, generations=GENERATIONS):
    rng = np.random.default_rng(seed)
    nests = np.array([random_vector(rng) for _ in range(population_size)])
    scores = np.array([evaluate_vector(grid, n)[0] for n in nests])
    evaluations = population_size

    idx = int(np.argmin(scores))
    best = nests[idx].copy()
    best_score = float(scores[idx])
    history = []
    pa = 0.25

    for _ in range(generations):
        for _ in range(population_size):
            i = int(rng.integers(population_size))
            step = 0.08 * levy_flight(rng, MAX_STEPS)
            candidate = clip_vector(nests[i] + step)
            result = evaluate_vector(grid, candidate)
            evaluations += 1

            j = int(rng.integers(population_size))
            if result[0] < scores[j]:
                nests[j] = candidate
                scores[j] = result[0]

        abandon = rng.random(population_size) < pa
        for i in np.where(abandon)[0]:
            nests[i] = random_vector(rng)
            scores[i] = evaluate_vector(grid, nests[i])[0]
            evaluations += 1

        idx = int(np.argmin(scores))
        if scores[idx] < best_score:
            best_score = float(scores[idx])
            best = nests[idx].copy()

        history.append(best_score)

    result = evaluate_vector(grid, best)
    return {
        "algorithm": "Cuckoo", "fitness": result[0], "path": result[1],
        "success": result[2], "steps": result[3], "collisions": result[4],
        "history": history, "evaluations": evaluations,
    }
