using System;
using System.Collections.Generic;

class Node
{
    public long Summ { get; set; }
    public long Add { get; set; }
    public int Replace { get; set; }

    public Node()
    {
        Summ = Add = 0;
        Replace = -1;
    }
}

class Program
{
    static void PushTree(List<Node> tree, int v, int treeSize)
    {
        if (tree[v].Replace != -1)
        {
            if (treeSize != 1)
            {
                tree[v * 2].Replace = tree[v * 2 + 1].Replace = tree[v].Replace;
                tree[v * 2].Add = tree[v * 2 + 1].Add = 0;
            }
            tree[v].Summ = (long)tree[v].Replace * treeSize;
        }
        tree[v].Replace = -1;

        if (treeSize != 1)
        {
            tree[v * 2].Add += tree[v].Add;
            tree[v * 2 + 1].Add += tree[v].Add;
        }
        tree[v].Summ += tree[v].Add * treeSize;
        tree[v].Add = 0;
    }

    static long GetSum(List<Node> tree, int v, int tl, int tr, int l, int r)
    {
        PushTree(tree, v, tr - tl + 1);

        if (l > r) return 0;

        if (l == tl && tr == r) return tree[v].Summ;

        int tm = (tl + tr) / 2;
        return GetSum(tree, v * 2, tl, tm, l, Math.Min(r, tm)) + GetSum(tree, v * 2 + 1, tm + 1, tr, Math.Max(l, tm + 1), r);
    }

    static void UpdateReplace(List<Node> tree, int v, int tl, int tr, int l, int r, int value)
    {
        PushTree(tree, v, tr - tl + 1);

        if (l > r) return;

        if (l == tl && tr == r)
        {
            tree[v].Replace = value;
            tree[v].Add = 0;
            PushTree(tree, v, tr - tl + 1);
        }
        else
        {
            int tm = (tl + tr) / 2;
            UpdateReplace(tree, v * 2, tl, tm, l, Math.Min(r, tm), value);
            UpdateReplace(tree, v * 2 + 1, tm + 1, tr, Math.Max(l, tm + 1), r, value);
            tree[v].Summ = tree[v * 2].Summ + tree[v * 2 + 1].Summ;
        }
    }

    static void UpdateAdd(List<Node> tree, int v, int tl, int tr, int l, int r, int value)
    {
        PushTree(tree, v, tr - tl + 1);

        if (l > r) return;

        if (l == tl && tr == r)
        {
            tree[v].Add += value;
            PushTree(tree, v, tr - tl + 1);
        }
        else
        {
            int tm = (tl + tr) / 2;
            UpdateAdd(tree, v * 2, tl, tm, l, Math.Min(r, tm), value);
            UpdateAdd(tree, v * 2 + 1, tm + 1, tr, Math.Max(l, tm + 1), r, value);
            tree[v].Summ = tree[v * 2].Summ + tree[v * 2 + 1].Summ;
        }
    }

    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        List<Node> tree = new List<Node>(n * 4);
        for (int i = 0; i < n * 4; i++)
        {
            tree.Add(new Node());
        }

        for (int req = 0; req < m; req++)
        {
            string[] Type = Console.ReadLine().Split();
            if (Type[0] == "1")
            {
                int l = int.Parse(Type[1]);
                int r = int.Parse(Type[2]);
                int v = int.Parse(Type[3]);
                UpdateReplace(tree, 1, 0, n - 1, l, r - 1, v);
            }
            else if (Type[0] == "2")
            {
                int l = int.Parse(Type[1]);
                int r = int.Parse(Type[2]);
                int v = int.Parse(Type[3]);
                UpdateAdd(tree, 1, 0, n - 1, l, r - 1, v);
            }
            else
            {
                int l = int.Parse(Type[1]);
                int r = int.Parse(Type[2]);
                Console.WriteLine(GetSum(tree, 1, 0, n - 1, l, r - 1));
            }
        }
    }
}