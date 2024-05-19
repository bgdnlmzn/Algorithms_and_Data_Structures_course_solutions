n = int(input())
papa = list(map(int, input().split()))
d = 1
h = 0
tree = [(0, []) for _ in range(n)]
mas = [[0, 0] for _ in range(n)]
invert_tree = [[] for _ in range(n)]
value = 0
for i in range(1, n):
    x = papa[value]
    value += 1
    tree[x][1].append(i)
    tree[i] = (tree[x][0] + 1, [])
    h = max(h, tree[x][0] + 1)
    invert_tree[i].append(x)

for i in range(n - 1, -1, -1):
    if invert_tree[i]:
        j = invert_tree[i][0]
        if mas[j][0] <= mas[i][0] + 1:
            mas[j][1] = mas[j][0]
            mas[j][0] = mas[i][0] + 1
        elif mas[j][1] <= mas[i][0] + 1:
            mas[j][1] = mas[i][0] + 1
    d = max(d, mas[i][0] + mas[i][1])
print(h,d)
for i in tree:
    print(i[0], end=' ')