class BSTNode:
    __slots__ = ("city", "left", "right")

    def __init__(self, city):
        self.city = city
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, city):
        if self.root is None:
            self.root = BSTNode(city)
            self._size = 1
            return

        node = self.root

        while True:
            if city.city_id < node.city.city_id:
                if node.left is None:
                    node.left = BSTNode(city)
                    self._size += 1
                    return
                node = node.left

            elif city.city_id > node.city.city_id:
                if node.right is None:
                    node.right = BSTNode(city)
                    self._size += 1
                    return
                node = node.right

            else:
                node.city = city
                return

    def search(self, city_id):
        node = self.root

        while node is not None:
            if city_id == node.city.city_id:
                return node.city

            if city_id < node.city.city_id:
                node = node.left
            else:
                node = node.right

        return None

    def delete(self, city_id):
        self.root, deleted = self._delete(self.root, city_id)

        if deleted:
            self._size -= 1

        return deleted

    def _delete(self, node, city_id):
        if node is None:
            return None, False

        if city_id < node.city.city_id:
            node.left, deleted = self._delete(node.left, city_id)
            return node, deleted

        if city_id > node.city.city_id:
            node.right, deleted = self._delete(node.right, city_id)
            return node, deleted

        if node.left is None:
            return node.right, True

        if node.right is None:
            return node.left, True

        successor = node.right

        while successor.left is not None:
            successor = successor.left

        node.city = successor.city
        node.right, _ = self._delete(
            node.right,
            successor.city.city_id
        )

        return node, True

    def height(self):
        if self.root is None:
            return 0

        stack = [(self.root, 1)]
        highest = 0

        while stack:
            node, depth = stack.pop()
            highest = max(highest, depth)

            if node.left is not None:
                stack.append((node.left, depth + 1))

            if node.right is not None:
                stack.append((node.right, depth + 1))

        return highest

    def __len__(self):
        return self._size