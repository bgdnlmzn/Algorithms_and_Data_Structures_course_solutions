import sys
a = str(sys.stdin.readline().strip())
b = str(sys.stdin.readline().strip())
def zFunction(S):
    res = [0] * len(S)
    l = -1
    r = -1
    for i in range(1, len(S)):
        if i > r:
            x = 0
            while x + i < len(S) and S[x] == S[x + i]:
                x += 1
            res[i] = x
            if x + i - 1 > r:
                l = i
                r = x + i - 1
        else:
            if res[i - l] + i < r:
                res[i] = res[i - l]
            else:
                x = min(res[i - l], r - i)
                while x + i < len(S) and S[x + i] == S[x]:
                    x += 1
                l = i
                r = i + x - 1
                res[i] = x
    return res

def find(s, t):
    concat = t + "$" + s
    zf = zFunction(concat)
    res = 0
    for i in range(len(t) + 1, len(concat)):
        if zf[i] == len(t):
            res += 1
    return res


count = 0
for i in range(len(a) - len(b) + 1):
    st = a[i:i + len(b)]
    if st != b:
        count += find(st + st, b)
    else:
        count += 1
sys.stdout.write(str(count))



