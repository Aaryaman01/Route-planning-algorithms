import csv
import os

import matplotlib.pyplot as plt


INPUT_FILE = "task1_data_structures/results/task1_benchmark_results.csv"
OUTPUT_DIR = "task1_data_structures/results/figures"


def load_results():
    results = []

    with open(INPUT_FILE, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            results.append(row)

    return results


def plot_operation_times(results):
    structures = ["BST", "AVL", "Hash Table", "Min-Heap"]

    for operation in [
        "insert_seconds",
        "search_seconds",
        "delete_seconds",
    ]:
        plt.figure()

        for structure in structures:
            sizes = []
            times = []

            for row in results:
                if row["structure"] == structure:
                    value = row[operation]

                    if value != "":
                        sizes.append(int(row["dataset_size"]))
                        times.append(float(value))

            if times:
                plt.plot(
                    sizes,
                    times,
                    marker="o",
                    label=structure,
                )

        plt.xlabel("Number of Cities")
        plt.ylabel("Time (seconds)")
        plt.title(f"{operation.replace('_', ' ').title()} Comparison")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        output_file = os.path.join(
            OUTPUT_DIR,
            f"{operation}.png",
        )

        plt.savefig(output_file)
        plt.close()


def plot_heap_operations(results):
    plt.figure()

    sizes = []
    peek_times = []
    extract_times = []

    for row in results:
        if row["structure"] == "Min-Heap":
            sizes.append(int(row["dataset_size"]))
            peek_times.append(float(row["peek_seconds"]))
            extract_times.append(float(row["extract_min_seconds"]))

    plt.plot(
        sizes,
        peek_times,
        marker="o",
        label="Peek",
    )

    plt.plot(
        sizes,
        extract_times,
        marker="o",
        label="Extract-Min",
    )

    plt.xlabel("Number of Cities")
    plt.ylabel("Time (seconds)")
    plt.title("Min-Heap Priority Operations")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    output_file = os.path.join(
        OUTPUT_DIR,
        "min_heap_operations.png",
    )

    plt.savefig(output_file)
    plt.close()


def plot_tree_heights(results):
    plt.figure()

    for structure in ["BST", "AVL"]:
        sizes = []
        heights = []

        for row in results:
            if row["structure"] == structure:
                sizes.append(int(row["dataset_size"]))
                heights.append(int(row["height"]))

        plt.plot(
            sizes,
            heights,
            marker="o",
            label=structure,
        )

    plt.xlabel("Number of Cities")
    plt.ylabel("Tree Height")
    plt.title("BST and AVL Tree Height Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    output_file = os.path.join(
        OUTPUT_DIR,
        "tree_height_comparison.png",
    )

    plt.savefig(output_file)
    plt.close()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    results = load_results()

    plot_operation_times(results)
    plot_heap_operations(results)
    plot_tree_heights(results)

    print(f"Figures saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()