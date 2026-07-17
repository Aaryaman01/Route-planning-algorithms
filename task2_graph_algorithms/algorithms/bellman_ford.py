def bellman_ford(graph, start):
    vertices = graph.get_vertices()

    distances = {
        vertex: float("inf")
        for vertex in vertices
    }

    distances[start] = 0

    for _ in range(len(vertices) - 1):
        updated = False

        for source in vertices:
            if distances[source] == float("inf"):
                continue

            for destination, weight in graph.get_neighbours(source):
                new_distance = distances[source] + weight

                if new_distance < distances[destination]:
                    distances[destination] = new_distance
                    updated = True

        if not updated:
            break

    for source in vertices:
        if distances[source] == float("inf"):
            continue

        for destination, weight in graph.get_neighbours(source):
            if distances[source] + weight < distances[destination]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances