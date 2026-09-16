import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_summary(csv_path="results/results.csv"):
    os.makedirs("results/graphs", exist_ok=True)
    df = pd.read_csv(csv_path)

    summary = df.groupby("algorithm")["fitness"].mean().sort_values()
    plt.figure(figsize=(9, 5))
    plt.bar(summary.index, summary.values)
    plt.ylabel("Fitness médio")
    plt.xlabel("Algoritmo")
    plt.title("Fitness médio por algoritmo")
    plt.tight_layout()
    plt.savefig("results/graphs/fitness_medio.png", dpi=160)
    plt.close()

    success = df.groupby("algorithm")["success"].mean() * 100
    plt.figure(figsize=(9, 5))
    plt.bar(success.index, success.values)
    plt.ylabel("Taxa de sucesso (%)")
    plt.xlabel("Algoritmo")
    plt.title("Taxa de sucesso")
    plt.ylim(0, 105)
    plt.tight_layout()
    plt.savefig("results/graphs/taxa_sucesso.png", dpi=160)
    plt.close()

    time_mean = df.groupby("algorithm")["time_seconds"].mean().sort_values()
    plt.figure(figsize=(9, 5))
    plt.bar(time_mean.index, time_mean.values)
    plt.ylabel("Tempo médio (s)")
    plt.xlabel("Algoritmo")
    plt.title("Tempo médio de execução")
    plt.tight_layout()
    plt.savefig("results/graphs/tempo_medio.png", dpi=160)
    plt.close()

    print("Gráficos salvos em results/graphs/")


def plot_convergence(histories):
    os.makedirs("results/graphs", exist_ok=True)

    plt.figure(figsize=(10, 6))
    for name, history in histories.items():
        arr = np.asarray(history, dtype=float)
        plt.plot(arr, label=name)

    plt.xlabel("Geração")
    plt.ylabel("Melhor fitness acumulado")
    plt.title("Curvas de convergência")
    plt.legend()
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig("results/graphs/convergencia.png", dpi=160)
    plt.close()

    print("Curva de convergência salva em results/graphs/convergencia.png")
