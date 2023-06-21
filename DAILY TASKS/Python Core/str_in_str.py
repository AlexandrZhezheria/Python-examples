# Напиши функцію str_in_str яка приймає два рядкові аргументи haystack, needle та повертає індекс першої появи needle у haystack,
# якщо needle не є частиною haystack, поверніть -1, якщо needle є порожнім рядком, поверніть 0.
# Нотатки:
# haystack та needle складаються тільки з малих літер латинського алфавіту
# len(haystack) >= 1
# len(needle) >= 0
# Приклади:

str_in_str("hello", "ll") # повертає 2
str_in_str("hello", "bye") # повертає -1
str_in_str("hello", "") # повертає 0

def str_in_str(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
