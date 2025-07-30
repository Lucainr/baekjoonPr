import sys
from collections import deque

def topological_sort(n, edges):
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == n:
        return print(' '.join(map(str, result)))
    else:
        return []

n, m = map(int, sys.stdin.readline().split())
edges = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges.append((a, b))

topological_sort(n, edges)