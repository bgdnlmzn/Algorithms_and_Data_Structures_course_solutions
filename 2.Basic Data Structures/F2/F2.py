import sys, collections
n = int(sys.stdin.readline().strip())
res = []
queue = collections.deque()
people_ahead= dict()
left =0
front=0


for _ in range(n):
    line = list(map(int,sys.stdin.readline().strip().split()))
    if line[0]==1:
        people_ahead[line[1]] = front
        front+=1
        queue.append(line[1])
    elif line[0]==2:
        left+=1
        queue.popleft()
    elif line[0]==3:
        front-=1
        queue.pop()
    elif line[0]==4:
        res.append(str(abs(people_ahead.get(line[1])-left)))
    else:
        elem = queue.popleft()
        res.append(str(elem))
        queue.appendleft(elem)
sys.stdout.write('\n'.join(res))