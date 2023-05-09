# Напиши функцію last, яка повертає останній елемент переданого аргументу / аргументів.
# Приклади:
# last([1, 2, 3, 4]) == 4
# last("xyz") == "z"
# last(1, 2, 3, 4) == 4
# last(True, "qwerty", 56, []) == []


from typing import Any, Union


def last(*args: Any) -> Union[Any, None]:
    for arg in reversed(args):
        try:
            return arg[-1]
        except (TypeError, IndexError):
            pass
    return arg
