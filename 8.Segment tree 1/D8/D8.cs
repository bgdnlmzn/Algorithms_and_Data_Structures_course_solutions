using System;
using System.Collections.Generic;

public class SegmentTree
{
    private int n;
    private List<int> a;
    private int neut;
    private List<int> stree;

    public SegmentTree(List<int> a)
    {
        this.n = a.Count;
        this.a = a;
        this.neut = -2000000000;
        this.stree = new List<int>();
        for (int i = 0; i < 4 * n; i++)
        {
            this.stree.Add(this.neut);
        }
        Build(1, 0, n - 1);
    }

    private void Build(int node, int l, int r)
    {
        if (l == r)
        {
            stree[node] = a[l];
        }
        else
        {
            int mid = (l + r) / 2;
            Build(2 * node, l, mid);
            Build(2 * node + 1, mid + 1, r);
            stree[node] = Func(stree[2 * node], stree[2 * node + 1]);
        }
    }

    public int Query(int j, int k)
    {
        return Q(1, 0, n - 1, j, n - 1, k);
    }

    public void Update(int i, int x)
    {
        UpdateHelper(1, 0, n - 1, i, x);
    }

    private int Q(int node, int tl, int tr, int l, int r, int x)
    {
        if (l > r)
        {
            return 2000000000;
        }
        if (tl == tr)
        {
            return (stree[node] >= x) ? tl : 2000000000;
        }
        int tm = (tl + tr) / 2;
        if (tl < l)
        {
            return Math.Min(Q(2 * node, tl, tm, l, Math.Min(r, tm), x), Q(2 * node + 1, tm + 1, tr, Math.Max(l, tm + 1), r, x));
        }
        if (stree[2 * node] >= x)
        {
            return Q(2 * node, tl, tm, l, Math.Min(r, tm), x);
        }
        else
        {
            return Q(2 * node + 1, tm + 1, tr, Math.Max(l, tm + 1), r, x);
        }
    }

    private void UpdateHelper(int node, int l, int r, int i, int x)
    {
        if (l == r)
        {
            a[i] = x;
            stree[node] = x;
        }
        else
        {
            int mid = (l + r) / 2;
            if (l <= i && i <= mid)
            {
                UpdateHelper(2 * node, l, mid, i, x);
            }
            else
            {
                UpdateHelper(2 * node + 1, mid + 1, r, i, x);
            }
            stree[node] = Func(stree[2 * node], stree[2 * node + 1]);
        }
    }

    private int Func(int a, int b)
    {
        return Math.Max(a, b);
    }
}

class Program
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();

        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);
        List<int> a = new List<int>();
        string[] numbers = Console.ReadLine().Split();
        foreach (var num in numbers)
        {
            a.Add(int.Parse(num));
        }
        SegmentTree tree = new SegmentTree(a);
        List<int> res = new List<int>();
        
        for (int i = 0; i < m; i++)
        {
            string[] opArgs = Console.ReadLine().Split();
            int op = int.Parse(opArgs[0]);
            List<int> arg = new List<int>();
            for (int j = 1; j < opArgs.Length; j++)
            {
                arg.Add(int.Parse(opArgs[j]));
            }
            if (op == 1)
            {
                int l = arg[0];
                int v = arg[1];
                tree.Update(l, v);
            }
            else
            {
                int x = arg[0];
                int l = arg[1];
                int result = tree.Query(l, x);
                res.Add((result != 2000000000) ? result : -1);
            }
        }
        foreach (var r in res)
        {
            Console.WriteLine(r);
        }
    }
}

