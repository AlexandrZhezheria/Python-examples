# Скоріш за все ти вже стикався з цим завданням, але цього разу тобі потрібно його вирішити використовуючи try/except.
# Напиши функцію create_dict, яка приймає кортеж зі значеннями keys_tuple і створює словник.
# В цьому словнику ключі це елементи з keys_tuple, а значення - їх порядкові номера.
# Як ти памʼятаєш, не всі значення можуть бути ключами словника.
# Використовуючи try/except записуй ключі в словник, а коли це неможливо -
# виводь повідомлення "Cannot add {value} to the dict!" для кожного неприпустимого значення.
# Писати except Exception це приклад поганого використання try/except, відловлюй тільки ту помилку,
# яку видає інтерпретатор, коли ти намагаєшся використовувати невідповідне значення як ключ словника.

def create_dict(keys_tuple: tuple) -> dict:
    result_dict = {}

    for it in range(len(keys_tuple)):
        try:
            result_dict[keys_tuple[it]] = it
        except TypeError:
            print(f"Cannot add {keys_tuple[it]} to the dict!")

    return result_dict

# Приклад:
dictionary = create_dict((7, 1, 3))
dictionary == {7: 0, 1: 1, 3: 2}

dictionary = create_dict((None, [1, 2], 5))
# Cannot add [1, 2] to the dict!
dictionary == {None: 0, 5: 2}

dictionary = create_dict((3, (1, 2), 5))
dictionary == {3: 0, (1, 2): 1, 5: 2}

dictionary = create_dict((3, (1, [2, 3]), [], int))
# Cannot add (1, [2, 3]) to the dict!
# Cannot add [] to the dict!
dictionary == {3: 0, int: 3}