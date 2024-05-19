import sys

t = int(sys.stdin.readline().strip())
res = []
for _ in range(t):
    line = sys.stdin.readline().strip()
    n, m = map(int, line.split())

    dif1 = float('inf')
    dif2 = float('inf')
    k1 = 0
    k2 = 0
    left = 0
    right = m - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        leftSum = (((n - 1) * m * n + ((mid + 1) + 1) * n) * (mid + 1)) / 2
        rightSum = (((n - 1) * m * n + ((mid + 1) + 1 + m) * n) * (m - (mid + 1))) / 2
        if abs(leftSum - rightSum) < dif1:
            dif1 = abs(leftSum - rightSum)
            k1 = mid + 1
        elif abs(leftSum - rightSum) == dif1:
            if k1 > mid + 1:
                k1 = mid + 1
        if leftSum > rightSum:
            right = mid - 1
        else:
            left = mid + 1

    mid = 0
    left = 0
    right = n - 1

    while left <= right:

        mid = (left + right) // 2
        upSum = (((mid + 1) * m * m + m) * (mid + 1)) // 2
        downSum = ((((mid + 1) + n) * m * m + m) * (n - (mid + 1))) // 2
        if abs(upSum - downSum) < dif2:
            dif2 = abs(upSum - downSum)
            k2 = mid + 1
        elif abs(upSum - downSum) == dif2:
            if k2 > mid + 1:
                k2 = mid + 1
        if upSum > downSum:
            right = mid - 1
        else:
            left = mid + 1

    if dif1 <= dif2:
        res.append(f'V {k1 + 1}')
    else:
        res.append(f'H {k2 + 1}')
sys.stdout.write('\n'.join(res))