import sys
from collections import deque

n = int(sys.stdin.readline().strip())
x1, y1 = map(int, sys.stdin.readline().strip().split())
x2, y2 = map(int, sys.stdin.readline().strip().split())
path_of = []
vertices = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        vertices.append((i, j))
moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
edges = {}
for (i, j) in vertices:
    if (i, j) not in edges.keys():
        edges[(i, j)] = []
    for (dx, dy) in moves:
        nx = i + dx
        ny = j + dy
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
            edges[(i, j)].append((nx, ny))
q = deque()
visited = set()
pr = {}
q.append((x1, y1))
visited.add((x1, y1))
answer = 0
while len(q) > 0:
    x, y = q.popleft()
    if (x, y) == (x2, y2):
        path = []
        while (x, y) in pr:
            path.append((x, y))
            x, y = pr[(x, y)]
        path.append((x, y))
        answer = (len(path) - 1)
        for i in path:
            path_of.append((i[0], i[1]))
        break

    for t in edges[(x, y)]:
        if t not in visited:
            visited.add(t)
            pr[t] = (x, y)
            q.append(t)

sys.stdout.write(str(answer) + '\n')
for i in reversed(path):
    sys.stdout.write(str(i[0]) + ' ' + str(i[1]) + '\n')