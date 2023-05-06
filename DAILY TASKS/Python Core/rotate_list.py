# Напиши функцію rotate_list, яка приймає список чисел та кількість кроків steps і повертає список,
# зрушений праворуч на steps кроків, де steps – ціле додатне число.
# Приклади:
# rotate_list(nums=[1, 2, 3, 4, 5, 6, 7], steps = 3) == [5, 6, 7, 1, 2, 3, 4]
# rotate_list(nums=[-1, -100, 3, 99], steps = 2) == [3, 99, -1, -100]

def rotate_list(nums: list, steps: int) -> list:
    return nums[-steps:] + nums[:-steps]
