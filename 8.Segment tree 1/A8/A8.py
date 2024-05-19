class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build_tree(0, 0, len(arr) - 1)

    def build_tree(self, idx, left, right):
        if left == right:
            self.tree[idx] = self.arr[left]
            return
        mid = (left + right) // 2
        self.build_tree(2 * idx + 1, left, mid)
        self.build_tree(2 * idx + 2, mid + 1, right)
        self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]

    def update(self, idx, left, right, i, val):
        if left == right == i:
            self.tree[idx] = val
            return
        if i < left or i > right:
            return
        mid = (left + right) // 2
        self.update(2 * idx + 1, left, mid, i, val)
        self.update(2 * idx + 2, mid + 1, right, i, val)
        self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]

    def query(self, idx, left, right, qleft, qright):
        if qleft <= left and qright >= right:
            return self.tree[idx]
        if qleft > right or qright < left:
            return 0
        mid = (left + right) // 2
        return self.query(2 * idx + 1, left, mid, qleft, qright) + \
               self.query(2 * idx + 2, mid + 1, right, qleft, qright)

    def range_update(self, idx, left, right, qleft, qright, val):
        if qleft <= left and qright >= right:
            self.tree[idx] += (right - left + 1) * val
            return
        if qleft > right or qright < left:
            return
        mid = (left + right) // 2
        self.range_update(2 * idx + 1, left, mid, qleft, qright, val)
        self.range_update(2 * idx + 2, mid + 1, right, qleft, qright, val)
        self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]

n,m = map(int,input().split())
arr = list(map(int,input().split()))
segment_tree = SegmentTree(arr)
for _ in range(m):
    op = list(map(int,input().split()))
    if op[0]==1:
        segment_tree.update(0, 0, len(arr) - 1, op[1], op[2])
    else:
        print(segment_tree.query(0, 0, len(arr) - 1, op[1], op[2]-1))