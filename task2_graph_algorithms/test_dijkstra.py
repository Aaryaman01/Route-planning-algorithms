from task2_graph_algorithms.graph import WeightedDirectedGraph
from task2_graph_algorithms.algorithms.dijkstra import dijkstra


graph = WeightedDirectedGraph()

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("C", "B", 1)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 8)

distances = dijkstra(graph, "A")

print(distances)