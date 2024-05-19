import sys
n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().strip().split()))
stack = [(-1,0)]
k = 0
for i in a:
    if stack[-1][0]==i:
        stack.append((i,stack[-1][1]+1))
    else:
        if stack[-1][1]>=3:
            while stack[-1][0] == stack[-2][0]:
                stack.pop()
                k+=1
            stack.pop()
            k+=1
        if stack[-1][0] == i:
            stack.append((i,stack[-1][1]+1))
        else:
            stack.append((i,1))
if stack[-1][1] >=3:
    while stack[-1][0] == stack[-2][0]:
        stack.pop()
        k += 1
    stack.pop()
    k += 1
sys.stdout.write(str(k) + "\n")