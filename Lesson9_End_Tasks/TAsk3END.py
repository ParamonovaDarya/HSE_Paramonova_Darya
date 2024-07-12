...
Задание 3
Монотонная последовательность — это последовательность, элементы которой с
увеличением номера только возрастают, или, наоборот, только убывают.
Массив nums является монотонно возрастающим, если верно i <= j, nums[i] <= nums[j].
Напишите функцию, которая будет принимать в себя массив, состоящий из цифр, и
возвращать:
true — если массив является монотонным,
false — в обратном случае.
...

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
