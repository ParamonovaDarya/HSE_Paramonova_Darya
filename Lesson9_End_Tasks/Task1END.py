def fib(n):
    print('Введите a:')
    a = int(input())
    print('Введите b:')
    b = int(input())
    for _ in range(n):
        yield a
        a, b = b, a + b
print('Введите число, сколько чисел будет в выдаче, n:')
n = int(input())
for number in fib(n):
    print(number)