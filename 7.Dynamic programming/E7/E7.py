s = input()
t = input()
m = len(s) # len 1 str
n = len(t) # len 2 str
d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
for i in range(m+1):
    d[i][0] = i
for j in range(n+1):
    d[0][j] = j
for i in range(1, m+1):
    for j in range(1, n+1):
        if s[i-1] == t[j-1]:
            cost = 0
        else:
            cost =1
        d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+cost)
        if i > 1 and j > 1 and s[i-1] == t[j-2] and s[i-2] == t[j-1]:
            d[i][j] = min(d[i][j], d[i-2][j-2]+cost)
print(d[m][n])