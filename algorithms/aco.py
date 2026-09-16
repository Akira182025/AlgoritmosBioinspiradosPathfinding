import numpy as np
from config import POPULATION_SIZE, GENERATIONS, MAX_STEPS
from fitness import evaluate_moves, MOVES


def run_aco(grid, seed=42, population_size=POPULATION_SIZE, generations=GENERATIONS):
    rng = np.random.default_rng(seed)

    # Feromônio associado a cada célula e direção.
    pheromone = np.ones((grid.height, grid.width, 4), dtype=float)

    alpha = 1.0
    beta = 2.5
    evaporation = 0.20
    q = 100.0

    best_score = float("inf")
    best_moves = None
    history = []
    evaluations = 0

    for _ in range(generations):
        ant_solutions = []

        for _ in range(population_size):
            current = grid.start
            moves = []
            visited = {current}

            for _step in range(MAX_STEPS):
                x, y = current
                options = []
                weights = []

                for move, (dx, dy) in MOVES.items():
                    nxt = (x + dx, y + dy)

                    if grid.valid(nxt):
                        gx, gy = grid.goal
                        old_d = abs(gx - x) + abs(gy - y)
                        new_d = abs(gx - nxt[0]) + abs(gy - nxt[1])

                        # Heurística favorece movimentos que aproximam do objetivo.
                        heuristic = 1.0 + max(0, old_d - new_d)
                        weight = (pheromone[y, x, move] ** alpha) * (heuristic ** beta)

                        if nxt in visited:
                            weight *= 0.35

                        options.append(move)
                        weights.append(weight)

                if not options:
                    break

                weights = np.asarray(weights, dtype=float)
                weights /= weights.sum()

                move = int(rng.choice(options, p=weights))
                moves.append(move)

                dx, dy = MOVES[move]
                current = (current[0] + dx, current[1] + dy)
                visited.add(current)

                if current == grid.goal:
                    break

            result = evaluate_moves(grid, moves)
            evaluations += 1
            ant_solutions.append((result[0], moves, result))

            if result[0] < best_score:
                best_score = result[0]
                best_moves = moves.copy()

        pheromone *= (1.0 - evaporation)

        ant_solutions.sort(key=lambda item: item[0])
        for score, moves, _ in ant_solutions[:max(1, population_size // 5)]:
            amount = q / max(score, 1e-9)
            current = grid.start

            for move in moves:
                x, y = current
                pheromone[y, x, move] += amount

                dx, dy = MOVES[move]
                nxt = (current[0] + dx, current[1] + dy)

                if grid.valid(nxt):
                    current = nxt

                if current == grid.goal:
                    break

        history.append(best_score)

    result = evaluate_moves(grid, best_moves)

    return {
        "algorithm": "ACO",
        "fitness": result[0],
        "path": result[1],
        "success": result[2],
        "steps": result[3],
        "collisions": result[4],
        "history": history,
        "evaluations": evaluations,
    }
