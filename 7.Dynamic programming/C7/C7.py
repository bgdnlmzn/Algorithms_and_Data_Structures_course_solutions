from collections import deque

n, k = map(int, input().split())
path = [0] + list(map(int, input().split())) + [0]
val = [0]*n
prev_i = [-1]*n
answer = []
prev = n-1
d = deque([0])
for i in range(1,n):
    while d and d[0]<i-k:
        d.popleft()
    val[i] = val[d[0]]+path[i]
    prev_i[i]=d[0]
    while d and val[i]>=val[d[-1]]:
        d.pop()
    d.append(i)
while prev >=0:
    answer.append(prev+1)
    prev = prev_i[prev]
answer.reverse()

print(val[n-1])
print(len(answer) - 1)
print(" ".join(map(str, answer)))