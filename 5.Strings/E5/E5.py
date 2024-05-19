import sys
t = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
ans=[]
for i in range(len(s)-len(t)+1):
    k=0
    for j in range(len(t)):
        if s[i+j]!=t[j]:
            k+=1
            if k>1:
                break
    if k <=1:
        ans.append(i+1)
sys.stdout.write(str(len(ans))+'\n')
sys.stdout.write(" ".join(map(str,ans)) + "\n")