# Нам дається клас NumberInfo. Твоє завдання реалізувати властивості через декоратор @property так, аби:
# number - має бути записаний у захищений однойменний атрибут, а також має бути доступним для читання та запису.
# len_digits - повертає довжину цілої частини number
# is_integer - перевіряє, є число типом int
# is_float - перевіряє, є число типом float
# decimal - повертає кількість знаків після коми
# is_positive - перевіряє, є число додатним
# is_natural - перевіряє, є число натуральним
# is_prime - перевіряє, є чи число простим

from typing import Union


class NumberInfo:
    def __init__(self, number: int) -> None:
        self._number = number

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        self._number = value

    @property
    def is_prime(self) -> bool:
        if self._number < 2:
            return False
        if self.is_integer:
            for i in range(2, self._number):
                if self._number % i == 0 and self._number != 2:
                    return False
        if self.is_float:
            return False
        return True

    @property
    def len_digits(self) -> int:
        return len(str(int(self._number)))

    @property
    def is_integer(self) -> bool:
        return isinstance(self._number, int)

    @property
    def is_float(self) -> bool:
        return isinstance(self._number, float)

    @property
    def decimal(self) -> Union[int, float]:
        if self.is_integer:
            return 0
        return len(str(self._number).split(".")[-1])

    @property
    def is_positive(self) -> bool:
        return True if self._number > 0 else False

    @property
    def is_natural(self) -> bool:
        return True if self.is_positive and self.is_integer else False

# Приклад:

number_int = NumberInfo(1)

# number_int.number == 1
# number_int.len_digits == 1
# number_int.is_integer is True
# number_int.is_float is False
# number_int.decimal == 0
# number_int.is_positive is True
# number_int.is_natural is True
# number_int.is_prime is False

number_float = NumberInfo(123.1234)

# number_float.number == 123.1234
# number_float.len_digits == 3
# number_float.is_integer is False
# number_float.is_float is True
# number_float.decimal == 4
# number_float.is_positive is True
# number_float.is_natural is False
# number_float.is_prime is False