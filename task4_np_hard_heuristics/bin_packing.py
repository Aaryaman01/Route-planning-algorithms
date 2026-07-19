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