import sys
string = str(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
def zFunction(S):
    result = len(S) * [0]
    l = -1
    r = -1
    for i in range(1, len(S)):
        if i > r:
            x = 0
            while x + i < len(S) and S[x] == S[x + i]:
                x += 1
            result[i] = x
            if x + i - 1 > r:
                l = i
                r = x + i - 1
        else:
            if result[i - l] + i <= r:
                result[i] = result[i - l]
            else:
                x = min(result[i - l], r - i) # не выйдет просто поставить result[i - l], т.к. он далековат
                while x + i < len(S) and S[x + i] == S[x]:
                    x += 1
                l = i
                r = i + x - 1
                result[i] = x
    return result

def find(S, T):
    concat = T + '$' + S
    zf = zFunction(concat)
    result = []
    c=0
    for i in range(len(T), len(concat)):
        if zf[i] == len(T):
            result.append(i - len(T) - 1)
            c+=1
    return result,c


for _ in range(n):
    substring = str(sys.stdin.readline().strip())
    occ,c = find(string, substring)
    sys.stdout.write(str(c)+' '+' '.join(map(str, occ))+'\n')