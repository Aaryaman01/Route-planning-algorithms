import csv
import os

import matplotlib.pyplot as plt


def load_results():
    input_path = (
        "task5_concurrency/results/"
        "task5_benchmark_results.csv"
    )

    results = []

    with open(input_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            results.append({
                "algorithm": row["algorithm"],
                "data_size": int(row["data_size"]),
                "thread_count": row["thread_count"],
                "time": float(
                    row["average_time_seconds"]
                ),
                "speedup": float(row["speedup"])
            })

    return results


def create_visualizations():
    results = load_results()

    output_directory = (
        "task5_concurrency/results/figures"
    )

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    algorithms = [
        "Sequential",
        "ThreadPoolExecutor",
        "threading.Thread"
    ]

    data_sizes = [
        1_000,
        5_000,
        10_000
    ]

    # Runtime comparison for each data size
    for data_size in data_sizes:
        data_results = [
            row
            for row in results
            if row["data_size"] == data_size
        ]

        labels = []
        times = []

        for row in data_results:
            if row["algorithm"] == "Sequential":
                label = "Sequential"
            else:
                label = (
                    f"{row['algorithm']} - "
                    f"{row['thread_count']} threads"
                )

            labels.append(label)
            times.append(row["time"])

        plt.figure()

        plt.bar(
            labels,
            times
        )

        plt.xlabel("Approach")
        plt.ylabel("Average time (seconds)")
        plt.title(
            f"Sorting Runtime Comparison "
            f"({data_size} items)"
        )

        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.tight_layout()

        output_path = os.path.join(
            output_directory,
            f"runtime_comparison_{data_size}.png"
        )

        plt.savefig(output_path)
        plt.close()

        print(
            f"Saved graph to {output_path}"
        )

    # Speedup against sequential sorting
    for algorithm in algorithms[1:]:
        algorithm_results = [
            row
            for row in results
            if row["algorithm"] == algorithm
        ]

        thread_counts = [
            row["thread_count"]
            for row in algorithm_results
            if row["data_size"] == 10_000
        ]

        speedups = [
            row["speedup"]
            for row in algorithm_results
            if row["data_size"] == 10_000
        ]

        plt.figure()

        plt.plot(
            thread_counts,
            speedups,
            marker="o"
        )

        plt.axhline(
            y=1.0,
            linestyle="--"
        )

        plt.xlabel("Number of threads")
        plt.ylabel("Speedup")
        plt.title(
            f"{algorithm} Speedup "
            "(10,000 items)"
        )

        plt.grid(True)

        output_path = os.path.join(
            output_directory,
            f"{algorithm.lower().replace('.', '').replace(' ', '_')}"
            "_speedup.png"
        )

        plt.savefig(output_path)
        plt.close()

        print(
            f"Saved graph to {output_path}"
        )

    # Runtime against input size
    for algorithm in algorithms:
        algorithm_results = [
            row
            for row in results
            if row["algorithm"] == algorithm
        ]

        if algorithm == "Sequential":
            data_sizes_for_plot = [
                row["data_size"]
                for row in algorithm_results
            ]

            times = [
                row["time"]
                for row in algorithm_results
            ]

            label = algorithm

            plt.figure()

            plt.plot(
                data_sizes_for_plot,
                times,
                marker="o",
                label=label
            )

            plt.xlabel("Input size")
            plt.ylabel("Average time (seconds)")
            plt.title(
                "Sorting Runtime Against Input Size"
            )

            plt.grid(True)

            output_path = os.path.join(
                output_directory,
                "runtime_against_input_size.png"
            )

            plt.savefig(output_path)
            plt.close()

            break


if __name__ == "__main__":
    create_visualizations()