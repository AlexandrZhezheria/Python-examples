# Напиши генератор time_range, який приймає два аргументи, час початку та час закінчення: time_start,
# time_end - кортежі з трьома цілими hours, minutes, seconds.
# На першій ітерації time_range повинен повертати початковий час time_start, на кожній наступній ітерації
# він повертає попереднє значення, збільшене на одну секунду.
# Час закінчення може бути меншим за початковий.

def time_range(time_start: tuple, time_end: tuple) -> tuple:
    """Генератор, який повертає послідовність часів, починаючи з time_start і закінчуючи перед time_end."""
    current_time = list(time_start)
    while current_time != list(time_end):
        yield tuple(current_time)
        # Додаємо одну секунду до поточного часу
        current_time[2] += 1
        # Якщо секунди дорівнюють 60, додатково додаємо одну хвилину
        if current_time[2] == 60:
            current_time[2] = 0
            current_time[1] += 1
        # Якщо хвилини дорівнюють 60, додатково додаємо одну годину
        if current_time[1] == 60:
            current_time[1] = 0
            current_time[0] += 1
        # Якщо години дорівнюють 24, переносимо їх на наступний день
        if current_time[0] == 24:
            current_time[0] = 0


# Приклад:

t_range = time_range(time_start=(10, 0, 0),
                     time_end=(10, 0, 3))
next(t_range) == (10, 0, 0)
next(t_range) == (10, 0, 1)
next(t_range) == (10, 0, 2)
next(t_range)
# Error: StopIteration

t_range = time_range(time_start=(23, 59, 59),
                     time_end=(0, 0, 3))
t_range_list = list(t_range)
t_range_list == [
  (23, 59, 59),
  (0, 0, 0),
  (0, 0, 1),
  (0, 0, 2)
]