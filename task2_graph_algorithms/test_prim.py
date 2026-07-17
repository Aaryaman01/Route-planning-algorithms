from task2_graph_algorithms.graph import WeightedDirectedGraph
from task2_graph_algorithms.algorithms.prim import prim


graph = WeightedDirectedGraph()

graph.add_edge("A", "B", 4)
graph.add_edge("B", "A", 4)

graph.add_edge("A", "C", 2)
graph.add_edge("C", "A", 2)

graph.add_edge("B", "C", 1)
graph.add_edge("C", "B", 1)

graph.add_edge("B", "D", 5)
graph.add_edge("D", "B", 5)

graph.add_edge("C", "D", 8)
graph.add_edge("D", "C", 8)

minimum_spanning_tree, total_weight = prim(graph, "A")

print(minimum_spanning_tree)
print(total_weight)