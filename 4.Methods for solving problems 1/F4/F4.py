import sys
n = int(sys.stdin.readline().strip())
segment = []
for _ in range(n):
    segment.append(list(map(int,sys.stdin.readline().strip().split())))
current = 0
mas = []
for [l,r] in segment:
    mas.append((l,-1))
    mas.append((r,+1))
mas.sort()
count = 1
sum_len = 0
for i in range(1,len(mas)):
    if count !=0:
        sum_len+= mas[i][0]-mas[i-1][0]
    count-= mas[i][1]
sys.stdout.write(str(sum_len))