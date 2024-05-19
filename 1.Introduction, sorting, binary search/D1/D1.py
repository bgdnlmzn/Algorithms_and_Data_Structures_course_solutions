c = float(input())
accuracy = 10**(-5)
low = 0
high = c
while low <= high:
    mid = (low + high)/2
    expr = mid**2 + (mid+1)**0.5
    if abs(expr-c) <= accuracy:
        break
    if expr > c:
        high = mid
    else:
        low = mid
print(mid)