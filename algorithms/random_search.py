from config import MAX_STEPS, POPULATION_SIZE, GENERATIONS
from fitness import evaluate_moves
from utils import random_moves


def run_random_search(grid, seed=42, population_size=POPULATION_SIZE, generations=GENERATIONS):
    import numpy as np
    rng = np.random.default_rng(seed)

    total_candidates = population_size * generations
    history = []
    best_score = float("inf")
    best_moves = None
    evaluations = 0

    for _ in range(total_candidates):
        moves = random_moves(rng, MAX_STEPS)
        result = evaluate_moves(grid, moves)
        evaluations += 1

        if result[0] < best_score:
            best_score = result[0]
            best_moves = moves.copy()

        if evaluations % population_size == 0:
            history.append(best_score)

    result = evaluate_moves(grid, best_moves)
    return {
        "algorithm": "Random", "fitness": result[0], "path": result[1],
        "success": result[2], "steps": result[3], "collisions": result[4],
        "history": history, "evaluations": evaluations,
    }
