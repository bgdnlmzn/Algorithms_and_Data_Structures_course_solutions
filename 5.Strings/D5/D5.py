s = input().strip()
n = len(s)
i = 0
j = 1
k = 0
while i+k < n and j+k < n:
    if s[i+k] == s[j+k]:
        k += 1
    elif s[i+k] > s[j+k]:
        i = max(i+k+1, j+1)
        k = 0
    else:
        j = max(j+k+1, i+1)
        k = 0
    if i == j:
        j += 1
index = min(i, j)
result = s[index:]+s[:index]
print(result)