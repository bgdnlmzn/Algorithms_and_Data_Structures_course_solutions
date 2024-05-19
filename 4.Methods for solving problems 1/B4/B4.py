import sys

n, m, q = map(int, sys.stdin.readline().strip().split())
matrix = []
for i in range(n):
    array = list(map(int, sys.stdin.readline().strip().split()))
    matrix.append(array)
prefix2d = []
for i in range(len(matrix) + 1):
    prefix2d.append((len(matrix[0]) + 1) * [0])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        prefix2d[i + 1][j + 1] = prefix2d[i][j + 1] + prefix2d[i + 1][j] + matrix[i][j] - prefix2d[i][j]

answer = []
for _ in range(q):
    some_q = list(map(int, sys.stdin.readline().strip().split()))
    x1 = some_q[0]
    y1 = some_q[1]
    x2 = some_q[2]
    y2 = some_q[3]
    answer.append(str(prefix2d[x2][y2] - prefix2d[x2][y1 - 1] - prefix2d[x1 - 1][y2] + prefix2d[x1 - 1][y1 - 1]))

sys.stdout.write('\n'.join(answer))