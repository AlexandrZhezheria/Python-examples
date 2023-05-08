# Напишіть функцію find_function яка приймає:
# list_with_function - список з анонімною функцією в будь-якому місці списку
# list_to_filter - список, який ви фільтруватимете за допомогою знайденої вами анонімної функції.
# Функція повертає відфільтровану версію другого параметра list_to_filter, використовуючи функцію, знайдену в першому параметрі.
# Приклади:
# list_with_function = [lambda a: a% 2 == 0, 9, 3, 1, 0]
# list_to_filter = [1, 2, 3, 4]
# find_function(list_with_function, list_to_filter)  # повертає [2, 4]
# list_with_function = [9, 3, lambda а: а % 2, 1, 0]
# list_to_filter = [1, 2, 3, 4]
# find_function(list_with_function, list_to_filter)  # повертає [1, 3]
#
# list_with_function = [9, 3, lambda a: a % 13 == 0, 1, 0]
# list_to_filter = [1, 2, 3, 4]
# find_function(list_with_function, list_to_filter)  # повертає []


def find_function(list_with_function: list, list_to_filter: list) -> list:
    for item in list_with_function:
        if callable(item):
            return list(filter(item, list_to_filter))
    return []
