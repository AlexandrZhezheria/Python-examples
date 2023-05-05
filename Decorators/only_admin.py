# У тебе є функція create_permissions, яка отримує список словників з користувачами та виводить повідомлення про створені дозволи.
# Твоя задача написати такий декоратор only_admin, який бере перший аргумент users, переданий в функцію, і потім фільтрує
# тільки тих користувачів, у кого is_admin = True, і тільки для таких користувачів викликає функцію, яку він декорує.


def create_permissions(users: list) -> None:
    for user in users:
        print(f"Creating permissions for {user["username"]}")


def only_admin(func):
    # write your code here
    pass

# Приклад:

@only_admin
def create_permissions(users: list) -> None:
    for user in users:
        print(f"Creating permissions for {user["username"]}")

users = [
     {"username": "admin", "is_admin": True},
     {"username": "moderator_a11", "is_admin": True},
     {"username": "custom_user1", "is_admin": False},
     {"username": "custom_user2", "is_admin": False},
     {"username": "admin_2nd", "is_admin": True},
]

create_permissions(users)
# Creating permissions for admin
# Creating permissions for moderator_a11
# Creating permissions for admin_2nd