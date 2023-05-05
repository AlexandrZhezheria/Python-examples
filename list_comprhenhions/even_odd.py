# Напиши функцію even_odd, яка приймає список цілих чисел. Вона повинна перевірити кожне число на парність
# і повернути список, що складається з "even" чи "odd".
# Функція повинна містити тільки інструкцію return. Використовуй list comprehension.
# Тут можуть згодитись тернарні оператори.


def even_odd(numbers: list) -> list:
    return ["odd" if num % 2 else "even" for num in numbers]


# Приклад:
even_odd([4]) # == ["even"]
even_odd([145, -24442, 317]) # == ["odd", "even", "odd"]