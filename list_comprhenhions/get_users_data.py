# Тобі приходять данні про користувачів твоєї компанії. Але ці данні не впорядковані і, щоб полегшити роботу своїх колег,
# тобі треба їх структурувати. Було б не погано мати таку структуру даних, в якій ти можеш отримати інформацію
# про користувача, звертаючись за id цього користувача.
# Напиши функцію get_users_data, яка отримує список з даними користувачів.
# Список з даними користувачів це список, який складається з кортежів, кожний з яких складається з чотирьох значень:
# id, username, email, password конкретного користувача.
# Функція повинна повертати словник, в якому ключі це id користувача, а значення цих ключей - також словник з рештою даних:
# username, email, password.
# Функція повинна містити тільки інструкцію return. Використовуй dict comprehension.


def get_users_data(users: list) -> dict:
    return {
        user[0]: {"username": user[1], "email": user[2], "password": user[3]}
        for user in users
    }




# Приклад:
users = [
          (12, "Maxim", "maxim@example.com", "UBg11eub42hge")
        ] # Тільки один користувач
get_users_data(users) == {
    12: {
          "username": "Maxim",
          "email": "maxim@example.com",
          "password": "UBg11eub42hge"
        },
}  # В результаті словник з одним ключем - id користувача


users = [
            (12, "Maxim", "maxim@example.com", "UBg11eub42hge"),
            (13, "Dmitro", "dmitro@example.com", "sdTioT36723fw"),
            (14, "Roman", "roman@example.com", "hbFEkj34NggE2"),
            (15, "Ivan", "ivan@example.com", "sdTioT36723fw"),
        ] # Чотири користувачі

get_users_data(users) == {
    12: {"username": "Maxim", "email": "maxim@example.com", "password": "UBg11eub42hge"},
    13: {"username": "Dmitro", "email": "dmitro@example.com", "password": "sdTioT36723fw"},
    14: {"username": "Roman", "email": "roman@example.com", "password": "hbFEkj34NggE2"},
    15: {"username": "Ivan", "email": "ivan@example.com", "password": "sdTioT36723fw"},
} # В результаті словник з чотирма ключами - id користувачів
