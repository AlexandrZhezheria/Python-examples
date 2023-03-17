# Напиши функцію prime_numbers, яка приймає список чисел numbers і повертає словник, який показує які числа є простими.
# Тобі вже дана функція is_prime, яка перевіряє чи число просте. Використовуй її.
# Функція повинна містити тільки конструкцію return. Використовуй dict comprehension.

def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_numbers(numbers: list) -> dict:
    return {num: is_prime(num) for num in numbers}



# Приклад:
numbers = [19]
prime_numbers(numbers) # == {19: True}

numbers = [3, 6, 12, 17]
prime_numbers(numbers) # == {3: True, 6: False, 12: False, 17: True}
