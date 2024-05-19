import heapq

INF = 10**18

def dijkstra(g, s):
    d = [INF] * len(g)
    d[s] = 0
    q = [(0, s)]
    while q:
        dist, u = heapq.heappop(q)
        if dist > d[u]:
            continue
        for v, l in g[u]:
            if d[v] > d[u] + l:
                d[v] = d[u] + l
                heapq.heappush(q, (d[v], v))
    return d


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))
x, y, z = map(int, input().split())
x -= 1
y -= 1
z -= 1

d_x = dijkstra(g, x)
d_y = dijkstra(g, y)
d_z = dijkstra(g, z)

res = INF
for i in range(n):
    d_x_to_i = d_x[i]
    d_y_to_i = d_y[i]
    d_z_to_i = d_z[i]

    if d_x_to_i != INF or d_y_to_i != INF or d_z_to_i != INF:
        min_d = min(d_x_to_i, d_y_to_i, d_z_to_i)
        if min_d == d_x_to_i:
            res = min(res, 2 * min_d + d_y_to_i + d_z_to_i)
        if min_d == d_y_to_i:
            res = min(res, 2 * min_d + d_x_to_i + d_z_to_i)
        if min_d == d_z_to_i:
            res = min(res, 2 * min_d + d_y_to_i + d_x_to_i)

if res != INF:
    print(res)
else:
    print("-1")