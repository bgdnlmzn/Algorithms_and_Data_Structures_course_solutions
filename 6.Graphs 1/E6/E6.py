from collections import deque

def d(s, graph):
    dist = [float('inf')] * len(graph)
    q = deque()
    q.append(s)
    dist[s] = 0
    while q:
        v = q.popleft()
        for i in range(len(graph[v])):
            if dist[graph[v][i][0]] > dist[v] + graph[v][i][1]:
                dist[graph[v][i][0]] = dist[v] + graph[v][i][1]
                if graph[v][i][1] == 0:
                    q.appendleft(graph[v][i][0])
                else:
                    q.append(graph[v][i][0])
    return dist[0] + 1

def minNum(n):
    graph = [[] for _ in range(n)]
    for i in range(1, n + 1):
        graph[i % n].append(((i + 1) % n, 1))
        graph[i % n].append(((i * 10) % n, 0))
    return d(1, graph)


n = int(input())
print(minNum(n))