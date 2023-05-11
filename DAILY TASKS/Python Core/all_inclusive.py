# Напиши функцію all_inclusive, яка приймає рядок - string та список рядків lst і повертає:
# True, якщо всі обороти рядків включені до lst (оборот - це перенесення останнього символу рядка на початок рядка),
# наприклад, рядок abc складається із трьох обертів: cab bca abc. Якщо в списку, крім оборотів, є інші рядки, то вони ігноруються.
# False, якщо хоча б один оборот не включений до lst.
# Примітка:
# будемо вважати, що оборотів рядка "" немає, тому для будь-якого lst: all_inclusive("", lst) --> true
# Приклади:
# all_inclusive("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) # повертає Тrue - список включає всі обороти
# all_inclusive("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) # повертає False
# - оборот "yAjylvp" відсутній у списку


def all_inclusive(string: str, lst: list) -> bool:
    for i in range(len(string)):
        if string not in lst:
            return False
        string = string[1:] + string[0]
    return True
