import heapq


def prim(graph, start):
    visited = set()
    minimum_spanning_tree = []
    priority_queue = [(0, start, None)]
    total_weight = 0

    while priority_queue:
        weight, current_vertex, parent = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        if parent is not None:
            minimum_spanning_tree.append(
                (parent, current_vertex, weight)
            )
            total_weight += weight

        for neighbour, edge_weight in graph.get_neighbours(current_vertex):
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (edge_weight, neighbour, current_vertex)
                )

    return minimum_spanning_tree, total_weight