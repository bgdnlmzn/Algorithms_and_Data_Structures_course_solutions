#include <iostream>
#include <vector>
using namespace std;
struct TreeNode
{
    int length, count, left, right;
    bool updated, color;
    TreeNode() {}
    TreeNode(int l, int r) {
        this->left = l;
        this->right = r;
        length = count = 0;
        color = updated = false;
    }
};
void buildTree(vector <TreeNode>& tree, int node, int tl, int tr) {
    tree[node] = TreeNode(tl, tr);
    if (tl != tr) {
        int tm = (tl + tr) / 2;
        buildTree(tree, 2 * node, tl, tm);
        buildTree(tree, 2 * node + 1, tm + 1, tr);
    }
}
void updateTree(vector <TreeNode>& tree, int node) {
    if (!tree[node].updated) return;
    tree[node].length = tree[node].color ? (tree[node].right - tree[node].left + 1) : 0;
    tree[node].count = tree[node].color ? 1 : 0;
    tree[node].updated = false;
    if (tree[node].left != tree[node].right) {
        tree[2 * node].color = tree[2 * node + 1].color = tree[node].color;
        tree[2 * node].updated = tree[2 * node + 1].updated = true;
    }
}
void drawSegment(vector <TreeNode>& tree, int node, bool col, int l, int r) {
    if ((tree[node].right < l) || (r < tree[node].left)) return;
    updateTree(tree, node);
    if ((l <= tree[node].left) && (tree[node].right <= r)) {
        tree[node].color = col;
        tree[node].updated = true;
        return;
    }
    if (tree[node].left == tree[node].right) return;
    drawSegment(tree, 2 * node, col, l, r);
    drawSegment(tree, 2 * node + 1, col, l, r);
    int current = 2 * node;
    while (true) {
        updateTree(tree, current);
        if (tree[current].left == tree[current].right) break;
        current = 2 * current + 1;
    }
    bool left = (tree[current].count == 1);
    current = 2 * node + 1;
    while (true) {
        updateTree(tree, current);
        if (tree[current].left == tree[current].right) break;
        current *= 2;
    }
    bool right = (tree[current].count == 1);
    tree[node].length = tree[2 * node].length + tree[2 * node + 1].length;
    tree[node].count = tree[2 * node].count + tree[2 * node + 1].count;
    if (left && right) --tree[node].count;
}
int main()
{
    vector <TreeNode> segTree(4 * 1000100);
    vector <pair <long long, long long> > result;
    buildTree(segTree, 1, 0, 1000100);
    int n, x, length;
    cin >> n;
    char color;
    for (int i = 0; i < n; ++i) {
        cin >> color >> x >> length;
        length += length > 0 ? -1 : 1;
        drawSegment(segTree, 1, (color == 'B'), x + 500000, x + length + 500000);
        result.push_back(make_pair(segTree[1].count, segTree[1].length));
    }
    for (auto i : result) {
        cout << i.first << ' ' << i.second << endl;
    }
    return 0;
}