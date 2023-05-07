# Напиши функцію isomorphic_strings, яка приймає рядки first_string, second_string та визначає, чи вони є ізоморфними.
# Рядки ізоморфні, якщо кількість та розташування символів в first_string є пропорційними до кількості та розташування в second_string.
# Усі входження конкретних символів мають бути замінені іншими символами зі збереженням їхнього порядку.
# Приклади:
# isomorphic_strings(first_string="egg", second_string="add") is True
# isomorphic_strings(first_string="foo", second_string="bar") is False
# isomorphic_strings(first_string="paper", second_string="title") is True

def isomorphic_strings(first_string: str, second_string: str) -> bool:
    d1, d2 = {}, {}
    for i, val in enumerate(first_string):
        d1[val] = d1.get(val, []) + [i]
    for i, val in enumerate(second_string):
        d2[val] = d2.get(val, []) + [i]
    return sorted(d1.values()) == sorted(d2.values())
