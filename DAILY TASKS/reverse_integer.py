# Напиши функцію reverse_integer, яка приймає 32-бітове ціле число number зі знаком, і повертає number з інвертованими цифрами задом наперед.
# Якщо інвертування number призводить до того, що значення виходить за межі діапазону 32-бітних цілих чисел зі знаком [-2**31, 2**31 - 1], поверни 0.
# Припустимо, що середовище не дозволяє зберігати 64-бітні цілі числа (зі знаком або без знака).
# Примітка:
# -2**31 <= number <= 2**31 - 1
# приклади:
# reverse_integer(123)  # повертає 321
# reverse_integer(-123)  # повертає -321
# reverse_integer(120)  # повертає 21

def reverse_integer(number: int) -> int:
    result = 0
    abs_number = abs(number)
    while abs_number:
        result = result * 10 + abs_number % 10
        abs_number //= 10

    if (
        result > 2**31 - 1
        or number > 2**31 - 1
        or result < -(2**31)
        or number < -(2**31)
    ):
        return 0
    return -result if number < 0 else result
