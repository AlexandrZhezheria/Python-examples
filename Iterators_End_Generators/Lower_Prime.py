# Напиши ітератор LowerPrime, його метод __init__ приймає та зберігає ціле число number.
# На першій ітерації LowerPrime повинен повертати найближче просте число, що менше за number,
# на кожній наступній ітерації він повертає найближче просте число, що менше за попереднє.
# Ітератор повинен raise StopIteration коли повернув найменше просте число - 2.

from __future__ import annotations
from typing import Union


class LowerPrime:
    def __init__(self, number: int) -> None:
        self.number = number
        self.current_number = number

    def __iter__(self) -> LowerPrime:
        self.current_number = self.number
        return self

    def __next__(self) -> Union[int, StopIteration]:
        for num in range(self.current_number - 1, 1, -1):
            if self.is_prime(num):
                self.current_number = num
                return num
        raise StopIteration

    @staticmethod
    def is_prime(number: int) -> bool:
        for divisor in range(2, number // 2 + 1):
            if number % divisor == 0:
                return False
        return True


# Приклад:

lower_prime = LowerPrime(number=11)
lower_prime_it = iter(lower_prime)
next(lower_prime_it) == 7
next(lower_prime_it) == 5
lower_prime_it.number == 11  # attribute 'number' does not change

lower_prime = LowerPrime(number=3)
lower_prime_it = iter(lower_prime)
next(lower_prime_it) == 2
next(lower_prime_it)
# Error: StopIteration

lower_prime = LowerPrime(number=11)
lower_prime_it = iter(lower_prime)
list(lower_prime_it) == [7, 5, 3, 2]
