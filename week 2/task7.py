def election(x: int, y: int, z: int) -> bool:
    if x + y + z >= 2:
        return True
    return False


a = input()
x, y, z = a.split()
print(int(election(int(x), int(y), int(z))))
