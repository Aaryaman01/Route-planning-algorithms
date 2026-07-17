from task2_graph_algorithms.graph import WeightedDirectedGraph


graph = WeightedDirectedGraph()

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 5)

graph.display()

print(graph.get_vertices())
print(graph.get_neighbours("A"))