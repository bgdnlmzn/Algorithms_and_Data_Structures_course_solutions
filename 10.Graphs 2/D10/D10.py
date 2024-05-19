size = int(input())
values_a = [0] * (size + 2)
values_d = [0] * (size + 2)
left = [0] * (size + 2)
right = [0] * (size + 2)
values_a[1:size + 1] = map(int, input().split())
values_d[1:size + 1] = map(int, input().split())
left[1:size + 1] = range(size)
right[1:size + 1] = range(2, size + 2)
current = set(range(1, size + 1))
for _ in range(size):
    dead_set = set()
    for index in current:
        if 1 <= index <= size and values_a[left[index]] + values_a[right[index]] > values_d[index]:
            dead_set.add(index)
    current.clear()
    for index in dead_set:
        current.add(left[index])
        current.add(right[index])
        left[right[index]] = left[index]
        right[left[index]] = right[index]
    current -= dead_set
    print(len(dead_set), end=' ')
print()