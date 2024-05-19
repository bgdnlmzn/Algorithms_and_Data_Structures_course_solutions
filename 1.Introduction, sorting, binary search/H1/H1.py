n = int(input())
string = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
linked_list = [0] * len(alphabet)
for i in range(len(string)):
    linked_list[ord(string[i]) - 65] += 1

potential_mid = ''
potential_side = ''
for i in range(len(linked_list)):
    if linked_list[i] > 1 and linked_list[i] % 2 == 0:
        potential_side += chr(65 + i) * linked_list[i]
    else:
        if linked_list[i] != 0:
            potential_side += chr(65 + i) * (linked_list[i] - 1)
            potential_mid += chr(65 + i)

potential_mid = sorted(potential_mid, key=lambda x: x.lower())
potential_side = sorted(potential_side, key=lambda x: x.lower())

mid = ''
side = ''
k = 0
mid_char = ''
answer = ''
for i in range(0, len(potential_side), 2):
    side += potential_side[i]
if potential_mid != []:
    for i in range(len(potential_mid)):
        if potential_mid.count(potential_mid[i]) > k:
            k = potential_mid.count(potential_mid[i])
            mid_char = potential_mid[i]
if potential_mid == []:
    answer = side + side[::-1]
else:
    answer = side + mid_char * k + side[::-1]

print(answer)