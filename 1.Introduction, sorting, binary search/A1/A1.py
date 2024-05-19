n, k = map(int, input().split())
input_list = [int(elem) for elem in input().split()]
key_list = [int(elem) for elem in input().split()]

def binary_search(some_list, item):
    low = 0
    high = len(some_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = some_list[mid]
        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False

for i in range(k):
    if binary_search(input_list, key_list[i]):
        print('YES')
    else:
        print('NO')