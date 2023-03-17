# Реалізуй функцію numbers_handler, яка приймає список чисел numbers і три колбеки:
# before - колбек, який першим викликається для кожного з чисел
# action - викликається другим для кожного з чисел
# after - викликається останнім для кожного з чисел
# Кожен із колбеків має єдиний параметр - число number.
# Функція повинна викликати всі три колбеки у вказаному порядку для кожного з чисел.
# Крім того, реалізуй значення за замовчуванням для цих колбеків.
# Для before напиши функцію new_number, яка приймає число та виводить рядок Received a new number: {number} за допомогою функції print.
# Для action напиши функцію is_positive, яка приймає число та виводить рядок {number} is a
# positive number якщо число number - додатне, рядок Zero, якщо число дорівнює нулю, і рядок {number} is a negative number, якщо число від'ємне.
# Для after напиши функцію print_bye, яка просто виводить рядок Bye!.

from typing import Callable


def new_number(number: int) -> None:
    print(f"Received a new number: {number}")


def is_positive(number: int) -> None:
    if number > 0:
        print(f"{number} is a positive number")
    elif number == 0:
        print("Zero")
    else:
        print(f"{number} is a negative number")


def print_bye(number: int) -> None:
    print("Bye!")


def numbers_handler(
    numbers: list,
    before: Callable = new_number,
    action: Callable = is_positive,
    after: Callable = print_bye,
) -> None:
    for number in numbers:
        before(number)
        action(number)
        after(number)

# Приклади:
numbers_handler([1, -1, 0]) # викликаємо функцію зі значеннями функцій за замовчуванням
# на екран виводиться:
# Received a new number: 1
# 1 is a positive number
# Bye!
# Received a new number: -1
# -1 is a negative number
# Bye!
# Received a new number: 0
# Zero
# Bye!


def print_hello(number):
    print("Hello!")

def some_action(number):
    print("Action!")

numbers_handler([10], action=some_action, before=print_hello)
# Викликаємо функцію зі своїми функціями
# на екран виводиться:
# Hello!
# Action!
# Bye!
