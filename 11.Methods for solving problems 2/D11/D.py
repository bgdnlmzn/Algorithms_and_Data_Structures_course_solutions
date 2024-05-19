import math
length, num_points = map(int, input().split())
points = []  
positions = list(map(int, input().split()))
positions.insert(0, 0)
positions.append(length)
num_points += 2

dp = []  
for _ in range(num_points):
    dp.append([0] * num_points)

for j in range(1, num_points):
    for i in range(j - 2, -1, -1):
        dp[i][j] = math.inf
        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        dp[i][j] += positions[j] - positions[i]

print(dp[0][num_points - 1])
