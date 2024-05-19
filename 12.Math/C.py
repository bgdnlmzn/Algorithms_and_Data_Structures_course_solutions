def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(max_num + 1) if is_prime[p]]

def find_pair(n):
    primes = sieve(n)
    prime_set = set(primes)
    for p in primes:
        q = n - p
        if q in prime_set:
            return p, q

n = int(input())
p, q = find_pair(n)
print(p, q)
