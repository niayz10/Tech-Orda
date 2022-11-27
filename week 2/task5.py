a = int(input())
total = 0
i = 0
x = 0
while a > 0:
    x = a % 10
    if x == 1:
        total += 2**i
    i += 1
    a = a // 10

print(total)