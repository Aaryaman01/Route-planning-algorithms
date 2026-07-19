def hamiltonian_cycle(graph):
    vertex_count = len(graph)
    path = [-1] * vertex_count

    path[0] = 0

    def is_safe(vertex, position):
        previous_vertex = path[position - 1]

        if not graph[previous_vertex][vertex]:
            return False

        if vertex in path:
            return False

        return True

    def backtrack(position):
        if position == vertex_count:
            return graph[path[-1]][path[0]] == 1

        for vertex in range(1, vertex_count):
            if is_safe(vertex, position):
                path[position] = vertex

                if backtrack(position + 1):
                    return True

                path[position] = -1

        return False

    if not backtrack(1):
        return None

    return path + [path[0]]