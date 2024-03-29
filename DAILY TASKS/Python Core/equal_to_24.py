# Гра, в яку я грав, коли був маленьким: витягував 4 карти з гральних карт, використовувавши + - * / та (),
# щоб зробити залишкові результати рівними 24.
# Напиши функцію equal_to_24, яка приймає 4 параметри first_card second_card third_card fouth_card (4 карти),
# діапазон значень 1-13 та повертає рядок "2 * 2 * 2 * 3" або "(4 + 2) * (5 - 1)”. Якщо неможливо обчислити 24, поверни "It's not possible!".
# Необхідно використовувати всі чотири карти, використовувати три чи дві карти неправильно; Використання карти двічі або більше також неправильне.
# Просто потрібно повернути одне правильне рішення, не потрібно визначати всі варіанти.
# Приклади:
# equal_to_24(1, 2, 3, 4)  # може повернути "(1 + 3) * (2 + 4)" або "1 * 2 * 3 * 4"
# equal_to_24(2, 3, 4, 5)  # може повернути "(5 + 3 - 2) * 4" або "(3 + 4 + 5) * 2"
# equal_to_24(3, 4, 5, 6)  # може повернути "(3 - 4 + 5) * 6"
# equal_to_24(1, 1, 1, 1)  # повертає "It's not possible!"
# equal_to_24(13, 13, 13, 13)  # повертає "It's not possible!"

import itertools as it


def equal_to_24(*cards) -> str:
    for template in ["aZ(bX(cVd))", "(aZb)X(cVd)", "((aZb)Xc)Vd"]:
        for card in it.permutations(cards):
            for prod in it.product("*/+-", repeat=3):
                temp = template
                for char in (
                    ("Z", prod[0]),
                    ("X", prod[1]),
                    ("V", prod[2]),
                    ("a", str(card[0])),
                    ("b", str(card[1])),
                    ("c", str(card[2])),
                    ("d", str(card[3])),
                ):
                    temp = temp.replace(*char)
                try:
                    if eval(temp) == 24:
                        return temp
                except ZeroDivisionError:
                    pass
    return "It's not possible!"
