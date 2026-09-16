import os

from grid import Grid
from config import ALGORITHMS, RUNS, POPULATION_SIZE, GENERATIONS
from algorithms.aco import run_aco
from algorithms.cuckoo import run_cuckoo
from algorithms.gwo import run_gwo
from algorithms.ga import run_ga
from algorithms.pso import run_pso
from algorithms.random_search import run_random_search
from experiments.benchmark import run_benchmark
from experiments.statistics import summarize
from visualization.plots import plot_summary, plot_convergence
from visualization.game import run_game

RUNNERS = {
    "ACO": run_aco,
    "Cuckoo": run_cuckoo,
    "GWO": run_gwo,
    "GA": run_ga,
    "PSO": run_pso,
    "Random": run_random_search,
}


def run_single(grid):
    print("\nAlgoritmos:")
    for i, name in enumerate(ALGORITHMS, 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("Escolha: "))
        algorithm = ALGORITHMS[choice - 1]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    result = RUNNERS[algorithm](grid, seed=42)

    print("\n=== RESULTADO ===")
    print(f"Algoritmo: {algorithm}")
    print(f"Fitness: {result['fitness']:.2f}")
    print(f"Sucesso: {result['success']}")
    print(f"Passos: {result['steps']}")
    print(f"Colisões: {result['collisions']}")
    print(f"Avaliações: {result['evaluations']}")

    print("\nMapa com o caminho:")
    grid.show(result["path"])


def run_visual(grid):
    print("\nAlgoritmos:")
    for i, name in enumerate(ALGORITHMS, 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("Escolha: "))
        algorithm = ALGORITHMS[choice - 1]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    run_game(grid, algorithm=algorithm, seed=42)


def main():
    grid = Grid()

    while True:
        print("\n" + "=" * 55)
        print("BIOPATH — PROJETO DE ALGORITMOS BIO-INSPIRADOS")
        print("=" * 55)
        print("1. Mostrar mapa")
        print("2. Executar um algoritmo")
        print("3. Benchmark (30 execuções)")
        print("4. Gerar estatísticas e testes")
        print("5. Gerar gráficos")
        print("6. Abrir jogo Pygame")
        print("0. Sair")

        option = input("\nOpção: ").strip()

        if option == "1":
            grid.show()

        elif option == "2":
            run_single(grid)

        elif option == "3":
            run_benchmark(
                grid,
                runs=RUNS,
                population_size=POPULATION_SIZE,
                generations=GENERATIONS,
            )

        elif option == "4":
            if not os.path.exists("results/results.csv"):
                print("Execute primeiro o benchmark.")
            else:
                summarize()

        elif option == "5":
            if not os.path.exists("results/results.csv"):
                print("Execute primeiro o benchmark.")
            else:
                plot_summary()
                histories = {}
                for algorithm in ALGORITHMS:
                    result = RUNNERS[algorithm](grid, seed=42)
                    histories[algorithm] = result["history"]
                plot_convergence(histories)

        elif option == "6":
            run_visual(grid)

        elif option == "0":
            print("Projeto encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
