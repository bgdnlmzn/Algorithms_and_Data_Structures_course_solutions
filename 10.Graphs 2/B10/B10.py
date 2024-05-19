import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)]
    min_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if not visited[node]:
            visited[node] = True
            min_weight += weight
            for neighbor, edge_weight in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

    return min_weight


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a-1].append((b-1, w))
    graph[b-1].append((a-1, w))

min_weight = prim(graph)
print(min_weight)