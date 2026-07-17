class MinHeap:
    def __init__(self):
        self._items = []

    def insert(self, city):
        self._items.append(city)
        self._sift_up(len(self._items) - 1)

    def peek(self):
        if not self._items:
            return None

        return self._items[0]

    def extract_min(self):
        if not self._items:
            return None

        if len(self._items) == 1:
            return self._items.pop()

        minimum = self._items[0]
        self._items[0] = self._items.pop()
        self._sift_down(0)

        return minimum

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self._items[index].distance >= self._items[parent].distance:
                break

            self._items[index], self._items[parent] = (
                self._items[parent],
                self._items[index],
            )

            index = parent

    def _sift_down(self, index):
        size = len(self._items)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if (
                left < size
                and self._items[left].distance
                < self._items[smallest].distance
            ):
                smallest = left

            if (
                right < size
                and self._items[right].distance
                < self._items[smallest].distance
            ):
                smallest = right

            if smallest == index:
                break

            self._items[index], self._items[smallest] = (
                self._items[smallest],
                self._items[index],
            )

            index = smallest

    def __len__(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0