#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Window {
    int y, x1, x2, id;
    bool isOpen;

    Window(int y = 0, int x1 = 0, int x2 = 0, int id = 0, bool isOpen = false) {
        this->id = id;
        this->isOpen = isOpen;
        this->x2 = x2;
        this->x1 = x1;
        this->y = y;
    }
};

struct SegmentTreeNode {
    int maxValue, position, pendingUpdate;

    SegmentTreeNode(int maxValue = 0, int position = -1, int pendingUpdate = 0) {
        this->maxValue = maxValue;
        this->position = position;
        this->pendingUpdate = pendingUpdate;
    }

    SegmentTreeNode combine(const SegmentTreeNode& other) const {
        return SegmentTreeNode(max(maxValue, other.maxValue),
            (maxValue > other.maxValue ? position : other.position));
    }
};

int treeSize = 1;

pair<int, pair<int, int> > maxPair(pair<int, pair<int, int> > x, pair<int, pair<int, int> > y) {
    if (x.first > y.first) {
        return x;
    }
    return y;
}

void propagateUpdate(vector<SegmentTreeNode>& tree, int node) {
    tree[node].maxValue += tree[node].pendingUpdate;
    if (node < treeSize) {
        tree[2 * node].pendingUpdate += tree[node].pendingUpdate;
        tree[2 * node + 1].pendingUpdate += tree[node].pendingUpdate;
    }
    tree[node].pendingUpdate = 0;
}

void rangeAdd(vector<SegmentTreeNode>& tree, int node, int left, int right, int queryLeft, int queryRight, bool value) {
    propagateUpdate(tree, node);
    if (right < queryLeft || left > queryRight)
        return;
    if (left >= queryLeft && right <= queryRight) {
        tree[node].pendingUpdate += value ? -1 : 1;
        propagateUpdate(tree, node);
    }
    else {
        int mid = (left + right) / 2;
        rangeAdd(tree, 2 * node, left, mid, queryLeft, min(queryRight, mid), value);
        rangeAdd(tree, 2 * node + 1, mid + 1, right, max(queryLeft, mid + 1), queryRight, value);
        tree[node] = tree[2 * node].combine(tree[2 * node + 1]);
    }
}

bool compareWindows(const Window& a, const Window& b) {
    return (a.y == b.y && !a.isOpen && b.isOpen) || a.y < b.y;
}

int main() {
    int size = 1e6, halfSize = size / 2;
    while (treeSize <= size) treeSize <<= 1;
    vector<SegmentTreeNode> segmentTree(4 * size);
    for (int i = treeSize; i < segmentTree.size(); ++i) {
        segmentTree[i].position = i - treeSize + 1;
    }
    for (int i = treeSize - 1; i >= 1; --i)
        segmentTree[i] = segmentTree[i * 2].combine(segmentTree[i * 2 + 1]);

    int numberOfWindows;
    cin >> numberOfWindows;
    vector<Window> windows(halfSize / 2 + 10);
    int leftX, bottomY, rightX, topY;
    for (int i = 0; i < 2 * numberOfWindows; i += 2) {
        cin >> leftX >> bottomY >> rightX >> topY;
        leftX += halfSize, bottomY += halfSize, rightX += halfSize, topY += halfSize;
        windows[i] = Window(topY, leftX, rightX, i, true);
        windows[i + 1] = Window(bottomY, leftX, rightX, i, false);
    }
    sort(windows.begin(), windows.begin() + 2 * numberOfWindows, compareWindows);
    int result = -1, xPos, yPos;
    for (int i = 0; i < 2 * numberOfWindows; ++i) {
        rangeAdd(segmentTree, 1, 1, treeSize, windows[i].x1, windows[i].x2, windows[i].isOpen);
        if (segmentTree[1].maxValue > result) {
            result = segmentTree[1].maxValue;
            xPos = segmentTree[1].position - halfSize;
            yPos = windows[i].y - halfSize;
        }
    }
    cout << result << endl;
    cout << xPos << ' ' << yPos << endl;
    return 0;
}

