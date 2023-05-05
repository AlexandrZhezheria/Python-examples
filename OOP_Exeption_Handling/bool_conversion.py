# Напиши функції:
#
# from_int - приймає value, якщо value не є цілим числом, то викликає виняток TypeError, якщо value дорівнює одиниці, то повертає True, якщо нулю, то повертає False, якщо value це інше значення, то функція викликає виняток ValueError.

from typing import Any


class BoolConversionError(Exception):
    pass


def from_int(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError("Value not an integer!")
    if value == 0:
        return False
    if value == 1:
        return True
    raise ValueError("Incorrect value!")


def from_str(value: str) -> bool:
    if not isinstance(value, str):
        raise TypeError("Value not an str!")
    if value in ("False", "F", "0"):
        return False
    if value in ("True", "T", "1"):
        return True
    raise ValueError("Incorrect value!")


def make_bool(value: Any) -> bool:
    try:
        try:
            b = from_int(value)
        except TypeError:
            try:
                b = from_str(value)
            except TypeError:
                raise BoolConversionError(
                    f"Cannot convert to the bool {type(value)} type"
                )
    except ValueError:
        raise BoolConversionError(f"Cannot convert to the bool {value} value")
    else:
        return b

bool_value = from_int(1)
print(bool_value)  # True

bool_value = from_int(1.1)
# TypeError

# from_str - приймає value, якщо value не є рядком, то викликає виняток TypeError, якщо value це значення з ["True", "T", "1"], то повертає True, якщо з ["False", "F", "0"], то повертає False, якщо value це інше значення, то функція викликає виняток ValueError.
bool_value = from_str("1")
print(bool_value)  # True

bool_value = from_str("1.1")
# ValueError

# make_bool - приймає value, спочатку намагається викликати функцію from_int щоб отримати булеве значення, якщо from_int викликала виняток TypeError, то намагається викликати функцію from_str, якщо from_str також викликала виняток TypeError, то функція make_bool викликає виняток BoolConversionError з повідомленням: Cannot convert to the bool {type(value)} type". Якщо при якомусь із викликів функцій from_int і from_str піднявся виняток ValueError то функція make_bool має викликати виняток BoolConversionError з повідомленням: Cannot convert to the bool {value} value. Якщо функції вдалося отримати булеве значення, вона його повертає.
bool_value = make_bool(1)
print(bool_value)  # True

bool_value = make_bool("F")
print(bool_value)  # False

bool_value = make_bool("false")
# BoolConversionError: Cannot convert to the bool false value

bool_value = make_bool({True})
# BoolConversionError: Cannot convert to the bool <class "set"> type

# Виняток BoolConversionError має наслідуватись лише від класу Exception.