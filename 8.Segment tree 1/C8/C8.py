class SegmentTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [0] * (4 * self.size)
        self.build_tree(arr, 0, self.size - 1, 0)

    def build_tree(self, arr, start, end, index):
        if start == end:
            self.tree[index] = arr[start]
            return

        mid = (start + end) // 2
        self.build_tree(arr, start, mid, 2 * index + 1)
        self.build_tree(arr, mid + 1, end, 2 * index + 2)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def update(self, idx):
        self._update(0, self.size - 1, idx, 0)

    def _update(self, start, end, idx, tree_index):
        if start == end:
            self.tree[tree_index] = 1 - self.tree[tree_index]
            return

        mid = (start + end) // 2
        if start <= idx <= mid:
            self._update(start, mid, idx, 2 * tree_index + 1)
        else:
            self._update(mid + 1, end, idx, 2 * tree_index + 2)

        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def k(self, k):
        return self._k(0, self.size - 1, k, 0)

    def _k(self, start, end, k, tree_index):
        if start == end:
            return start

        mid = (start + end) // 2
        left_count = self.tree[2 * tree_index + 1]
        if k < left_count:
            return self._k(start, mid, k, 2 * tree_index + 1)
        else:
            return self._k(mid + 1, end, k - left_count, 2 * tree_index + 2)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = SegmentTree(arr)
for _ in range(m):
    op, arg = map(int, input().split())
    if op == 1:
        tree.update(arg)
    else:
        print(tree.k(arg))
