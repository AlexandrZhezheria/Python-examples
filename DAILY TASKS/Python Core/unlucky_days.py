# П'ятниця 13-го вважається нещасливим днем.
# Напиши функцію unlucky_days, яка приймає значення-рік і повертає кількість нещасливих днів у ньому.
# Приклади:
# unlucky_days(2015) == 3
# unlucky_days(1986) == 1

from datetime import date


def unlucky_days(year: int) -> int:
    counter = 0
    for months in range(1, 13):
        if date(year, months, 13).isoweekday() == 5:
            counter += 1
    return counter
