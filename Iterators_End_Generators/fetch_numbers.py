# В тебе є ітератор NumberIterator.
# Напиши функцію fetch_numbers, яка приймає ітератор класу NumberIterator iterator та число number і повертає список з наступних number чисел ітератора.


from __future__ import annotations
from typing import Iterator, Union


class NumberIterator:
    def __init__(self, numbers: list) -> None:
        self.numbers = numbers

    def __iter__(self) -> NumberIterator:
        self.it = 0
        return self

    def __next__(self) -> Union[int, StopIteration]:
        if self.it >= len(self.numbers):
            raise StopIteration
        result = self.numbers[self.it]
        self.it += 1
        return result


def fetch_numbers(iterator: Iterator, number: int) -> list:
    numbers = []
    while len(numbers) < number:
        try:
            num = next(iterator)
            numbers.append(num)
        except StopIteration:
            break
    return numbers

# def fetch_numbers(iterator: Iterator, number: int) -> list:
#     result = []
#
#     for _ in range(number):
#         result.append(next(iterator))
#
#     return result


# Приклад:
iter_ = iter(
  NumberIterator([1, 2, 3, 4, 5])
)

fetch_numbers(iterator=iter_, number=3)  # [1, 2, 3]

next(iter_)  # 4

# Зауваж, що функція не повинна порушувати логіку ітератора. Вибравши 3 числа функцією, ми отримуємо четверте
# число використовуючи next() після неї. Також, функція повинна коректно працювати, якщо ми вже вибрали декілька чисел з ітератора перед цим.

# Приклад 2:
iter_ = iter(
  NumberIterator([1, 2, 3, 4, 5])
)

next(iter_)  # 1
next(iter_)  # 2

fetch_numbers(iterator=iter_, number=3)  # [3, 4, 5]