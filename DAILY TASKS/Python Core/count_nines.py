# Я хочу порахувати від 1 до number. Скільки разів я використовуватиму «9»?
# Напиши функцію count_nines, яка приймає number (number >= 0) як аргумент і повертає кількість дев'яток від 1 до number.
# Наприклад, 9, 19, 91 додадуть по одній дев'ятці кожен, 99, 199, 919 дадуть по дві дев'ятки кожен і т.д.
# Приклад:
# count_nines(8) # повертає 0
# count_nines(9) # повертає 1
# count_nines(10) # повертає 1
# count_nines(98) # повертає 18
# count_nines(100) # повертає 20


def count_nines(number: int) -> int:
    count = 0
    for i in range(1, number + 1):
        count += str(i).count("9")
    return count
