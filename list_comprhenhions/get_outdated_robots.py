# Функція get_outdated_robots приймає список роботів robots і повертає список індексів тих роботів, у яких core_version
# менший за new_version.
# Ти вже робив це завдання раніше, тепер спробуй вирішити його в один рядок, використовуючи list comprehension.
# Функція повинна містити тільки конструкцію return.


def get_outdated_robots(robots: list, new_version: int) -> list:
    return [i for i, robot in enumerate(robots) if robot["core_version"] < new_version]
# Я використав enumerate для того, щоб отримати індекс кожного робота у списку.
# Потім я перевірив, чи менший core_version робота за new_version і повернув список індексів тих роботів, у яких ця умова виконується.

# Приклад:
robots = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]

get_outdated_robots(robots, 10) # == [0, 3]
get_outdated_robots(robots, 14) # == [0, 1, 3]
get_outdated_robots(robots, 8) # == []
get_outdated_robots(robots, 18) # == [0, 1, 2, 3, 4]