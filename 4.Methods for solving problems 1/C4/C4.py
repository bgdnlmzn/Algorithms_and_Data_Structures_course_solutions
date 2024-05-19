import sys
n , k = map(int,sys.stdin.readline().strip().split())
array = list(map(int,sys.stdin.readline().strip().split()))
low = 0
high = array[-1]-array[0]+1
while high-1>low:
    mid = (low + high)//2
    count = 1
    last = array[0]
    for i in range(len(array)):
        if array[i] - last >= mid:
            count+=1
            last = array[i]
    if count >= k:
        low = mid
    else:
        high = mid
sys.stdout.write(str(low))