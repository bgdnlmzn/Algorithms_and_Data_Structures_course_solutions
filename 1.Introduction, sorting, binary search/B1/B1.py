n, k = map(int, input().split())
input_list = [int(elem) for elem in input().split()]
key_list = [int(elem) for elem in input().split()]


def binary_search(some_list, item):
    if item > some_list[-1]:
        return some_list[-1]
    elif item < some_list[0]:
        return some_list[0]
    else:
        low = 0
        high = len(some_list) - 1
        while low <= high:
            ans = 0
            mid = (low + high) // 2
            guess = some_list[mid]
            if guess == item:
                return guess
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1

    if abs(item - some_list[high]) <= abs(item - some_list[low]):
        return some_list[high]
    else:
        return some_list[low]


for i in range(k):
    print(binary_search(input_list, key_list[i]))