import sys

n = int(sys.stdin.readline().strip())
path1 = list(map(int, sys.stdin.readline().strip().split()))
changer = []
path2 = []
k = 0
first_in_q = min(path1)
res = []
for i in path1:
    changer.append(i)
    k += 1
    if i == first_in_q:
        res.append([1, k])
        first_in_q += 1
        k = 0
        k_changer = 1
        path2.append(changer.pop())

        while len(changer) > 0:
            if changer[-1] == first_in_q:
                first_in_q += 1
                path2.append(changer.pop())
                k_changer += 1
            else:
                break
        res.append([2, k_changer])
if len(changer) > 0:
    sys.stdout.write(str(0) + "\n")
else:
    sys.stdout.write(str(len(res)) + "\n")
    for i in res:
        sys.stdout.write(" ".join(map(str, i)) + "\n")