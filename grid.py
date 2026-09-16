from config import GRID_WIDTH, GRID_HEIGHT, START, GOAL, OBSTACLES


class Grid:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.start = START
        self.goal = GOAL
        self.obstacles = set(OBSTACLES)

    def inside(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def is_obstacle(self, pos):
        return pos in self.obstacles

    def valid(self, pos):
        return self.inside(pos) and not self.is_obstacle(pos)

    def neighbors(self, pos):
        x, y = pos
        candidates = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]
        return [p for p in candidates if self.valid(p)]

    def show(self, path=None):
        path = set(path or [])
        for y in range(self.height):
            row = []
            for x in range(self.width):
                p = (x, y)
                if p == self.start:
                    row.append("S")
                elif p == self.goal:
                    row.append("G")
                elif p in self.obstacles:
                    row.append("#")
                elif p in path:
                    row.append("*")
                else:
                    row.append(".")
            print(" ".join(row))
