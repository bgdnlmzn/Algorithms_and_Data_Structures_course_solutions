#include <bits/stdc++.h>
using namespace std;

vector<int> zFunction(const string &S) {
    int n = S.size();
    vector<int> res(n);
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i > r) {
            int x = 0;
            while (x + i < n && S[x] == S[x + i]) {
                x++;
            }
            res[i] = x;
            if (x > 0) {
                l = i;
                r = i + x - 1;
            }
        } else {
            if (res[i - l] < r - i + 1) {
                res[i] = res[i - l];
            } else {
                int x = r - i + 1;
                while (x + i < n && S[x + i] == S[x]) {
                    x++;
                }
                l = i;
                r = i + x - 1;
                res[i] = x;
            }
        }
    }
    return res;
}

int findOccurrences(const string &s, const string &t) {
    string concat = t + "$" + s;
    vector<int> zf = zFunction(concat);
    int res = 0;
    int t_len = t.size();
    for (int i = t_len + 1; i < concat.size(); ++i) {
        if (zf[i] == t_len) {
            res++;
        }
    }
    return res;
}

int main() {
    string a, b;
    getline(cin, a);
    getline(cin, b);

    int count = 0;
    int a_len = a.size();
    int b_len = b.size();

    for (int i = 0; i <= a_len - b_len; ++i) {
        string st = a.substr(i, b_len);
        if (st != b) {
            count += findOccurrences(st + st, b);
        } else {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
