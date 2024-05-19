import sys
s = sys.stdin.readline().strip()
stack = []
for i in s.split(' '):
    if i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    else:
        stack.append(int(i))

sys.stdout.write(str(stack.pop()) + "\n")