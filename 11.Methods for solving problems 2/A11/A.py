from collections import defaultdict
from math import log2  # Добавленный импорт

class LCA:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.depth = [0] * n
        self.parent = [[-1] * int(log2(n) + 1) for _ in range(n)]
        self._preprocess()

    def _preprocess(self):
        graph = defaultdict(list)
        for u, v in self.edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, par, d):
            self.parent[node][0] = par
            self.depth[node] = d
            for child in graph[node]:
                if child != par:
                    dfs(child, node, d + 1)

        dfs(0, -1, 0)

        for i in range(1, int(log2(self.n)) + 1):
            for node in range(self.n):
                if self.parent[node][i - 1] != -1:
                    self.parent[node][i] = self.parent[self.parent[node][i - 1]][i - 1]

    def find_lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]

        while diff > 0:
            l = int(log2(diff))
            u = self.parent[u][l]
            diff -= (1 << l)

        if u == v:
            return u

        for i in range(int(log2(self.n)), -1, -1):
            if self.parent[u][i] != -1 and self.parent[u][i] != self.parent[v][i]:
                u = self.parent[u][i]
                v = self.parent[v][i]

        return self.parent[u][0]
n = int(input())
edges = []
p = list(map(int,input().split()))
for i in range(n - 1):
    pi = p[i]
    edges.append((pi, i + 1))
m = int(input())
queries = []
for _ in range(m):
    u, v = map(int, input().split())
    queries.append((u, v))


lca = LCA(n, edges)
for u, v in queries:
    print(lca.find_lca(u, v))



