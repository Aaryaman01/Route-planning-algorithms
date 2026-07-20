import csv
import os

import matplotlib.pyplot as plt


def load_results():
    input_path = (
        "task4_np_hard_heuristics/results/"
        "task4_benchmark_results.csv"
    )

    results = []

    with open(input_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            results.append({
                "algorithm": row["algorithm"],
                "item_count": int(row["item_count"]),
                "time": float(row["average_time_seconds"]),
                "bins": int(row["number_of_bins"])
            })

    return results


def create_visualizations():
    results = load_results()

    output_directory = (
        "task4_np_hard_heuristics/results/figures"
    )

    os.makedirs(output_directory, exist_ok=True)

    algorithms = [
        "First-Fit Decreasing",
        "Local Search"
    ]

    for algorithm in algorithms:
        algorithm_results = [
            row
            for row in results
            if row["algorithm"] == algorithm
        ]

        item_counts = [
            row["item_count"]
            for row in algorithm_results
        ]

        times = [
            row["time"]
            for row in algorithm_results
        ]

        bins = [
            row["bins"]
            for row in algorithm_results
        ]

        plt.figure()

        plt.plot(
            item_counts,
            times,
            marker="o"
        )

        plt.xlabel("Number of items")
        plt.ylabel("Average time (seconds)")
        plt.title(
            f"{algorithm} Runtime"
        )
        plt.grid(True)

        output_path = os.path.join(
            output_directory,
            f"{algorithm.lower().replace(' ', '_').replace('-', '')}"
            "_runtime.png"
        )

        plt.savefig(output_path)
        plt.close()

        print(f"Saved graph to {output_path}")

    plt.figure()

    for algorithm in algorithms:
        algorithm_results = [
            row
            for row in results
            if row["algorithm"] == algorithm
        ]

        item_counts = [
            row["item_count"]
            for row in algorithm_results
        ]

        bins = [
            row["bins"]
            for row in algorithm_results
        ]

        plt.plot(
            item_counts,
            bins,
            marker="o",
            label=algorithm
        )

    plt.xlabel("Number of items")
    plt.ylabel("Number of bins")
    plt.title("Bin Packing Solution Quality")
    plt.legend()
    plt.grid(True)

    output_path = os.path.join(
        output_directory,
        "bin_count_comparison.png"
    )

    plt.savefig(output_path)
    plt.close()

    print(f"Saved graph to {output_path}")


if __name__ == "__main__":
    create_visualizations()