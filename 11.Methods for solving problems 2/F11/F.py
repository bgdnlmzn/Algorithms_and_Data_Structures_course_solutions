def counts(a, m, n, cnt, coins):
    if n == 0:
        return cnt, coins
    if n < 0:
        return -1, []
    if m == 0:
        return -1, []
    c2, coins2 = counts(a[1:], m-1, n-2*a[0], cnt + 2, coins + [a[0], a[0]])
    c1, coins1 = counts(a[1:], m-1, n-a[0], cnt + 1, coins + [a[0]])
    c0, coins0 = counts(a[1:], m-1, n, cnt, coins)
    b = []
    if c2 >= 0:
        b.append((c2, coins2))
    if c1 >= 0:
        b.append((c1, coins1))
    if c0 >= 0:
        b.append((c0, coins0))
    if b:
        return min(b, key=lambda x: x[0])
    return -1, []

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
sum_a = sum(2*x for x in a)
if sum_a < n:
    print(-1)
else:
    c, coins_used = counts(a, m, n, 0, [])
    if c < 0:
        print(0)
    else:
        print(c)
        for coin in coins_used:
            print(coin, end=' ')




