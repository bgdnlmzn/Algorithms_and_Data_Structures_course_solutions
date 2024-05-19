n = int(input())
dp = [[1,1,1] for _ in range(n)]
for i in range(1,n):
    dp[i][0]= dp[i-1][0] + dp[i-1][1]+dp[i-1][2]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]+dp[i-1][2]
    dp[i][2] = dp[i-1][0] + dp[i-1][1]
print(sum(dp[-1]))