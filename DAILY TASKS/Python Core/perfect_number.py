# Досконале число — це ціле додатне число, яке дорівнює сумі своїх додатних дільників, не враховуючи саме число.
# Дільник цілого числа x — це ціле число, на яке x можна розділити без остачі.
# Створи функцію perfect_number, яка приймає ціле число number та повертає True, якщо number — perfect number, а в інакшому випадку повертає False.
# Приклади:
# Ввід: number = 28
# Вивід: True
# Пояснення: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, та 14 - дільники числа 28.
# Ввід: number = 7
# Вивід: False


def perfect_number(number: int) -> bool:
    if number <= 1:
        return False
    divisors_sum = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    return divisors_sum == number
