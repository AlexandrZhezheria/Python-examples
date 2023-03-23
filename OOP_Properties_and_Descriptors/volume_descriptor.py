# Реалізуй дескриптор Volume для класу Box. Клас Box приймає в методі __init__ три аргументи:
# length - довжину коробки
# width - ширину коробки
# height - висоту коробки І має їх записати в однойменні публічні атрибути.
# Дескриптор Volume повинен мати єдиний метод __get__, що повертав би об'єм за аттрибутами length, width та height.
# Використай дескриптор Volume у класі Box, щоб за допомогою нього обчислювати об'єм коробки.

class Volume:
    def __get__(self, instance, owner):
        return instance.length * instance.width * instance.height

class Box:
    volume = Volume()

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

small_box = Box(2, 4, 6)
print(small_box.volume)         # 48
big_box = Box(10, 20, 15)
print(big_box.volume)           # 3000

# Примітка:
# Дескриптор має бути створений як аттрибут volume класу Box.