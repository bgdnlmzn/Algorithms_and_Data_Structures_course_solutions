n = int(input())
a = list(map(int, input().split()))
d = [1] * n
p = [-1] * n

for i in range(n):
    max_last = 0
    pred = i
    for j in range(i):
        if a[j] < a[i] and d[j] > max_last:
            max_last = d[j]
            pred = j
    d[i] = max_last + 1
    p[i] = pred

cur = d.index(max(d))
print(d[cur])

ans = [a[cur]]
while cur != p[cur]:
    cur = p[cur]
    ans.append(a[cur])
ans.reverse()

print(*ans)