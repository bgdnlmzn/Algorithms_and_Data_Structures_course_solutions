import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
edges = {}
for _ in range(m):
    first_edge, sec_edge = map(int, sys.stdin.readline().strip().split())
    if first_edge not in edges:
        edges[first_edge] = []
    edges[first_edge].append(sec_edge)
for i in range(1, n + 1):
    if i not in edges:
        edges[i] = []


def cycle(edges):
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for i in edges.get(node):
            if dfs(i):
                return True

        stack.remove(node)
        return False

    for node in edges:
        if dfs(node):
            return True

    return False


answer = cycle(edges)
if answer:
    sys.stdout.write(str(1))
else:
    sys.stdout.write(str(0))

# sys.stdout.write(str(answer))