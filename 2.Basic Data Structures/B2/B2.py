import sys

n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
stack1 = []
stack2 = []
res = []


def push(x):
    if len(stack1) > 0:
        stack1.append([x, min(x, stack1[-1][1])])
    else:
        stack1.append([x, x])


def pop():
    if len(stack2) > 0:
        stack2.pop()
    else:
        x = stack1.pop()[0]
        stack2.append([x, x])
        while len(stack1) > 0:
            x = stack1.pop()[0]
            stack2.append([x, min(stack2[-1][1], x)])
        stack2.pop()


def get_result():
    if len(stack1) == 0:
        return stack2[-1][1]
    if len(stack2) == 0:
        return stack1[-1][1]

    return min(stack1[-1][1], stack2[-1][1])


count = 0
for i in a:
    push(i)
    count += 1
    if count == k:
        res.append(get_result())
        pop()
        count = k - 1
sys.stdout.write(" ".join(map(str, res)) + "\n")