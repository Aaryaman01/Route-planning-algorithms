import csv
import os

import matplotlib.pyplot as plt


def load_results():
    input_path = (
        "task3_algorithmic_strategies/results/"
        "task3_benchmark_results.csv"
    )

    results = []

    with open(input_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            results.append({
                "algorithm": row["algorithm"],
                "input_size": int(row["input_size"]),
                "time": float(row["average_time_seconds"])
            })

    return results


def create_visualizations():
    results = load_results()

    output_directory = (
        "task3_algorithmic_strategies/results/figures"
    )

    os.makedirs(output_directory, exist_ok=True)

    algorithms = [
        "Weighted Job Scheduling",
        "Minimum Platforms",
        "Hamiltonian Cycle"
    ]

    file_names = {
        "Weighted Job Scheduling":
            "weighted_job_scheduling.png",
        "Minimum Platforms":
            "minimum_platforms.png",
        "Hamiltonian Cycle":
            "hamiltonian_cycle.png"
    }

    for algorithm in algorithms:
        algorithm_results = [
            row
            for row in results
            if row["algorithm"] == algorithm
        ]

        input_sizes = [
            row["input_size"]
            for row in algorithm_results
        ]

        times = [
            row["time"]
            for row in algorithm_results
        ]

        plt.figure()

        plt.plot(
            input_sizes,
            times,
            marker="o"
        )

        plt.xlabel("Input size")
        plt.ylabel("Average time (seconds)")
        plt.title(
            f"{algorithm} Performance"
        )
        plt.grid(True)

        output_path = os.path.join(
            output_directory,
            file_names[algorithm]
        )

        plt.savefig(output_path)
        plt.close()

        print(f"Saved graph to {output_path}")


if __name__ == "__main__":
    create_visualizations()