# Напиши функцію find_mode, яка приймає єдиний параметр ls - список. Вона повинна повертати моду списку, тобто елемент,
# який найчастіше зустрічається у списку. Якщо кілька елементів зустрічаються максимальну кількість разів, то поверни будь-який з них.

# Just google it :)
from statistics import mode
from typing import Any


def find_mode(ls: list[Any]) -> Any:
    if not isinstance(ls, list):
        raise TypeError("ls must be a list")
    if len(ls) == 0:
        raise ValueError("ls must be non-empty")
    return mode(ls)

find_mode([1]) == 1
find_mode([1, 2, 1, 1, 2]) == 1,
find_mode([5, "hello", 12, 33, "a", 12, "a", "a"]) == "a"

# Якщо було отримано не список, а аргумент іншого типу, поруш виняток TypeError з повідомленням ls must be a list

find_mode("not a list")  # raises TypeError: ls must be a list

# Якщо було отримано порожній список, то для нього неможливо обчислити моду, тому поруш виняток ValueError з повідомленням ls must be non-empty

find_mode([])  # raises ValueError: ls must be non-empty