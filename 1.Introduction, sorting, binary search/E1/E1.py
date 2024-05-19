a,b,c,d = map(int,input().split())
accuracy = 10**(-7)
low = -100000000000000000000000
high = 100000000000000000000000
def expr(value):
    return a*value**3 + b*value**2 + c*value + d
while abs(high-low)>accuracy:
    mid = (low + high)/2
    if expr(mid)*expr(high)>0:
        high = mid
    else:
        low = mid
print(high)