# Твоє завдання – написати функцію sum_of_a_sequence, яка повертає суму послідовності цілих чисел.
# Послідовність визначається трьома додатними значеннями: begin_number, end_number, step.
# Якщо begin_number є більшим, ніж end_number, функція має повернути 0.
# Приклади:
# sum_of_a_sequence(begin_number=1, end_number=7, step=1) == 28 # 1 + 2 + 3 + 4 + 5 + 6 + 7
# sum_of_a_sequence(begin_number=2, end_number=6, step=2) == 12 # 2 + 4 + 6
# sum_of_a_sequence(begin_number=9, end_number=3, step=3) == 0


def sum_of_a_sequence(begin_number: int, end_number: int, step: int) -> int:
    return sum(range(begin_number, end_number + 1, step))
