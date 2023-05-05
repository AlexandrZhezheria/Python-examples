# Напиши функцію you_are_a_square, яка визначає, чи є число квадратом.
# Приклади:
# you_are_a_square(-1) is False # no square root from the negative number
# you_are_a_square(0) is True # square root of 0 is 0
# you_are_a_square(1) is True # square root of 1 is 1
# you_are_a_square(25) is True # square root of 25 is 5
# you_are_a_square(40) is False # square root of 40 is not an integer

import math


def you_are_a_square(number: int) -> bool:
    if number < 0:
        return False
    elif number == 0:
        return True
    else:
        root = math.sqrt(number)
        return root.is_integer()
