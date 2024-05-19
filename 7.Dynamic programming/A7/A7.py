n = int(input())
path=list(map(int,input().split()))
dp = [0]*n
dp[0] = path[0]
for i in range(1,n):
    dp[i]=path[i]+min(dp[i-1],dp[i-2])
print(dp[-1])