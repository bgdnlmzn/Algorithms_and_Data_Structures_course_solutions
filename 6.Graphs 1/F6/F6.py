from collections import deque

def bfs(s, end, gr):
    visited = set()
    queue = deque([(s, 0)])
    visited.add(s)

    while queue:
        g, level = queue.popleft()
        for t in gr[g]:
            if t not in visited:
                if t == end:
                    return level + 1
                queue.append((t, level + 1))
                visited.add(t)
    return -1


subst = {}
gr = []
ch = 1

m = int(input())
for i in range(m):
    v1, i, v2 = input().split()
    if v1 not in subst:
        subst[v1] = ch
        ch += 1
    if v2 not in subst:
        subst[v2] = ch
        ch += 1
    while len(gr) < ch + 1:
        gr.append([])
    gr[subst[v1]].append(subst[v2])

v1 = input()
v2 = input()
if v1 not in subst or v2 not in subst:
    print(-1)
else:
    print(bfs(subst[v1], subst[v2], gr))
