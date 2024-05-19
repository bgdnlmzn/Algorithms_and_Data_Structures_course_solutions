import sys
n, c = map(int,sys.stdin.readline().strip().split())
tasks = []
for i in range(n):
    s, t = map(int,sys.stdin.readline().strip().split())
    tasks.append([s + t, s, i + 1])
tasks.sort()
result = [tasks[0]]
for i in range(1, len(tasks)):
    if tasks[i][1] >= result[-1][0]:
        result.append(tasks[i])

sys.stdout.write(str(len(result)*c)+'\n')
sys.stdout.write(str(len(result))+'\n')
for i in result:
    sys.stdout.write(str(i[-1])+' ')