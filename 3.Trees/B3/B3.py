n, r = map(int, input().split())
nodes = [tuple(map(int, input().split())) for _ in range(n)]

heights = [-1] * n
is_avl = True

stack = [(r, 0)]

mins = [float('inf')] * n
maxs = [float('-inf')] * n

while stack and is_avl:
    node, state = stack.pop()

    if node == -1:
        continue

    left_child, right_child = nodes[node]

    if state == 0:
        stack.append((node, 1))
        if left_child != -1:
            stack.append((left_child, 0))
    elif state == 1:
        stack.append((node, 2))
        if right_child != -1:
            stack.append((right_child, 0))
    elif state == 2:
        left_height = heights[left_child] if left_child != -1 else 0
        right_height = heights[right_child] if right_child != -1 else 0

        if abs(left_height - right_height) > 1:
            is_avl = False
            break

        heights[node] = max(left_height, right_height) + 1

        left_max = maxs[left_child] if left_child != -1 else float('-inf')
        right_min = mins[right_child] if right_child != -1 else float('inf')

        if (left_child != -1 and left_max >= node) or (right_child != -1 and right_min <= node):
            is_avl = False
            break

        mins[node] = min(node, mins[left_child] if left_child != -1 else node)
        maxs[node] = max(node, maxs[right_child] if right_child != -1 else node)

print(1 if is_avl else 0)

