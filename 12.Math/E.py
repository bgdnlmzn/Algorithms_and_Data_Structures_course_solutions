MOD = 10**9 + 7
def modinv(a, p):
    return pow(a, p-2, p)

def binomial(n, k, mod):
    if k > n:
        return 0
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i-1] * i % mod
    
    inv_fact = [1] * (n + 1)
    inv_fact[n] = modinv(fact[n], mod)
    for i in range(n-1, 0, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % mod
    
    return fact[n] * inv_fact[k] % mod * inv_fact[n-k] % mod

n, k = map(int, input().split())

result = binomial(n, k, MOD)
print(result)
