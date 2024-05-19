def generate_rank(nums):
    n = len(nums)
    temp = nums.copy()
    temp.sort()
    rank = {}
    max_rank = 0
    for i in range(n):
        if temp[i] not in rank:
            rank[temp[i]] = max_rank
            max_rank += 1
    for i in range(n):
        nums[i] = rank[nums[i]]
    return max_rank


def select_best(left, right):
    max_len_left, ways_left = left
    max_len_right, ways_right = right
    if max_len_left > max_len_right:
        result = (max_len_left, ways_left)
    elif max_len_left < max_len_right:
        result = (max_len_right, ways_right)
    else:
        result = (max_len_left, ways_left + ways_right)
    return result


def update_tree(start, end, parent, element, max_length, ways, tree):
    if start == end:
        if tree[parent][0] == max_length:
            tree[parent] = (max_length, tree[parent][1] + ways)
        else:
            tree[parent] = (max_length, ways)
        return
    mid = (start + end) // 2
    if element <= mid:
        update_tree(start, mid, 2 * parent + 1, element, max_length, ways, tree)
    else:
        update_tree(mid + 1, end, 2 * parent + 2, element, max_length, ways, tree)
    tree[parent] = select_best(tree[2 * parent + 1], tree[2 * parent + 2])


def query_max_length(start, end, qstart, qend, parent, tree):
    if start > qend or end < qstart:
        return (0, 0)
    if start >= qstart and end <= qend:
        return tree[parent]
    mid = (start + end) // 2
    left = query_max_length(start, mid, qstart, qend, 2 * parent + 1, tree)
    right = query_max_length(mid + 1, end, qstart, qend, 2 * parent + 2, tree)
    return select_best(left, right)


def count_lis(nums):
    n = len(nums)
    max_rank = generate_rank(nums)
    tree = [(0, 0)] * (4 * max_rank + 5)
    for i in range(n):
        max_length = 1
        ways = 1
        if nums[i] > 0:
            info = query_max_length(0, max_rank, 0, nums[i] - 1, 0, tree)
            if info[0] + 1 > max_length:
                max_length = info[0] + 1
                ways = info[1]
        update_tree(0, max_rank, 0, nums[i], max_length, ways, tree)
    return tree[0][1]


n = int(input())
arr = list(map(int, input().split()))
MOD = 10**9 + 7
print(count_lis(arr) % MOD)