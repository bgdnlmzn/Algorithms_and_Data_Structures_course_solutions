def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def mod_inv(a, mod):
    return mod_exp(a, mod - 2, mod)

def calc(n, m, k, mod):
    total_combinations = mod_exp(m, n, mod)
    
    K_mod = k % mod
    
    K_inv = mod_inv(K_mod, mod)

    result = (total_combinations * K_inv) % mod
    
    return result

n, m, k, mod = map(int,input().split())
print(calc(n, m, k, mod))
