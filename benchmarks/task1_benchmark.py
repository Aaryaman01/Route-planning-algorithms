import csv
import os
from random import Random
from time import perf_counter

from algorithms.data_structures.avl import AVLTree
from algorithms.data_structures.bst import BST
from algorithms.data_structures.hash_table import HashTable
from algorithms.data_structures.min_heap import MinHeap
from models.city import City


DATASET_SIZES = [100, 1_000, 10_000]
SEARCH_COUNT = 1_000
DELETE_COUNT = 100


def generate_cities(n, seed=42):
    rng = Random(seed)

    return [
        City(
            city_id=i,
            name=f"City_{i:05d}",
            latitude=rng.uniform(-90, 90),
            longitude=rng.uniform(-180, 180),
            population=rng.randint(10_000, 10_000_000),
            distance=round(rng.uniform(1, 2_000), 2),
        )
        for i in range(n)
    ]


def measure_bst(cities, search_keys, delete_keys):
    tree = BST()

    start = perf_counter()

    for city in cities:
        tree.insert(city)

    insert_time = perf_counter() - start
    tree_height = tree.height()

    start = perf_counter()

    for city_id in search_keys:
        tree.search(city_id)

    search_time = perf_counter() - start

    start = perf_counter()

    for city_id in delete_keys:
        tree.delete(city_id)

    delete_time = perf_counter() - start

    return {
        "structure": "BST",
        "insert_seconds": insert_time,
        "search_seconds": search_time,
        "delete_seconds": delete_time,
        "peek_seconds": "",
        "extract_min_seconds": "",
        "height": tree_height,
    }


def measure_avl(cities, search_keys, delete_keys):
    tree = AVLTree()

    start = perf_counter()

    for city in cities:
        tree.insert(city)

    insert_time = perf_counter() - start
    tree_height = tree.height()

    start = perf_counter()

    for city_id in search_keys:
        tree.search(city_id)

    search_time = perf_counter() - start

    start = perf_counter()

    for city_id in delete_keys:
        tree.delete(city_id)

    delete_time = perf_counter() - start

    return {
        "structure": "AVL",
        "insert_seconds": insert_time,
        "search_seconds": search_time,
        "delete_seconds": delete_time,
        "peek_seconds": "",
        "extract_min_seconds": "",
        "height": tree_height,
    }


def measure_hash_table(cities, search_keys, delete_keys):
    table = HashTable()

    start = perf_counter()

    for city in cities:
        table.insert(city)

    insert_time = perf_counter() - start

    start = perf_counter()

    for city_id in search_keys:
        table.search(city_id)

    search_time = perf_counter() - start

    start = perf_counter()

    for city_id in delete_keys:
        table.delete(city_id)

    delete_time = perf_counter() - start

    return {
        "structure": "Hash Table",
        "insert_seconds": insert_time,
        "search_seconds": search_time,
        "delete_seconds": delete_time,
        "peek_seconds": "",
        "extract_min_seconds": "",
        "height": "",
    }


def measure_min_heap(cities):
    heap = MinHeap()

    start = perf_counter()

    for city in cities:
        heap.insert(city)

    insert_time = perf_counter() - start

    start = perf_counter()
    heap.peek()
    peek_time = perf_counter() - start

    start = perf_counter()

    for _ in range(min(100, len(cities))):
        heap.extract_min()

    extract_time = perf_counter() - start

    return {
        "structure": "Min-Heap",
        "insert_seconds": insert_time,
        "search_seconds": "",
        "delete_seconds": "",
        "peek_seconds": peek_time,
        "extract_min_seconds": extract_time,
        "height": "",
    }


def run_benchmark():
    results = []
    rng = Random(42)

    for size in DATASET_SIZES:
        cities = generate_cities(size)

        search_keys = [
            rng.randrange(size)
            for _ in range(SEARCH_COUNT)
        ]

        delete_count = min(DELETE_COUNT, size)
        delete_keys = list(range(delete_count))

        results.append({
            "dataset_size": size,
            **measure_bst(cities, search_keys, delete_keys),
        })

        results.append({
            "dataset_size": size,
            **measure_avl(cities, search_keys, delete_keys),
        })

        results.append({
            "dataset_size": size,
            **measure_hash_table(cities, search_keys, delete_keys),
        })

        results.append({
            "dataset_size": size,
            **measure_min_heap(cities),
        })

    return results


def save_results(results):
    os.makedirs("results", exist_ok=True)

    output_file = "results/task1_benchmark_results.csv"

    fieldnames = [
        "dataset_size",
        "structure",
        "insert_seconds",
        "search_seconds",
        "delete_seconds",
        "peek_seconds",
        "extract_min_seconds",
        "height",
    ]

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    benchmark_results = run_benchmark()

    for result in benchmark_results:
        print(result)

    save_results(benchmark_results)