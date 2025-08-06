def sum_first(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sum_first(n - 1)

print(sum_first(5))

def tribonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

print(tribonacci(5))

def is_palindrome(s: str):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    inner = s[1:-1]
    return is_palindrome(inner)

print(is_palindrome('lagerregal'))
print(is_palindrome('stuttgart'))

def binom(n, k):
    if k == 0 or n == k:
        return 1
    return binom(n - 1, k - 1) + binom(n - 1, k)

# n=0             1
# n=1           1   1
# n=2         1   2   1
# n=3       1   3   3   1
# n=4     1   4   6   4   1
# n=5   1   5   10  10  5   1
# n=6 1   6   15  20  15  6   1