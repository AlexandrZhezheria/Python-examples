# Для списку nums розміру n поверніть найбільший елемент.
# Найбільшим елементом є елемент, який з’являється більше n / 2 разів.
# Найбільший елемент завжди існує в масиві.
# Приклади:
#     Input: nums = [3,2,3]
#     Output: 3
#     Input: nums = [2,2,1,1,1,2,2]
#     Output: 2

def majority_element(nums: list) -> int:
    counter = {}
    n = len(nums)
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
        if counter[num] > n / 2:
            return num
