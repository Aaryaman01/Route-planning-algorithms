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


if __name__ == "__main__":
    directed_graph = generate_graph(100, 500)
    undirected_graph = generate_undirected_graph(100, 500)

    print(
        "Dijkstra:",
        measure_time(dijkstra, directed_graph, 0)
    )

    print(
        "Bellman-Ford:",
        measure_time(bellman_ford, directed_graph, 0)
    )

    print(
        "Prim:",
        measure_time(prim, undirected_graph, 0)
    )