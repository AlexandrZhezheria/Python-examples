# В роботі месенджера зʼявилась несправність. Усі букви в повідомленнях змінили свій регістр випадковим чином.
# В тебе вже є клас, який частково справляється з цією проблемою. Його метод __init__ приймає message і зберігає вже виправлену версію.
# У нього є метод set_message, який приймає message виправляє та зберігає його. Також у нього є метод get_message який повертає message.
# Перепиши цей клас використовуючи property з назвою message, get_message повинен стати property getter"ом,
# а set_message - property setter"ом. Getter та setter повинні використовувати захищену властивість (її імʼя починається на _).

# refactor this code


class CorrectMessage:
    def __init__(self, message: str) -> None:
        self._message = ""
        self.message = message

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        self._message = message.lower().capitalize()

# Приклад:

correct_message = CorrectMessage("heLLO, wORlD!")
print(correct_message.message)  # Hello, world!

correct_message.message = "aNOther CoRREcT meSSAge"
print(correct_message.message)  # Another correct message

"message" in correct_message.__dict__  # False
# message is property, not an instance attribute

# Підказка: використовуй декоратор @property