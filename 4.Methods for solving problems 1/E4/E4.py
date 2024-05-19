import sys
n,k = map(int,sys.stdin.readline().strip().split())
array = list(map(int,sys.stdin.readline().strip().split()))
low = max(array)
high = sum(array)
while low <= high:
    mid = (low+high)//2
    k_otrezkov = 0
    summa = 0
    for i in range(len(array)):
        summa+=array[i]
        if summa > mid:
            k_otrezkov+=1
            summa = array[i]
    if k_otrezkov<k:
        high = mid-1
    else:
        low = mid+1
sys.stdout.write(str(low))