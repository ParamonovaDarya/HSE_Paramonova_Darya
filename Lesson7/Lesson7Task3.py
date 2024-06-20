...
Задача о сумме двух элементов массива.
Напишите функцию, которая в качестве аргументов принимает массив (list) с числами
и целевое число. Функция должна возвращать индексы элементов, которые в сумме
дают целевое число.
Пример 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Объяснение: так как nums[0] + nums[1] == 9, возвращается список с индексами [0, 1].
Пример 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Пример 3:
Input: nums = [3,3], target = 6
Output: [0,1]
...

def find_sum_indices(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
