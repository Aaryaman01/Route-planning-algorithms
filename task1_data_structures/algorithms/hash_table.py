class HashTable:
    def __init__(self, capacity=8):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _index(self, city_id):
        return city_id % len(self._buckets)

    def _resize(self):
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(len(old_buckets) * 2)]
        self._size = 0

        for bucket in old_buckets:
            for city_id, city in bucket:
                self.insert(city)

    def insert(self, city):
        index = self._index(city.city_id)
        bucket = self._buckets[index]

        for position, (city_id, _) in enumerate(bucket):
            if city_id == city.city_id:
                bucket[position] = (city.city_id, city)
                return

        bucket.append((city.city_id, city))
        self._size += 1

        if self._size / len(self._buckets) > 0.75:
            self._resize()

    def search(self, city_id):
        index = self._index(city_id)

        for stored_id, city in self._buckets[index]:
            if stored_id == city_id:
                return city

        return None

    def delete(self, city_id):
        index = self._index(city_id)
        bucket = self._buckets[index]

        for position, (stored_id, _) in enumerate(bucket):
            if stored_id == city_id:
                bucket.pop(position)
                self._size -= 1
                return True

        return False

    def __len__(self):
        return self._size

    def capacity(self):
        return len(self._buckets)