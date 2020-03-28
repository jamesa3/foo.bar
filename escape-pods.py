def get_capacity_matrix(entrances, exits, m):
    for i, row in enumerate(m):
        row.insert(0, 0)
        row.append(float('inf') if i in exits else 0)
    entrances = [x + 1 for x in entrances]
    c = list(m)
    n = len(c) + 2
    c.insert(0, [float('inf') if x in entrances else 0 for x in range(n)])
    c.append([0 for x in range(n)])
    return c


def get_adjacencies(c):
    A = []
    for row in c:
        a_row = []
        for i, cell in enumerate(row):
            if cell:
                a_row.append(i)
        A.append(a_row)
    return A


def breadth_first_search(C, A, s, t, F, M, visited):
    queue = [s]
    visited[s] = -2
    while len(queue):
        u = queue.pop(0)
        for v in A[u]:
            if visited[v] == -1 and C[u][v] - F[u][v] > 0:
                visited[v] = u
                M[v] = min(M[u], C[u][v] - F[u][v])
                if v == t:
                    return M[v], visited
                else:
                    queue.append(v)
    return 0, visited


def solution(entrances, exits, path):
    source = 0
    sink = len(path) + 1

    capacity_matrix = get_capacity_matrix(entrances, exits, path)
    adjacencies = get_adjacencies(capacity_matrix)

    n = len(capacity_matrix)
    flow = 0
    residual_capacity = [[0 for x in range(n)] for x in range(n)]

    while True:
        visited = [-1 for x in range(n)]
        M = [0 for x in range(n)]
        M[source] = float('inf')
        path_flow, visited = breadth_first_search(
            capacity_matrix,
            adjacencies,
            source,
            sink,
            residual_capacity,
            M,
            visited
        )
        if path_flow == 0:
            break
        flow += path_flow
        v = sink
        while v != source:
            u = visited[v]
            residual_capacity[u][v] += path_flow
            residual_capacity[v][u] -= path_flow
            v = u
    return flow


def main():
    print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))


if __name__ == '__main__':
    main()