n, m = map(int, input().split())
dp = []
for i in range(n):
    dp.append(list([0 for j in range(m)]))
dp[0][0] = 1
def rec(i, j):
    if i >= 0 and j >= 0 and i < n and j < m:
        if dp[i][j] == 0:
            dp[i][j] = rec(i-2, j-1)+rec(i-2, j+1)+rec(i-1, j-2)+rec(i+1, j-2)
    else:
        return 0
    return dp[i][j]
print(rec(n-1, m-1))