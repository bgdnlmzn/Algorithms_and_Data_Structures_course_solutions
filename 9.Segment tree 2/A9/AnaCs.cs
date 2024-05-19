using System;
using System.Collections.Generic;

class Program
{
    static long GetMin(List<(long, long)> tree, int v, int tl, int tr, int l, int r)
    {
        if (l > r) return long.MaxValue;

        long additional = tree[v].Item2;

        if (l == tl && tr == r) return tree[v].Item1 + additional;

        int tm = (tl + tr) / 2;
        return Math.Min(
            GetMin(tree, v * 2, tl, tm, l, Math.Min(r, tm)),
            GetMin(tree, v * 2 + 1, tm + 1, tr, Math.Max(l, tm + 1), r)
        ) + additional;
    }

    static void Update(List<(long, long)> tree, int v, int tl, int tr, int l, int r, int value)
    {
        if (l > r) return;

        if (l == tl && tr == r)
        {
            tree[v] = (tree[v].Item1, tree[v].Item2 + value);
        }
        else
        {
            int tm = (tl + tr) / 2;
            Update(tree, v * 2, tl, tm, l, Math.Min(r, tm), value);
            Update(tree, v * 2 + 1, tm + 1, tr, Math.Max(l, tm + 1), r, value);
            tree[v] = (Math.Min(tree[v * 2].Item1 + tree[v * 2].Item2, tree[v * 2 + 1].Item1 + tree[v * 2 + 1].Item2), tree[v].Item2);
        }
    }

    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        List<(long, long)> tree = new List<(long, long)>(n * 4);
        for (int i = 0; i < n * 4; ++i)
        {
            tree.Add((0, 0));
        }

        for (int req = 0; req < m; ++req)
        {
            string[] request = Console.ReadLine().Split();
            char reqType = request[0][0];
            if (reqType == '1')
            {
                int l = int.Parse(request[1]);
                int r = int.Parse(request[2]);
                int v = int.Parse(request[3]);
                Update(tree, 1, 0, n - 1, l, r - 1, v);
            }
            else
            {
                int l = int.Parse(request[1]);
                int r = int.Parse(request[2]);
                Console.WriteLine(GetMin(tree, 1, 0, n - 1, l, r - 1));
            }
        }
    }
}
