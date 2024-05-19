def countP(S):
    mod_s = '#' + '#'.join(S) + '#'
    n = len(mod_s)
    pal_lens = [0] * n
    c = r = max_pal_c = max_pal_len = 0
    for i in range(n):
        m = 2 * c - i
        if i < r:
            pal_lens[i] = min(r - i, pal_lens[m])
        while i - pal_lens[i] - 1 >= 0 and i + pal_lens[i] + 1 < n and \
                mod_s[i - pal_lens[i] - 1] == mod_s[i + pal_lens[i] + 1]:
            pal_lens[i] += 1
        if i + pal_lens[i] > r:
            c = i
            r = i + pal_lens[i]
        if pal_lens[i] > max_pal_len:
            max_pal_len = pal_lens[i]
            max_pal_c = i
    cnt = 0
    for l in pal_lens:
        cnt += (l + 1) // 2

    return cnt


S = input()
count = countP(S)
print(count)