def fibonacci(n: int) -> int:
    i, j = 1, 1
    k = 0
    for _ in range(1, n):
        k = j
        j = i + j
        i = k
    return j


n = int(input())
print(fibonacci(n))
