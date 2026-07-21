import csv
import os
import random
import time

from task5_concurrency.sorting import (
    merge_sort,
    parallel_merge_sort,
    threaded_merge_sort
)


def generate_data(size, seed=42):
    random.seed(seed)

    return [
        random.randint(1, 1_000_000)
        for _ in range(size)
    ]


def measure_time(function, *args):
    start_time = time.perf_counter()

    function(*args)

    end_time = time.perf_counter()

    return end_time - start_time


def benchmark(
    function,
    data,
    *extra_args,
    repetitions=3
):
    times = []

    for _ in range(repetitions):
        times.append(
            measure_time(
                function,
                data.copy(),
                *extra_args
            )
        )

    return sum(times) / len(times)


def save_results(results):
    output_path = (
        "task5_concurrency/results/"
        "task5_benchmark_results.csv"
    )

    os.makedirs(
        "task5_concurrency/results",
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
                "data_size",
                "thread_count",
                "average_time_seconds",
                "speedup"
            ]
        )

        writer.writeheader()
        writer.writerows(results)


def run_benchmark():
    data_sizes = [
        1_000,
        5_000,
        10_000
    ]

    thread_counts = [
        1,
        2,
        4,
        8
    ]

    results = []

    for data_size in data_sizes:
        data = generate_data(data_size)

        sequential_time = benchmark(
            merge_sort,
            data
        )

        print(
            f"{data_size} items - "
            f"Sequential: "
            f"{sequential_time:.6f} seconds"
        )

        results.append({
            "algorithm": "Sequential",
            "data_size": data_size,
            "thread_count": "N/A",
            "average_time_seconds": sequential_time,
            "speedup": 1.0
        })

        for thread_count in thread_counts:
            executor_time = benchmark(
                parallel_merge_sort,
                data,
                thread_count
            )

            executor_speedup = (
                sequential_time / executor_time
            )

            print(
                f"{data_size} items - "
                f"ThreadPoolExecutor - "
                f"{thread_count} threads: "
                f"{executor_time:.6f} seconds, "
                f"Speedup: "
                f"{executor_speedup:.2f}x"
            )

            results.append({
                "algorithm": "ThreadPoolExecutor",
                "data_size": data_size,
                "thread_count": thread_count,
                "average_time_seconds": executor_time,
                "speedup": executor_speedup
            })

            thread_time = benchmark(
                threaded_merge_sort,
                data,
                thread_count
            )

            thread_speedup = (
                sequential_time / thread_time
            )

            print(
                f"{data_size} items - "
                f"threading.Thread - "
                f"{thread_count} threads: "
                f"{thread_time:.6f} seconds, "
                f"Speedup: "
                f"{thread_speedup:.2f}x"
            )

            results.append({
                "algorithm": "threading.Thread",
                "data_size": data_size,
                "thread_count": thread_count,
                "average_time_seconds": thread_time,
                "speedup": thread_speedup
            })

    save_results(results)


if __name__ == "__main__":
    run_benchmark()