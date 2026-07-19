import csv
import os
import random
import time

from task3_algorithmic_strategies.weighted_job_scheduling import (
    Job,
    weighted_job_scheduling
)
from task3_algorithmic_strategies.minimum_platforms import (
    minimum_platforms
)
from task3_algorithmic_strategies.hamiltonian_cycle import (
    hamiltonian_cycle
)


def generate_jobs(job_count, seed=42):
    random.seed(seed)

    jobs = []

    for _ in range(job_count):
        start = random.randint(0, job_count * 2)
        duration = random.randint(1, 10)
        finish = start + duration
        profit = random.randint(10, 1_000)

        jobs.append(
            Job(
                start=start,
                finish=finish,
                profit=profit
            )
        )

    return jobs


def generate_train_schedule(train_count, seed=42):
    random.seed(seed)

    arrivals = []
    departures = []

    for _ in range(train_count):
        arrival = random.randint(0, 2_000)
        departure = arrival + random.randint(1, 100)

        arrivals.append(arrival)
        departures.append(departure)

    return arrivals, departures


def generate_graph(vertex_count, seed=42):
    random.seed(seed)

    graph = [
        [0] * vertex_count
        for _ in range(vertex_count)
    ]

    for i in range(vertex_count):
        for j in range(i + 1, vertex_count):
            if random.random() < 0.7:
                graph[i][j] = 1
                graph[j][i] = 1

    return graph


def measure_time(function, *args):
    start_time = time.perf_counter()

    function(*args)

    end_time = time.perf_counter()

    return end_time - start_time


def benchmark_algorithm(function, *args, repetitions=5):
    times = []

    for _ in range(repetitions):
        elapsed_time = measure_time(function, *args)
        times.append(elapsed_time)

    return sum(times) / len(times)


def save_results(results):
    output_path = (
        "task3_algorithmic_strategies/results/"
        "task3_benchmark_results.csv"
    )

    os.makedirs(
        "task3_algorithmic_strategies/results",
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
                "input_size",
                "average_time_seconds"
            ]
        )

        writer.writeheader()
        writer.writerows(results)


def run_benchmark():
    results = []

    job_sizes = [100, 500, 1_000]

    for size in job_sizes:
        jobs = generate_jobs(size)

        elapsed_time = benchmark_algorithm(
            weighted_job_scheduling,
            jobs
        )

        print(
            f"Weighted Job Scheduling "
            f"({size} jobs): "
            f"{elapsed_time:.6f} seconds"
        )

        results.append({
            "algorithm": "Weighted Job Scheduling",
            "input_size": size,
            "average_time_seconds": elapsed_time
        })

    train_sizes = [100, 500, 1_000]

    for size in train_sizes:
        arrivals, departures = generate_train_schedule(size)

        elapsed_time = benchmark_algorithm(
            minimum_platforms,
            arrivals,
            departures
        )

        print(
            f"Minimum Platforms "
            f"({size} trains): "
            f"{elapsed_time:.6f} seconds"
        )

        results.append({
            "algorithm": "Minimum Platforms",
            "input_size": size,
            "average_time_seconds": elapsed_time
        })

    graph_sizes = [6, 8, 10, 12]

    for size in graph_sizes:
        graph = generate_graph(size)

        elapsed_time = benchmark_algorithm(
            hamiltonian_cycle,
            graph
        )

        print(
            f"Hamiltonian Cycle "
            f"({size} vertices): "
            f"{elapsed_time:.6f} seconds"
        )

        results.append({
            "algorithm": "Hamiltonian Cycle",
            "input_size": size,
            "average_time_seconds": elapsed_time
        })

    save_results(results)


if __name__ == "__main__":
    run_benchmark()