# Напиши функцію maximum_product, яка приймає список цілих чисел та повертає максимальне значення, отримане від добутку двох сусідніх чисел у списку.
# Приклади:
# maximum_product([1, 2, 3]) == 6
# maximum_product([-5, 0, 3, 5, 2]) == 15

def maximum_product(num_list: list) -> int:
    if len(num_list) < 2:
        return 0 if len(num_list) == 0 else num_list[0]
    max_product = float("-inf")
    for i in range(len(num_list) - 1):
        product = num_list[i] * num_list[i + 1]
        if product > max_product:
            max_product = product
    return max_product
