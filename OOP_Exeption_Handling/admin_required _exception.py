# Дана функція access_admin_page, яка приймає словник request, вона надає доступ до сторінки адміна.
# Напиши для неї декоратори admin_required та login_required.
# login_required перевіряє наявність ключа user у словнику request і якщо його немає, це означає, що користувач не зайшов у свій акаунт.
# У цьому випадку декоратор повинен порушувати виняток UnauthenticatedError з повідомленням "Authentication credentials were not provided!".
# Інакше він не повинен змінювати поведінку переданої функції.
# admin_required перевіряє поле request["user"]["is_admin"] і якщо воно False, то це означає, що користувач не є адміном
# і видавати доступ до сторінки йому не можна. У цьому випадку декоратор повинен порушувати виняток PermissionDeniedError
# з повідомленням "User must be admin!". Інакше він не повинен змінювати поведінку функції, що декорується.
# Застосуйте декоратори до функції access_admin_page у правильному порядку не змінюючи її.

import functools
from typing import Callable, Union


class UnauthenticatedError(Exception):
    pass


class PermissionDeniedError(Exception):
    pass


def login_required(func: Callable) -> Callable:
    @functools.wraps(func)
    def inner(request: dict, *args, **kwargs) -> Union[UnauthenticatedError, Callable]:
        if "user" not in request:
            raise UnauthenticatedError(
                "Authentication credentials were not provided!"
            )

        return func(request, *args, **kwargs)

    return inner


def admin_required(func: Callable) -> Callable:
    @functools.wraps(func)
    def inner(request: dict, *args, **kwargs) -> Union[PermissionDeniedError, Callable]:
        if not request["user"]["is_admin"]:
            raise PermissionDeniedError("User must be admin!")

        return func(request, *args, **kwargs)

    return inner


@login_required
@admin_required
def access_admin_page(request: dict) -> None:
    print(f"Welcome to the admin page, {request["user"]["full_name"]}")


# Приклад:
request = {"user": {"full_name": "James Bond", "is_admin": True}}
access_admin_page(request)
# "Welcome to the admin page, James Bond"

request = {"user": {"full_name": "John Smith", "is_admin": False}}
access_admin_page(request)
# PermissionDeniedError: User must be admin!

request = {}
access_admin_page(request)
# UnauthenticatedError: Authentication credentials were not provided!
