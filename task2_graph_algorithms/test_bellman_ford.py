from task2_graph_algorithms.graph import WeightedDirectedGraph
from task2_graph_algorithms.algorithms.bellman_ford import bellman_ford


graph = WeightedDirectedGraph()

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "C", -2)
graph.add_edge("C", "D", 3)
graph.add_edge("B", "D", 4)

distances = bellman_ford(graph, "A")

print(distances)