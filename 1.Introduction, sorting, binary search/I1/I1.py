n = int(input())
changes = list(map(int,input().split()))
zero_list = [0]*n
index = n
answer = [0]*n
changes_i = 0
for i in range(n):
    j = changes[changes_i]
    zero_list[j-1] = 1
    if index - j == 0:
        while index>0 and zero_list[index-1] == 1:
            index -= 1
    answer[i] = i+1 - n+index + 1
    changes_i += 1
print('1', end=' ')
for i in answer:
    print(i, end=' ')