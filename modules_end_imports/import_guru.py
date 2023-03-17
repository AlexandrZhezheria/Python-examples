# Настав час стати гуру імпортів!
# Для цього виріши завдання, в якому тобі потрібно буде використати кілька варіантів імпортування вбудованих модулів.
# Імпортуй необхідні модулі, щоб вже написані функції почали працювати. Код самих функцій не можна змінювати!
# Імпортуй модуль datetime в окремому рядку
# Імпортуй модуль time із псевдонімом t, використовуючи для цього оператор as
# З модуля random імпортуй єдину функцію randint
# З модуля math імпортуй дві функції ceil та floor в одному рядку
# Підказка:
# Щоб імпортувати функцію з модуля, скористуйся оператором from

import datetime
import time as t
from random import randint
from math import ceil, floor

def print_current_time() -> None:
    print(t.time())


def generate_random_tuple(size: int) -> tuple:
    return (randint(-10, 10) for _ in range(size))


def floor_division(a: int, b: int) -> int:
    return floor(a / b)


def ceil_division(a: int, b: int) -> int:
    return ceil(a / b)


def create_today_date() -> datetime:
    return datetime.date.today()