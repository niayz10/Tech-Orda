a, b = int(input()), int(input())
max_d = (a * (a//b) + b * (b//a))/(b//a + a//b)
print(int(max_d))
