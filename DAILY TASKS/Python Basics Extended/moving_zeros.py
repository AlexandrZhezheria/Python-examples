# Напиши функцію moving_zeros яка приймає список nums, та повертає список, в котрому всі нулі переміщені в кінець.
# Збережи порядок решти елементів.

def moving_zeros(nums: list) -> list:
    zeros = []
    non_zeros = []
    for num in nums:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    return non_zeros + zeros


# Приклади:

print(moving_zeros([1, 0, 1, 2, 0, 1, 3])) # повертає [1, 1, 2, 1, 3, 0, 0]
print(moving_zeros([0, 2, 0, 1, 1, 0, 3])) # повертає [2, 1, 1, 3, 0, 0, 0]
print(moving_zeros([0,0])) # повертає [0, 0]
print(moving_zeros([])) # повертає []
