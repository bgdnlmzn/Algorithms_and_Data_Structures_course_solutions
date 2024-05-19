import sys
n = int(sys.stdin.readline().strip())
array = list(map(int,sys.stdin.readline().strip().split()))
q = int(sys.stdin.readline().strip())
prefix_sum = [0]
prefix_xor = [0]
def xor(a,b):
    return a^b
for i in range(len(array)):
    prefix_sum.append(prefix_sum[-1]+array[i])
    prefix_xor.append(xor(prefix_xor[-1],array[i]))
answer = []
for _ in range(q):
    some_q = array = list(map(int,sys.stdin.readline().strip().split()))
    l = some_q[1]
    r = some_q[2]
    if some_q[0]==1:
        answer.append(str(prefix_sum[r]-prefix_sum[l-1]))
    else:
        answer.append(str(prefix_xor[r]^prefix_xor[l-1]))
sys.stdout.write('\n'.join(answer))