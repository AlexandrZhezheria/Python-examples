# Напиши функцію missing_number, яка приймає список унікальних чисел unique_nums у діапазоні [0, n] та повертає єдине число, відсутнє у списку.
# Приклади:
# missing_number([3,0,1]) == 2
# missing_number([9,6,4,2,3,5,7,0,1]) == 8
# missing_number([0, 1]) == 2


def missing_number(unique_nums: list) -> int:
    return sum(range(len(unique_nums) + 1)) - sum(unique_nums)
