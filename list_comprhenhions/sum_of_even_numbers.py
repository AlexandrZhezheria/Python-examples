# Напиши функцію sum_of_even_numbers, яка приймає список цілих чисел numbers та повертає суму парних чисел у списку.
# Функція має містити тільки одну команду - return. Щоб розв'язати задачу в один рядок використай list comprehension.


def sum_of_even_numbers(numbers: list):
    return sum(num for num in numbers if num % 2 == 0)

# Приклади:

sum_of_even_numbers([]) # == 0
sum_of_even_numbers([1, 3, 5, 7]) # == 0
sum_of_even_numbers([2, 11, 2, 4]) # == 8