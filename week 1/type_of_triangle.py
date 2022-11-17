a, b, c = int(input()), int(input()), int(input())
max_d = max(a, b, c)
if max_d != c:
    if max_d == a:
        a, c = c, a
    else:
        b, c = c, b
if a - b < c < a + b:
    if c ** 2 == (a ** 2 + b ** 2):
        print("right ")
    elif c ** 2 < (a ** 2 + b ** 2):
        print("acute ")
    elif c ** 2 > (a ** 2 + b ** 2):
        print("obtuse ")
else:
    print("impossible")
