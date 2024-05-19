import sys

n = int(sys.stdin.readline().strip())
time = []
k = 0
for _ in range(n):
    h1, m1, s1, h2, m2, s2 = map(int, sys.stdin.readline().strip().split())
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    if start > end:

        time.append((start, 86400))
        time.append((0, end))

    else:
        if start == end:
            k += 1
        else:
            time.append((start, end))
points = []
for i in time:
    points.append((i[0], 's'))
    points.append((i[1], 'e'))
points.sort()
res = 0
s = 1000000
e = -1000000
Fl = False

for point, flag in points:
    if flag == 's':
        k += 1
    else:
        k -= 1
    if k == n:
        s = min(point, s)
        Fl = True
    else:
        if Fl:
            e = point
            res += e - s
            s = 1000000
            e = 1000000
            Fl = False
        else:
            continue

sys.stdout.write(str(res))