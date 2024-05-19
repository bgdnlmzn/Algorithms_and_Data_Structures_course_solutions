def find_longest_palindrome(input_str):
    n = len(input_str)
    mat = [[-1] * n for _ in range(n)]
    
    def F(i, j):
        if mat[i][j] == -1:
            if i == j:
                mat[i][j] = 1
            elif input_str[i] == input_str[j]:
                if i + 1 == j:
                    mat[i][j] = 2
                else:
                    mat[i][j] = 2 + F(i + 1, j - 1)
            else:
                mat[i][j] = max(F(i + 1, j), F(i, j - 1))
        return mat[i][j]

    max_length = F(0, n - 1)
    
    def restore_palindrome(i, j):
        if i > j:
            return ""
        if i == j:
            return input_str[i]
        if input_str[i] == input_str[j]:
            return input_str[i] + restore_palindrome(i + 1, j - 1) + input_str[j]
        if mat[i + 1][j] > mat[i][j - 1]:
            return restore_palindrome(i + 1, j)
        else:
            return restore_palindrome(i, j - 1)
    
    max_palindrome = restore_palindrome(0, n - 1)
    
    return max_length, max_palindrome

input_str = input()
max_length, max_palindrome = find_longest_palindrome(input_str)
print(max_length)
print(max_palindrome)




