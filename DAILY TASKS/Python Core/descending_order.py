# Твоє завдання – написати функцію descending_order, яка може прийняти будь-яке позитивне ціле число як аргумент
# і повернути його із цифрами в порядку спадання.
# Приклади:
# descending_order(42145) == 54421
# descending_order(123456789) == 987654321


def descending_order(num_value: int) -> int:
    return int("".join(sorted(str(num_value), reverse=True)))
