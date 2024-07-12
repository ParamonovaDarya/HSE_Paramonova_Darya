def is_monotonic(array):
    increasing = True
    decreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            increasing = False
        if array[i] > array[i - 1]:
            decreasing = False

    return increasing or decreasing
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(is_monotonic([a, b, c, d]))