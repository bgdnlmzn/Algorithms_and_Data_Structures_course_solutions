import sys
n = int(sys.stdin.readline().strip())
res = []
structure =[]
for _ in range(n):
    line = sys.stdin.readline().strip()

    if line.split()[0]=='1':
        new_elem = int(line.split()[1])
        if not structure:
            structure.append(new_elem)
        else:
            structure.append(min(structure[-1],new_elem))
    elif line.split()[0]=='2':
        structure.pop()
    else:
        res.append(str(structure[-1]))
sys.stdout.write('\n'.join(res))