# Ти розробляєш веб-сервіс, на якому можуть реєструватися користувачі. Але, перед тим як додати їх дані аутентифікації в базу даних, треба, щоб ім"я та пароль користувача пройшли валідацію.

class InvalidUsername(Exception):
    pass


class PasswordMissmatch(Exception):
    pass


class ValidationError(Exception):
    pass


class DBUserCreationError(Exception):
    pass


def username_validation(username: str) -> None:
    if (
        len(username) < 4 or len(username) > 15
    ):  # not (4 <= len(username) <= 15)
        raise InvalidUsername("Username is too short, or too long!")


def password_validation(password1: str, password2: str) -> None:
    if password1 != password2:
        raise PasswordMissmatch("Password is not confirmed!")


def user_validation(user: dict) -> None:
    try:
        username_validation(user["username"])
        password_validation(user["password1"], user["password2"])
    except (PasswordMissmatch, InvalidUsername):
        raise ValidationError


def db_user_creation(user: dict) -> None:
    try:
        user_validation(user)
    except ValidationError:
        raise DBUserCreationError("Invalid user data provided!")
    print(f"{user["username"]} is created in the database.")

# Напиши функції:
# username_validation - приймає username і викликає виняток InvalidUsername, якщо довжина username менша за 4 чи більша за 15.
username_validation(username="Usr")
# InvalidUsername

# password_validation - приймає password1, password2 і викликає виняток PasswordMissmatch, якщо password1 і password2 не рівні між собою.
password_validation(password1="1234", password2="1111")
# PasswordMissmatch

# user_validation - приймає регістраційні дані користувача - словник з username, password1, password2 і валідує ці дані за допомогою функцій username_validation та password_validation. якщо якась з цих функцій викликає валідаційний виняток, то user_validation повинна обробити цей виняток і викликати виняток ValidationError.
user_validation(
  user={"username": "Usr",
        "password1": "1234",
        "password2": "1234"}
)
# ValidationError

user_validation(
  user={"username": "User1",
        "password1": "1234",
        "password2": "1111"}
)
# ValidationError

# db_user_creation - приймає словник user, викликає функцію user_validation і передає туди user. якщо user_validation викликає виняток валідації, то db_user_creation повинна обробити цей виняток і викликати виняток DBUserCreationError. якщо ж користувач успішно валідований - то функція виводить повідомлення {username} is created in the database.
db_user_creation(
    user={"username": "User1",
          "password1": "password",
          "password2": "password"},
)
# User is created in the database.

db_user_creation(
    user={"username": "UsernameUsername",
          "password1": "password",
          "password2": "password"},
)
#  DBUserCreationError

# Винятки InvalidUsername, PasswordMissmatch, ValidationError, DBUserCreationError, повинні наслідуватись від Exception.
# Щоб поставити однаковий обробник на декілька винятків використовуй except (FirstError, SecondError, ...):