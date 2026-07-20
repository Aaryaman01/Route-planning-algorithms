import csv
import os
import random
import time

from task4_np_hard_heuristics.bin_packing import (
    first_fit_decreasing,
    local_search
)


def generate_items(item_count, dimensions=3, seed=42):
    random.seed(seed)

    items = []

    for _ in range(item_count):
        item = [
            random.randint(1, 30)
            for _ in range(dimensions)
        ]

        items.append(item)

    return items


def measure_time(function, *args):
    start_time = time.perf_counter()

    result = function(*args)

    end_time = time.perf_counter()

    return end_time - start_time, result


def benchmark_algorithm(function, *args, repetitions=5):
    times = []
    result = None

    for _ in range(repetitions):
        elapsed_time, result = measure_time(
            function,
            *args
        )

        times.append(elapsed_time)

    average_time = sum(times) / len(times)

    return average_time, result


def save_results(results):
    output_path = (
        "task4_np_hard_heuristics/results/"
        "task4_benchmark_results.csv"
    )

    os.makedirs(
        "task4_np_hard_heuristics/results",
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        newline=""
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "algorithm",
                "item_count",
                "average_time_seconds",
                "number_of_bins"
            ]
        )

        writer.writeheader()
        writer.writerows(results)


def run_benchmark():
    capacity = [100, 100, 100]

    item_sizes = [100, 500, 1_000]

    results = []

    for item_count in item_sizes:
        items = generate_items(item_count)

        ffd_time, ffd_bins = benchmark_algorithm(
            first_fit_decreasing,
            items,
            capacity
        )

        improved_bins = local_search(ffd_bins)

        local_search_time = 0

        for _ in range(5):
            fresh_bins = first_fit_decreasing(
                items,
                capacity
            )

            start_time = time.perf_counter()

            local_search(fresh_bins)

            end_time = time.perf_counter()

            local_search_time += (
                end_time - start_time
            )

        local_search_time /= 5

        print(
            f"{item_count} items:"
        )

        print(
            f"FFD: {ffd_time:.6f} seconds, "
            f"{len(ffd_bins)} bins"
        )

        print(
            f"Local Search: "
            f"{local_search_time:.6f} seconds, "
            f"{len(improved_bins)} bins"
        )

        results.append({
            "algorithm": "First-Fit Decreasing",
            "item_count": item_count,
            "average_time_seconds": ffd_time,
            "number_of_bins": len(ffd_bins)
        })

        results.append({
            "algorithm": "Local Search",
            "item_count": item_count,
            "average_time_seconds": local_search_time,
            "number_of_bins": len(improved_bins)
        })

    save_results(results)


if __name__ == "__main__":
    run_benchmark()