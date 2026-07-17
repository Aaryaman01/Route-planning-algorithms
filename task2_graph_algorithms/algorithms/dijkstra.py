import heapq


def dijkstra(graph, start):
    distances = {
        vertex: float("inf")
        for vertex in graph.get_vertices()
    }

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbour, weight in graph.get_neighbours(current_vertex):
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(
                    priority_queue,
                    (distance, neighbour)
                )

    return distances