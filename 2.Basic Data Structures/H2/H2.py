def left_s(arr, n):
    stack = []
    left = [-1] * n

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    return left


def right_s(arr, n):
    stack = []
    right = [n] * n

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    return right


def prefix_sum(arr, n):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    return prefix_sum


n = int(input())
arr = list(map(int, input().split()))
s_r = right_s(arr, n)
s_l = left_s(arr, n)
prefix = prefix_sum(arr, n)

maximum = 0
for i in range(n):
    summa = (prefix[s_r[i]] - prefix[s_l[i] + 1]) * arr[i]
    if summa > maximum:
        maximum = summa
print(maximum)
