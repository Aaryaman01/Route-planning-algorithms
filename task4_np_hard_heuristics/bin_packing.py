class Bin:
    def __init__(self, capacity):
        self.capacity = capacity
        self.remaining = capacity.copy()
        self.items = []

    def can_fit(self, item):
        return all(
            item[i] <= self.remaining[i]
            for i in range(len(item))
        )

    def add_item(self, item):
        if not self.can_fit(item):
            return False

        for i in range(len(item)):
            self.remaining[i] -= item[i]

        self.items.append(item)

        return True


def first_fit_decreasing(items, capacity):
    sorted_items = sorted(
        items,
        key=lambda item: sum(item),
        reverse=True
    )

    bins = []

    for item in sorted_items:
        placed = False

        for bin_container in bins:
            if bin_container.add_item(item):
                placed = True
                break

        if not placed:
            new_bin = Bin(capacity.copy())
            new_bin.add_item(item)
            bins.append(new_bin)

    return bins


def local_search(bins):
    improved = True

    while improved:
        improved = False

        for source_index in range(len(bins) - 1, -1, -1):
            source_bin = bins[source_index]

            for target_index in range(len(bins)):
                if source_index == target_index:
                    continue

                target_bin = bins[target_index]

                if all(
                    target_bin.can_fit(item)
                    for item in source_bin.items
                ):
                    for item in source_bin.items:
                        target_bin.add_item(item)

                    bins.pop(source_index)
                    improved = True
                    break

            if improved:
                break

    return bins