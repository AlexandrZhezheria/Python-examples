# Ти працюєш розробником в Міністерстві освіти. Гримнув карантин і всіх учнів перевели на дистанційне навчання і замість
# звичайних щоденників знадобились електронні.
# Створи клас SchoolDiary, його метод __init__ приймає і зберігає оцінки з предметів math, history, literature.

class Grade:
    def __init__(self) -> None:
        self.minvalue = 2
        self.maxvalue = 12

    def __set_name__(self, owner, name) -> None:
        self.protected_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.protected_name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Grade should be integer")
        if value not in range(self.minvalue, self.maxvalue + 1):
            raise ValueError(
                f"Grade should not be less than {self.minvalue} and greater than {self.maxvalue}"
            )
        setattr(instance, self.protected_name, value)


class SchoolDiary:
    math = Grade()
    history = Grade()
    literature = Grade()

    def __init__(self, math: int, history: int, literature: int) -> None:
        self.math = math
        self.history = history
        self.literature = literature



alex = SchoolDiary(math=10, history=12, literature=9)
alex.math, alex.history, alex.literature  # 10, 12, 9

# Але, оскільки оцінка повинна бути цілим числом і бути в діапазоні від 2 до 12 включно, ці властивості зручно було б зберігати у вигляді дескрипторів.
# Напиши дескриптор Grade такий що:
# його метод __init__ повинен зберігати у властивості мінімальну і максимальну оцінку - minvalue та maxvalue.
# має метод __set_name__, який приймає імʼя атрибуту, додає в його початок _ і зберігає його у властивість protected_name.
# має метод __get__, який повертає значення атрибуту
# має метод __set__, який встановлює значення атрибуту, але цей метод повинен спочатку перевірити тип нового значення,
# якщо тип неправильний - повинен визивати виключення TypeError з повідомленням: Grade should be integer.
# Потім повинен перевірити чи знаходиться нове значеннях в межах minvalue та maxvalue, якщо ні,
# то повинен викликати виключення ValueError з повідомленням Grade should not be less than {self.minvalue} and greater than {self.maxvalue}.
alex = SchoolDiary(math="10", history="12", literature="9")
# TypeError: Grade should be integer

alex = SchoolDiary(math=15, history=12, literature=9)
# ValueError: Grade should not be less thаn 2 and greater than 12

# Памʼятай:
# дескриптори повинні бути створені в атрибутах класу
# __set__ та __get__ повинні оперувати тільки властивістю self.protected_name.
# викликати виключення можна за допомогою raise SomeError("...message...")