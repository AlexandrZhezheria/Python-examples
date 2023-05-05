# Ти працюєш на фабриці роботів. Ви провели перевірку старих роботів і відібрали ті моделі, які будуть корисні у майбутньому.
# Але є одна проблема: ці роботи настільки старі, що їх документація вже давно загублена. І тепер твоя задача налагодити копіювання цих роботів.
# Є клас Robot, його метод __init__ приймає значення model, constructor, serial_no і зберігає їх у властивостях відповідно.
# Напиши функцію copy_robot, яка приймає robot екземпляр класу Robot, вона повинна повертати копію robot, але зі збільшеним serial_no на одиницю.


class Robot:
    def __init__(self, model: str, constructor: str, serial_no: int) -> None:
        self.model = model
        self.constructor = constructor
        self.serial_no = serial_no


def copy_robot(robot: Robot) -> Robot:
    new_serial_no = robot.serial_no + 1
    return Robot(robot.model, robot.constructor, new_serial_no)

# Приклад:
robot = Robot("g135", "Alex", 1664)
robot_copy = copy_robot(robot)

robot_copy is robot == False
robot_copy.model == "g135"
robot.serial_no == 1664
robot_copy.serial_no == 1665