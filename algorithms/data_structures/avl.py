class AVLNode:
    __slots__ = ("city", "left", "right", "height")

    def __init__(self, city):
        self.city = city
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(
            self._height(node.left),
            self._height(node.right)
        )

    def _balance_factor(self, node):
        if node is None:
            return 0

        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node):
        child = node.left
        subtree = child.right

        child.right = node
        node.left = subtree

        self._update_height(node)
        self._update_height(child)

        return child

    def _rotate_left(self, node):
        child = node.right
        subtree = child.left

        child.left = node
        node.right = subtree

        self._update_height(node)
        self._update_height(child)

        return child

    def _rebalance(self, node):
        self._update_height(node)

        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)

            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)

            return self._rotate_left(node)

        return node

    def insert(self, city):
        existing = self.search(city.city_id)

        if existing is not None:
            self._insert(self.root, city)
            return

        self.root = self._insert(self.root, city)
        self._size += 1

    def _insert(self, node, city):
        if node is None:
            return AVLNode(city)

        if city.city_id < node.city.city_id:
            node.left = self._insert(node.left, city)

        elif city.city_id > node.city.city_id:
            node.right = self._insert(node.right, city)

        else:
            node.city = city
            return node

        return self._rebalance(node)

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
        if self.search(city_id) is None:
            return False

        self.root = self._delete(self.root, city_id)
        self._size -= 1

        return True

    def _delete(self, node, city_id):
        if node is None:
            return None

        if city_id < node.city.city_id:
            node.left = self._delete(node.left, city_id)

        elif city_id > node.city.city_id:
            node.right = self._delete(node.right, city_id)

        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = node.right

            while successor.left is not None:
                successor = successor.left

            node.city = successor.city
            node.right = self._delete(
                node.right,
                successor.city.city_id
            )

        return self._rebalance(node)

    def height(self):
        return self._height(self.root)

    def __len__(self):
        return self._size