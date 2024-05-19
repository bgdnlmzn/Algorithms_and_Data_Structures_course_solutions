#include <cstdio>
#include <vector>
#include <cassert>
#include <functional>
#include <iostream>

int main() {
    int sizeI, sizeJ;
    std::cin >> sizeI >> sizeJ; // Чтение размеров sizeI и sizeJ из стандартного ввода
    std::function<int(int, int)> encode = [&](int i, int j) {
        return i * (sizeJ + 1) + j;
    };
    std::vector<int> parent(1 + encode(sizeI + 1, sizeJ + 1), -1);
    std::function<int(int)> getRoot = [&](int v) {
        if (parent[v] < 0) {
            return v;
        } else {
            int root = getRoot(parent[v]);
            parent[v] = root;
            return root;
        }
    };
    std::function<bool(int, int)> join = [&](int a, int b) {
        a = getRoot(a);
        b = getRoot(b);
        if (a == b) {
            return false;
        }
        assert(parent[a] < 0);
        assert(parent[b] < 0);
        if (parent[a] < parent[b]) {
            parent[a] += parent[b];
            parent[b] = a;
        } else {
            parent[b] += parent[a];
            parent[a] = b;
        }
        return true;
    };

    for (int i = 1; i <= sizeI; i++) {
        for (int j = 1; j <= sizeJ; j++) {
            int code;
            std::cin >> code; // Чтение кода из стандартного ввода
            if ((code & 1) != 0) {
                join(encode(i, j), encode(i + 1, j));
            }
            if ((code & 2) != 0) {
                join(encode(i, j), encode(i, j + 1));
            }
        }
    }
    std::vector<int> ansI;
    std::vector<int> ansJ;
    std::vector<int> ansD;
    int ansCost = 0;
    for (int i = 1; i < sizeI; i++) {
        for (int j = 1; j <= sizeJ; j++) {
            if (join(encode(i, j), encode(i + 1, j))) {
                ansI.push_back(i);
                ansJ.push_back(j);
                ansD.push_back(1);
                ansCost += 1;
            }
        }
    }
    for (int i = 1; i <= sizeI; i++) {
        for (int j = 1; j < sizeJ; j++) {
            if (join(encode(i, j), encode(i, j + 1))) {
                ansI.push_back(i);
                ansJ.push_back(j);
                ansD.push_back(2);
                ansCost += 2;
            }
        }
    }
    printf("%d %d\n", (int)ansI.size(), ansCost);
    for (int i = 0; i < (int)ansI.size(); i++) {
        printf("%d %d %d\n", ansI[i], ansJ[i], ansD[i]);
    }
    return 0;
}
