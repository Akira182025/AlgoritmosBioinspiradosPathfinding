GRID_WIDTH = 20
GRID_HEIGHT = 20

START = (0, 0)
GOAL = (19, 19)

MAX_STEPS = 80

POPULATION_SIZE = 30
GENERATIONS = 60
RUNS = 30

INVALID_MOVE_PENALTY = 15.0
NOT_REACHED_PENALTY = 500.0
COLLISION_PENALTY = 8.0

SEED = 42

ALGORITHMS = ["ACO", "Cuckoo", "GWO", "GA", "PSO", "Random"]

OBSTACLES = {
    (3, 0), (3, 1), (3, 2), (3, 3),
    (6, 2), (6, 3), (6, 4), (6, 5),
    (10, 1), (10, 2), (10, 3),
    (13, 4), (14, 4), (15, 4),
    (5, 8), (6, 8), (7, 8), (8, 8),
    (12, 10), (12, 11), (12, 12),
    (3, 13), (4, 13), (5, 13),
    (8, 15), (9, 15), (10, 15), (11, 15),
    (15, 16), (15, 17), (15, 18),
}
