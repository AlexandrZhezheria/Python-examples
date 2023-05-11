# Твій інтернет-магазин полюбляє роздавати купони на честь особливих подій. Деякі клієнти намагаються обдурити систему,
# вводячи неправильні номери або використовуючи прострочені купони.
# Створи функцію під назвою coupon_code, яка перевіряє, чи існує номер купону у системі та чи не є він простроченим.
# Купон перестає бути дійсним на наступний день ПІСЛЯ закінчення терміну дії.
# Усі дати передаються у вигляді рядків у наступному форматі: "MONTH DATE, YEAR".
# Приклади:
# coupon_code(
#     entered_code="123",
#     correct_code="123",
#     current_date="July 9, 2015",
#     expiration_date="July 9, 2015"
# ) is True
#
# coupon_code(
#     entered_code="123",
#     correct_code="123",
#     current_date="July 9, 2015",
#     expiration_date="July 2, 2015"
# ) is False
#
# Підказка
# Ти можеш імпортувати модуль datetime


from datetime import datetime


def coupon_code(
        entered_code: str,
        correct_code: str,
        current_date: str,
        expiration_date: str,
) -> bool:
    if entered_code != correct_code:
        return False

    current_date = datetime.strptime(current_date, "%B %d, %Y").date()
    expiration_date = datetime.strptime(expiration_date, "%B %d, %Y").date()

    if current_date > expiration_date:
        return False

    return True
