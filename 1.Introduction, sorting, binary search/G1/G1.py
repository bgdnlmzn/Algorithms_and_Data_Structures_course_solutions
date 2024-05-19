n = int(input())
a=[]
for i in range(n):
    a.append(i+1)
for i in range(n):
    a[i],a[i//2] = a[i//2],a[i]
for i in a:
    print(i, end=' ')