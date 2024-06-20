...
Задача о палиндроме.
Напишите функцию, которая будет принимать в себя тип данных int (число) и
возвращать тип bool, если переданное число является палиндромом.
Палиндром — слово, фраза или символы, которые одинаково читаются слева направо
и справа налево.
Пример 1:
Input: x = 121
Output: true
Объяснение: так как число читается одинаково в обе стороны, то функция вернёт True.
Пример 2:
Input: x = -121
Output: false
Пример 3:
Input: x = 10
Output: false
...

def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    original_num = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return original_num == reversed_num
