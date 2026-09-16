import pygame

from config import GRID_WIDTH, GRID_HEIGHT
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


def run_game(grid, algorithm="ACO", seed=42):
    pygame.init()

    cell = 30
    panel = 280
    width = GRID_WIDTH * cell + panel
    height = GRID_HEIGHT * cell

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("BioPath — NPC Pathfinding")

    font = pygame.font.SysFont("Arial", 20)
    small = pygame.font.SysFont("Arial", 16)
    clock = pygame.time.Clock()

    result = RUNNERS[algorithm](grid, seed=seed)
    path = result["path"]
    path_index = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((245, 245, 245))

        for y in range(grid.height):
            for x in range(grid.width):
                rect = pygame.Rect(x * cell, y * cell, cell, cell)
                p = (x, y)

                if p in grid.obstacles:
                    pygame.draw.rect(screen, (55, 55, 55), rect)
                else:
                    pygame.draw.rect(screen, (235, 235, 235), rect)

                pygame.draw.rect(screen, (190, 190, 190), rect, 1)

        visible = path[:path_index + 1]
        for x, y in visible:
            rect = pygame.Rect(x * cell + 7, y * cell + 7, cell - 14, cell - 14)
            pygame.draw.rect(screen, (80, 150, 220), rect)

        sx, sy = grid.start
        gx, gy = grid.goal

        pygame.draw.rect(
            screen, (80, 180, 100),
            pygame.Rect(sx * cell + 5, sy * cell + 5, cell - 10, cell - 10)
        )
        pygame.draw.rect(
            screen, (220, 90, 90),
            pygame.Rect(gx * cell + 5, gy * cell + 5, cell - 10, cell - 10)
        )

        if visible:
            nx, ny = visible[-1]
            pygame.draw.circle(
                screen, (30, 80, 180),
                (nx * cell + cell // 2, ny * cell + cell // 2), 9
            )

        px = GRID_WIDTH * cell + 18
        texts = [
            ("BioPath", font),
            (f"Algoritmo: {algorithm}", small),
            (f"Fitness: {result['fitness']:.2f}", small),
            (f"Sucesso: {'SIM' if result['success'] else 'NÃO'}", small),
            (f"Passos: {result['steps']}", small),
            ("", small),
            ("ESC = sair", small),
        ]

        yy = 20
        for text, used_font in texts:
            surface = used_font.render(text, True, (30, 30, 30))
            screen.blit(surface, (px, yy))
            yy += 35 if used_font == font else 27

        pygame.display.flip()

        if path_index < len(path) - 1:
            path_index += 1

        clock.tick(8)

    pygame.quit()
