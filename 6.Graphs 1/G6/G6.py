def d(s, graph):
    dist = [float('inf')] * len(graph)
    dist[s] = 0
    ch = [False] * len(graph)
    while True:
        v = -1
        for i in range(1, len(graph)):
            if not ch[i] and (v == -1 or dist[i] < dist[v]):
                v = i
        if v == -1:
            break
        ch[v] = True
        for u, l in graph[v]:
            if dist[u] > dist[v] + l:
                dist[u] = dist[v] + l
    mas = 0
    for i in range(1, len(dist)):
        mas = max(mas, dist[i])
    return mas


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
minimum = float('inf')
c = -1
for i in range(1, n+1):
    dist = d(i, graph)
    if dist < minimum:
        c = i
        minimum = dist
print(c)