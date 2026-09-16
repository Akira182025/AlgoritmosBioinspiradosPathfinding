from config import (
    MAX_STEPS,
    INVALID_MOVE_PENALTY,
    NOT_REACHED_PENALTY,
    COLLISION_PENALTY,
)

MOVES = {
    0: (1, 0),
    1: (-1, 0),
    2: (0, 1),
    3: (0, -1),
}


def decode_vector(vector):
    """Converte uma solução contínua [0,4) em movimentos inteiros."""
    return [int(x) % 4 for x in vector[:MAX_STEPS]]


def simulate(grid, moves):
    """Executa a rota e retorna caminho, colisões e sucesso."""
    x, y = grid.start
    path = [(x, y)]
    collisions = 0
    reached_at = None

    for step, move in enumerate(moves[:MAX_STEPS], start=1):
        dx, dy = MOVES[int(move) % 4]
        nxt = (x + dx, y + dy)

        if not grid.valid(nxt):
            collisions += 1
            nxt = (x, y)

        x, y = nxt
        path.append((x, y))

        if (x, y) == grid.goal:
            reached_at = step
            break

    return path, collisions, reached_at


def evaluate_moves(grid, moves):
    path, collisions, reached_at = simulate(grid, moves)

    if reached_at is not None:
        fitness = float(reached_at) + collisions * COLLISION_PENALTY
        return fitness, path, True, reached_at, collisions

    x, y = path[-1]
    gx, gy = grid.goal
    distance = abs(gx - x) + abs(gy - y)

    fitness = (
        NOT_REACHED_PENALTY
        + distance
        + collisions * COLLISION_PENALTY
        + INVALID_MOVE_PENALTY
    )
    return fitness, path, False, None, collisions


def evaluate_vector(grid, vector):
    return evaluate_moves(grid, decode_vector(vector))
