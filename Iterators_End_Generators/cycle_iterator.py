# Напиши ітератор Cycle, який приймає об'єкт iterable. Мета цього ітератора зациклити прохід по об'єкту iterable.
# Після останнього елемента iterable ітератор Cycle повинен знову повернути перший і почати прохід по iterable спочатку:

from typing import Any, Iterator


class Cycle:
    def __init__(self, iterable: Any) -> None:
        self.iterable = iterable
        self.iterator: Iterator = iter(iterable)

    def __iter__(self) -> "Cycle":
        return self

    def __next__(self) -> Any:
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)

# from __future__ import annotations
# from typing import Iterable, Union
#
#
# class Cycle:
#     def __init__(self, iterable: Iterable) -> None:
#         self.iterable = iterable
#
#     def __iter__(self) -> Cycle:
#         self.current_index = 0
#         return self
#
#     def __next__(self) -> Union[int, str, StopIteration]:
#         if not self.iterable:
#             raise StopIteration
#
#         res = self.iterable[self.current_index]
#         self.current_index = (self.current_index + 1) % len(self.iterable)
#
#         return res

# Приклади:

iterator = Cycle("abc")
print(next(iterator)) # a
print(next(iterator)) # b
print(next(iterator)) # c
print(next(iterator)) # a
print(next(iterator)) # b
print(next(iterator)) # c
print(next(iterator)) # a

iterator = Cycle([0, 1, 2, 3])
for i in range(10):
    print(next(iterator)) # 0 1 2 3 0 1 2 3 0 1

# Зверніть увагу, що якщо iterable порожній, то Cycle повинен відразу повертати помилку:

iterator = Cycle([])
next(iterator) # StopIteration exception