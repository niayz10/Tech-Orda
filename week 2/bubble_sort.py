array = [13456, 233, 123, 434, 5, 6, 7, 8]
flag = True

for i in range(len(array) - 1):
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(*array)
