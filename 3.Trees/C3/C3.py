def build_tree(papa):
    nodes = [[] for _ in range(len(papa))]
    root = None

    for i, parent in enumerate(papa):
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)

    return nodes, root


def lca(nodes, root, u, v):
    if root is None:
        return None

    if root == u or root == v:
        return root

    lca_found = None
    for baby in nodes[root]:
        baby_lca = lca(nodes, baby, u, v)
        if baby_lca is None:
            continue
        if lca_found is not None:
            return root
        lca_found = baby_lca

    return lca_found


answer = []
n = int(input())
papa = list(map(int, input().split()))
papa.insert(0, -1)
nodes, root = build_tree(papa)
q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    lca_node = lca(nodes, root, u, v)
    answer.append(lca_node)
for i in answer:
    print(i, end='\n')