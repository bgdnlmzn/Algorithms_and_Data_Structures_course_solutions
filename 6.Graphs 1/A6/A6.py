import sys
from collections import deque
n,m = map(int,sys.stdin.readline().strip().split())
edges = {}
for _ in range(m):
    first_edge,sec_edge = map(int,sys.stdin.readline().strip().split())
    if first_edge not in edges:
        edges[first_edge] = []
    if sec_edge not in edges:
        edges[sec_edge]= []
    edges[first_edge].append(sec_edge)
    edges[sec_edge].append(first_edge)
for i in range(1,n+1):
    if i not in edges:
        edges[i]=[]
comps = []
visited = set()
for i in range(1,n+1):
    if i in visited:
        continue
    q = deque()
    q.append(i)
    visited.add(i)
    cur_comp = [i]
    while len(q)>0:
        u = q.popleft()
        for t in edges[u]:
            if t in visited:
                continue
            q.append(t)
            visited.add(t)
            cur_comp.append(t)
    cur_comp.sort()
    comps.append(cur_comp)
sys.stdout.write(str(len(comps))+"\n")
for i in range(len(comps)):
    sys.stdout.write(str(len(comps[i]))+"\n")
    sys.stdout.write(" ".join(map(str,comps[i])) + "\n")