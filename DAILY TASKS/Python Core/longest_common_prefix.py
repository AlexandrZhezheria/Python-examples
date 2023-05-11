# Напишіть функцію, яка знаходить спільний префікс серед усіх рядків у списку. Рядки у списку складаються лише з букв нижнього регістру.
# Якщо спільного префікса немає, повертає порожній рядок "".
# Приклад 1:
# Input: strings_list = ["flower","flow","flight"]
# Output: "fl"
# Приклад 2:
# Input: strings_list = ["dog","racecar","car"]
# Output: "" - спільного префікса не знайдено


def longest_common_prefix(strings_list: list) -> str:
    if not strings_list:
        return ""

    prefix = strings_list[0]
    for i in range(1, len(strings_list)):
        while strings_list[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
