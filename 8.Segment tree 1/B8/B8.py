class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.unique_values = {v: i for i, v in enumerate(sorted(set(arr)))}
        self.tree = [(0, 0)] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = (arr[tl], 1)
        else:
            tm = (tl + tr) // 2
            self.build(arr, v * 2, tl, tm)
            self.build(arr, v * 2 + 1, tm + 1, tr)
            self.tree[v] = self.merge(self.tree[v * 2], self.tree[v * 2 + 1])

    def merge(self, left, right):
        if left[0] < right[0]:
            return left
        elif left[0] > right[0]:
            return right
        else:
            return left[0], left[1] + right[1]

    def query(self, v, tl, tr, l, r):
        if l > r:
            return float('inf'), 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return self.merge(self.query(v * 2, tl, tm, l, min(r, tm)),
                          self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r))

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = (new_val, 1)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2, tl, tm, pos, new_val)
            else:
                self.update(v * 2 + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = self.merge(self.tree[v * 2], self.tree[v * 2 + 1])

n, m = map(int, input().split())
arr = list(map(int, input().split()))

tree = SegmentTree(arr)

for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        tree.update(1, 0, n - 1, op[1], op[2])
    elif op[0] == 2:
        result = tree.query(1, 0, n - 1, op[1], op[2] - 1)
        print(result[0], result[1])