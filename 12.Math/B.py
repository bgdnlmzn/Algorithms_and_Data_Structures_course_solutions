def prime_fac(n):
    fac = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor in fac:
                fac[divisor] += 1
            else:
                fac[divisor] = 1
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                fac[n] = 1
            break
    return fac

def formatic(factors):
    return '*'.join([f"{factor}^{exp}" if exp > 1 else f"{factor}" for factor, exp in sorted(factors.items())])

n = int(input())
factors = prime_fac(n)
result = formatic(factors)
print(result)
