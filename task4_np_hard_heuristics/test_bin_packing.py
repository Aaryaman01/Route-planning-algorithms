from task4_np_hard_heuristics.bin_packing import (
    first_fit_decreasing
)


items = [
    [4, 2, 3],
    [2, 5, 1],
    [6, 3, 2],
    [3, 4, 4],
    [5, 2, 2]
]

capacity = [10, 10, 10]

bins = first_fit_decreasing(
    items,
    capacity
)

print("Number of bins:", len(bins))

for index, bin_container in enumerate(bins, start=1):
    print(
        f"Bin {index}:",
        bin_container.items,
        "Remaining:",
        bin_container.remaining
    )