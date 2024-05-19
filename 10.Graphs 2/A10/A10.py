class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.min_element = list(range(n))
        self.max_element = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.min_element[root_x] = min(self.min_element[root_x], self.min_element[root_y])
            self.max_element[root_x] = max(self.max_element[root_x], self.max_element[root_y])
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def get_info(self, x):
        root = self.find(x)
        return self.min_element[root], self.max_element[root], self.size[root]


n, m = map(int, input().split())
dsu = DisjointSet(n)

for _ in range(m):
    operation = input().split()
    if operation[0] == "union":
        x, y = map(int, operation[1:])
        dsu.union(x - 1, y - 1)
    elif operation[0] == "get":
        x = int(operation[1]) - 1
        min_element, max_element, size = dsu.get_info(x)
        print(min_element + 1, max_element + 1, size)