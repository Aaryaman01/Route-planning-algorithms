import csv
import os

import matplotlib.pyplot as plt


def load_results():
    input_path = (
        "task2_graph_algorithms/results/"
        "task2_benchmark_results.csv"
    )

    results = []

    with open(input_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            results.append({
                "algorithm": row["algorithm"],
                "vertices": int(row["vertices"]),
                "time": float(row["average_time_seconds"])
            })

    return results


def create_visualization():
    results = load_results()

    output_directory = (
        "task2_graph_algorithms/results/figures"
    )

    os.makedirs(output_directory, exist_ok=True)

    algorithms = [
        "Dijkstra",
        "Bellman-Ford",
        "Prim"
    ]

    vertex_sizes = sorted(
        set(row["vertices"] for row in results)
    )

    for algorithm in algorithms:
        times = [
            row["time"]
            for row in results
            if row["algorithm"] == algorithm
        ]

        plt.plot(
            vertex_sizes,
            times,
            marker="o",
            label=algorithm
        )

    plt.xlabel("Number of vertices")
    plt.ylabel("Average time (seconds)")
    plt.title("Graph Algorithm Performance Comparison")
    plt.legend()
    plt.grid(True)

    output_path = (
        f"{output_directory}/"
        "algorithm_performance_comparison.png"
    )

    plt.savefig(output_path)
    plt.close()

    print(f"Saved graph to {output_path}")


if __name__ == "__main__":
    create_visualization()