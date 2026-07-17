import csv
import os
import random
import time

from task2_graph_algorithms.graph import WeightedDirectedGraph
from task2_graph_algorithms.algorithms.dijkstra import dijkstra
from task2_graph_algorithms.algorithms.prim import prim
from task2_graph_algorithms.algorithms.bellman_ford import bellman_ford


def generate_graph(vertex_count, edge_count, seed=42):
    random.seed(seed)

    graph = WeightedDirectedGraph()

    for vertex in range(vertex_count):
        graph.add_vertex(vertex)

    edges_added = 0

    while edges_added < edge_count:
        source = random.randrange(vertex_count)
        destination = random.randrange(vertex_count)

        if source == destination:
            continue

        weight = random.randint(1, 100)

        graph.add_edge(source, destination, weight)
        edges_added += 1

    return graph


def generate_undirected_graph(vertex_count, edge_count, seed=42):
    random.seed(seed)

    graph = WeightedDirectedGraph()

    for vertex in range(vertex_count):
        graph.add_vertex(vertex)

    edges_added = 0
    existing_edges = set()

    while edges_added < edge_count:
        source = random.randrange(vertex_count)
        destination = random.randrange(vertex_count)

        if source == destination:
            continue

        edge = tuple(sorted((source, destination)))

        if edge in existing_edges:
            continue

        existing_edges.add(edge)

        weight = random.randint(1, 100)

        graph.add_edge(source, destination, weight)
        graph.add_edge(destination, source, weight)

        edges_added += 1

    return graph


def measure_time(function, *args):
    start_time = time.perf_counter()

    function(*args)

    end_time = time.perf_counter()

    return end_time - start_time


def benchmark_algorithm(function, graph, start_vertex, repetitions=5):
    times = []

    for _ in range(repetitions):
        elapsed_time = measure_time(
            function,
            graph,
            start_vertex
        )

        times.append(elapsed_time)

    return sum(times) / len(times)


def save_results(results):
    output_path = (
        "task2_graph_algorithms/results/"
        "task2_benchmark_results.csv"
    )

    os.makedirs(
        "task2_graph_algorithms/results",
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
                "vertices",
                "edges",
                "average_time_seconds"
            ]
        )

        writer.writeheader()
        writer.writerows(results)


def run_benchmark():
    graph_sizes = [
        (100, 500),
        (500, 2_000),
        (1_000, 5_000)
    ]

    results = []

    for vertex_count, edge_count in graph_sizes:
        print(
            f"\nTesting {vertex_count} vertices "
            f"and {edge_count} edges"
        )

        directed_graph = generate_graph(
            vertex_count,
            edge_count
        )

        undirected_graph = generate_undirected_graph(
            vertex_count,
            edge_count
        )

        dijkstra_time = benchmark_algorithm(
            dijkstra,
            directed_graph,
            0
        )

        bellman_ford_time = benchmark_algorithm(
            bellman_ford,
            directed_graph,
            0
        )

        prim_time = benchmark_algorithm(
            prim,
            undirected_graph,
            0
        )

        print(
            f"Dijkstra: {dijkstra_time:.6f} seconds"
        )

        print(
            f"Bellman-Ford: "
            f"{bellman_ford_time:.6f} seconds"
        )

        print(
            f"Prim: {prim_time:.6f} seconds"
        )

        results.extend([
            {
                "algorithm": "Dijkstra",
                "vertices": vertex_count,
                "edges": edge_count,
                "average_time_seconds": dijkstra_time
            },
            {
                "algorithm": "Bellman-Ford",
                "vertices": vertex_count,
                "edges": edge_count,
                "average_time_seconds": bellman_ford_time
            },
            {
                "algorithm": "Prim",
                "vertices": vertex_count,
                "edges": edge_count,
                "average_time_seconds": prim_time
            }
        ])

    save_results(results)


if __name__ == "__main__":
    run_benchmark()