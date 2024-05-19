import sys
n,m = map(int,sys.stdin.readline().strip().split())
edges =[]
for _ in range(m):
    edge = map(int,sys.stdin.readline().strip().split())
    edges.append(edge)
pos = [0]*(n+1)
answer = 'YES'
topo = list(map(int,sys.stdin.readline().strip().split()))
for i in range(n):
    pos[topo[i]]=i
for i,j in edges:
    if pos[i]>pos[j]:
        answer = 'NO'
        break
sys.stdout.write(str(answer))