import sys
string = str(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
ans = []
m = 10 ** 9 + 7
k = 31
def stringHash(S):
    global m, k
    hash_list= [0]*(len(S)+1)
    k_powers = [1]*(len(S)+1)
    for i in range(len(S)):
        hash_list[i+1]=(hash_list[i]*k + ord(S[i]))%m
        k_powers[i+1] = (k_powers[i]*k)%m
    return hash_list,k_powers

hash_list,k_powers = stringHash(string)
for _ in range(n):
    a,b,c,d = map(int,sys.stdin.readline().strip().split())
    first = (hash_list[b] - hash_list[a - 1] * k_powers[b - a + 1])%m
    sec = (hash_list[d] - hash_list[c - 1] * k_powers[d - c + 1])%m
    if first==sec:
        ans.append('Yes')
    else:
        ans.append('No')
for i in ans:
    sys.stdout.write(str(i)+'\n')