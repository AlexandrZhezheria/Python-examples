# Ти працюєш на фабриці роботів. Конструктор розробив план нового цеху з роботами. Але, щоб приступити до виготовлення роботів,
# спочатку треба підрахувати кількість однакових частин, які виготовляються.
# Є клас Robot, його метод __init__ приймає кількість частин із яких він виготовляється: wheels, gears, pistons і
# зберігає їх у властивостях відповідно.
# Напиши функцію robots_parts, яка приймає список з екземплярами класу Robot, підраховує суму частин різного виду,
# записує її в словник з ключами 'wheels', 'gears', 'pistons' та повертає його.


class Robot:
    def __init__(self, wheels: int, gears: int, pistons: int) -> None:
        self.wheels = wheels
        self.gears = gears
        self.pistons = pistons


def robots_parts(robots: list) -> dict:
    parts_sum = {"wheels": 0, "gears": 0, "pistons": 0}
    for robot in robots:
        parts_sum["wheels"] += robot.wheels
        parts_sum["gears"] += robot.gears
        parts_sum["pistons"] += robot.pistons
    return parts_sum


# Приклад:
robots = [
  Robot(wheels=10, gears=18, pistons=16),
  Robot(wheels=4, gears=8, pistons=8),
  Robot(wheels=22, gears=17, pistons=30),
]

robots_parts(robots) == {
  'wheels': 36,
  'gears': 43,
  'pistons': 54
}