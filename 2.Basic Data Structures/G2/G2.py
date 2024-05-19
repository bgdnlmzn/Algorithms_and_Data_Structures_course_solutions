import sys, collections
q_r = collections.deque()
q_l= collections.deque()
n = int(sys.stdin.readline().strip())
res=[]
for _ in range(n):
    line = list(map(str,sys.stdin.readline().strip().split()))
    if line[0]=='+':
        x = int(line[1])
        q_r.append(x)
    elif line[0]=='*':
        x = int(line[1])
        q_l.append(x)
    else:
        res.append(str(q_l.popleft()))
    while len(q_l)<(len(q_r)+len(q_l)+1)//2:
        q_l.append(q_r.popleft())
    while len(q_l)>(len(q_r)+len(q_l)+1)//2:
        q_r.appendleft(q_l.pop())
    #print('pravin',q_r)
    #print('levin',q_l)
sys.stdout.write('\n'.join(res))