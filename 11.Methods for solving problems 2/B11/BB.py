from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.parent = None
        self.weights = defaultdict(int)

def build_tree(n, edges):
    tree = TreeNode()
    for i in range(1, n):
        x, y, cost = map(int, edges[i - 1].split())
        tree.children[x].parent = tree
        tree.children[x].weights[i + 1] = cost
    return tree

def dfs(tree, node, parent):
    for child, child_node in tree.children[node].children.items():
        if child != parent:
            for parent_weight, parent_weight_val in tree.weights[node].items():
                child_node.weights[parent_weight] = min(parent_weight_val, tree.children[node].weights[child])
            dfs(tree, child, node)

def find_min_between(tree, u, v):
    min_weight = float('inf')
    while u != v:
        if len(tree.weights[u]) > len(tree.weights[v]):
            min_weight = min(min_weight, tree.weights[u][v])
            u = tree.children[u].parent
        else:
            min_weight = min(min_weight, tree.weights[v][u])
            v = tree.children[v].parent
    return min_weight

# Ввод числа вершин
n = int(input())

# Ввод ребер и их стоимостей
edges = [input() for _ in range(n - 1)]

# Построение дерева
tree = build_tree(n, edges)

# Вычисление минимальных стоимостей на пути от корня до каждой вершины
dfs(tree, 1, None)

# Ввод числа запросов
m = int(input())

# Обработка запросов и вывод результатов
for _ in range(m):
    x, y = map(int, input().split())
    print(find_min_between(tree, x, y))



