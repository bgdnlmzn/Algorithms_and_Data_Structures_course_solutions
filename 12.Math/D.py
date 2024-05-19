def find_nonzero_n(n):
    if n == 0 or n == 1:
        return 1
    def to_base_5(n):
        digits = []
        while n > 0:
            digits.append(n % 5)
            n //= 5
        return digits[::-1]  

    base_5_digits = to_base_5(n)

    idx_sum = 0
    l = len(base_5_digits)
    for i in range(l):
        digit = base_5_digits[i]
        pos = l - 1 - i
        idx_sum += digit * pos

    even_sum = 0
    for digit in base_5_digits:
        if digit % 2 == 0:
            even_sum += digit

    half_even_sum = even_sum // 2
    total_sum = idx_sum + half_even_sum
    mod_4 = total_sum % 4
    last_digit = 2 ** mod_4

    if last_digit == 1:
        last_digit = 6
    return last_digit

n = int(input())
print(find_nonzero_n(n))
