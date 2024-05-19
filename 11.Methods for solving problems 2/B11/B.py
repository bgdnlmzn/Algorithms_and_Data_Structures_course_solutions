from math import log2

def construct_tree(adjacency_list, edge_values):
    number_of_nodes = len(adjacency_list)
    log_n = int(log2(number_of_nodes)) + 1

    depths = [-1] * number_of_nodes
    ancestors = [[-1] * log_n for _ in range(number_of_nodes)]
    min_edge_values = [[float('inf')] * log_n for _ in range(number_of_nodes)]

    stack = [(0, 0, 0)] 

    while stack:
        node, depth, weight = stack.pop()
        depths[node] = depth
        min_edge_values[node][0] = weight

        for neighbor, edge_value in adjacency_list[node]:
            if depths[neighbor] == -1:
                stack.append((neighbor, depth + 1, edge_value))
                ancestors[neighbor][0] = node

    for j in range(1, log_n):
        for i in range(number_of_nodes):
            if ancestors[i][j - 1] != -1:
                ancestors[i][j] = ancestors[ancestors[i][j - 1]][j - 1]
                min_edge_values[i][j] = min(min_edge_values[i][j - 1], min_edge_values[ancestors[i][j - 1]][j - 1])

    return depths, ancestors, min_edge_values


def lowest_common_ancestor(u, v, depths, ancestors):
    if depths[u] < depths[v]:
        u, v = v, u
    log_n = len(ancestors[0])
    for i in range(log_n - 1, -1, -1):
        if depths[u] - (1 << i) >= depths[v]:
            u = ancestors[u][i]
    if u == v:
        return u
    for i in range(log_n - 1, -1, -1):
        if ancestors[u][i] != -1 and ancestors[u][i] != ancestors[v][i]:
            u, v = ancestors[u][i], ancestors[v][i]
    return ancestors[u][0]


def query_minimum_distance(u, v, depths, ancestors, min_edge_values):
    lca_node = lowest_common_ancestor(u, v, depths, ancestors)
    min_distance = float('inf')

    log_n = len(ancestors[0])

    for i in range(log_n - 1, -1, -1):
        if depths[u] - (1 << i) >= depths[lca_node]:
            min_distance = min(min_distance, min_edge_values[u][i])
            u = ancestors[u][i]
        if depths[v] - (1 << i) >= depths[lca_node]:
            min_distance = min(min_distance, min_edge_values[v][i])
            v = ancestors[v][i]

    return min_distance


num_nodes = int(input())
adjacency_list = [[] for _ in range(num_nodes)]
edge_values = [0] * (num_nodes - 1)
for i in range(num_nodes - 1):
    x, y = map(int, input().split())
    adjacency_list[x].append((i + 1, y))  
    edge_values[i] = y
    
depths, ancestors, min_edge_values = construct_tree(adjacency_list, edge_values)
num_queries = int(input())
for _ in range(num_queries):
    x, y = map(int, input().split())
    print(query_minimum_distance(x, y, depths, ancestors, min_edge_values))
