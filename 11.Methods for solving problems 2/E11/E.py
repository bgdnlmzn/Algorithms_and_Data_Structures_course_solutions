import sys

def expand(Left, Right, current):
    global string, Prev
    previous = Prev[Left][Right]
    if previous == 0:
        return current + string[Left:Right + 1]
    if previous > 0:

        return expand(Left + previous, Right, expand(Left, Left + previous - 1, current))

    return current + str(-(Right - Left + 1) // previous) + "(" + expand(Left, Left - previous - 1, "") + ")"


string = input().strip()
length = len(string)

DP = [[0] * length for _ in range(1001)]
Prev = [[0] * length for _ in range(1001)]
LCP = [[0] * (length + 1) for _ in range(1001)]

for i in range(length - 1, -1, -1):
    for j in range(length - 1, i - 1, -1):
        if string[i] == string[j]:
            LCP[i][j] = 1 + LCP[i + 1][j + 1]

for l in range(1, length + 1):
    for left in range(length - l + 1):
        right = left + l - 1
        DP[left][right] = l

        for m in range(left, right):
            if DP[left][right] > DP[left][m] + DP[m + 1][right]:
                DP[left][right] = DP[left][m] + DP[m + 1][right]
                Prev[left][right] = m - left + 1

        for pr in range(1, l):
            lpr = l // pr
            len_cur = 1 if lpr < 10 else 2 if lpr < 100 else 3 if lpr < 1000 else 4
            if l % pr == 0 and LCP[left][left + pr] >= l - pr:
                if DP[left][right] > 2 + len_cur + DP[left][left + pr - 1]:
                    DP[left][right] = 2 + len_cur + DP[left][left + pr - 1]
                    Prev[left][right] = -pr

print(expand(0, length - 1, ""))
