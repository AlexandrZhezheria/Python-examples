# В тебе є функція like_numbers, яка приймає список і повертає деякий рядок.
# Напиши 3 декоратори arrow, number_filter, round_dict, такі що:
# arrow перетворює вхідний словник у список рядків виду 'key -> value'.
# number_filter фільтрує вхідний список і залишає тільки числові типи
# round_dict округлює числа у вхідному списку і створює словник, де ключ - це нове значення числа, а його значення - подвоєне нове значення числа.
# Задекоруй функцію like_numbers трьома декораторами у правильному порядку так, щоб отримати результат показаний у прикладі.


from typing import Callable, Any


def arrow(func: Callable) -> Callable:
    def wrapper(items: dict) -> Any:
        new_items = [f"{key} -> {value}" for key, value in items.items()]
        return func(new_items)

    return wrapper


def round_dict(func: Callable) -> Callable:
    def wrapper(items: list) -> Any:
        new_items = {round(item): round(item) * 2 for item in items}
        return func(new_items)

    return wrapper


def number_filter(func: Callable) -> Callable:
    def wrapper(items: list) -> Any:
        new_items = [item for item in items if isinstance(item, (int, float))]
        return func(new_items)

    return wrapper


@number_filter
@round_dict
@arrow
def like_numbers(items: list) -> str:
    return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"


# Приклад:
# @round_dict
# @number_filter
# @arrow
# def like_numbers(items: list):
#     return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"

items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]

like_numbers(items)  # == "I like to filter, rounding, doubling, "
#    "store and decorate numbers: "
#    "2 -> 4, 4 -> 8, 9 -> 18, -123 -> -246!"
