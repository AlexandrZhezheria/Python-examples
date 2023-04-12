# Напиши декоратор error_handler, який потрібний для того, щоб у разі помилок певного типу повернути результат
# виконання необхідного callback-у.
# Декоратор повинен мати такі параметри:
# error_type - тип винятку, що має обробляти декоратор
# callback - колбек, який декоратор повинен викликати у разі виникнення очікуваної помилки
# *callback_args та **callback_kwargs, аргументи, які потрібно передати в callback
# Такий декоратор може бути корисним у великій кількості випадків. Наприклад, ми використовуємо функцію, яка має надсилати дуже важливу інформацію одному з наших сервісів. У випадку, якщо вона не пройшла (через інтернет, погоду або поганий гороскоп), ми хочемо, щоб сповіщення про це надсилалося на наш email. Це завдання можна легко вирішити за допомогою такого декоратора:

# write code below this line


def func_produce_value_error() -> int:
    print("Hello, ValueError")
    return int("0.2")


def func_produce_type_error() -> str:
    print("Hello, TypeError")
    return 10 + "10"

def send_alert_to_the_email(email: str):
    send_email(email, "We have some troubles!")

@error_handler(SendingInfoError, send_alert_to_the_email, "admin123@company")
def send_important_information(information):
    print("Sending important information...")
    server.send(information) # May produce an error

# Застосуй декоратор для функції func_produce_type_error, яку вже оголошено у файлі. Передай як callback функцію func_produce_value_error. Але оскільки вона теж викликає помилку, то застосуй до функції func_produce_type_error ще один callback, який вже оброблятиме помилку ValueError. В якості обробника передай функцію, яка повертає рядок Bye, errors.
#
# Таким чином, після того, як ти задекоруєш функцію func_produce_type_error, вона працюватиме так:

print(func_produce_type_error())
# "Hello, TypeError"
# "Hello, ValueError"
# "Bye, errors"

# Примітка:
# Застосовуй всі декоратори лише до функції func_produce_type_error.