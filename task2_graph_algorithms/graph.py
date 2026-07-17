class WeightedDirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)

        self.adjacency_list[source].append((destination, weight))

    def get_neighbours(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")