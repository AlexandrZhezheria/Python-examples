# Напиши функцію two_sum, яка приймає список цілих чисел nums, ціле число target і повертає індекси двох чисел зі списку,
# якщо їхня сума дорівнює target.
# Індекси повинні бути відсортовані у порядку зростання.

def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Приклади:
# two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1] # 2 + 7 = 9
# two_sum(nums=[3, 2, 4], target=6) == [1, 2] # 2 + 4 = 6

print(two_sum(nums=[2, 7, 11, 15], target=9))
print(two_sum(nums=[3, 2, 4], target=6))
