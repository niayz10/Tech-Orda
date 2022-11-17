a, b, c = int(input()), int(input()), int(input())
if a >= b >= c:
    print(c, b, a)
elif a <= b <= c:
    print(a, b, c)
elif b >= a >= c:
    print(c, a, b)
elif b >= c >= a:
    print(a, c, b)
elif c >= a >= b:
    print(b, a, c)
elif a >= c >= b:
    print(b, c, a)
