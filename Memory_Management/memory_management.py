# Уяви себе вчителем геометрії.
# Ти малюєш на дошці одну точку з координатами х та у та просиш учнів «скопіювати» собі цю точку в зошит. Після цього ти домальовуєш ще 2 точки та поєднуєш їх у трикутник.
# Звісно ж, ти просиш учнів скопіювати собі тепер увесь трикутник до зошита, щоб вони могли далі розв"язувати задачу.
import copy


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Triangle:
    def __init__(
        self,
        first_point: Point,
        second_point: Point,
        third_point: Point
    ) -> None:
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point

    def __str__(self) -> str:
        return f"Triangle out of ({self.first_point.x}, {self.first_point.y}), " \
               f"({self.second_point.x}, {self.second_point.y}), " \
               f"({self.third_point.x}, {self.third_point.y})"


def copy_point(point: Point) -> Point:
    return copy.copy(point)


def copy_triangle(triangle: Triangle) -> Triangle:
    return copy.deepcopy(triangle)


# А тепер твоє завдання. Реалізуй 2 класи:
# Point, який приймає x та y:
point = Point(x=1, y=1)

# Triangle, який приймає 3 точки: first_point, second_point та third_point:
triangle = Triangle(
   first_point=Point(0, 0),
   second_point=Point(1, 3),
   third_point=Point(5, 5)
)

# Також реалізуй функцію copy_point, яка приймає точку і повертає нову, абсолютно незалежну точку:

point = Point(x=1, y=1)
point2 = copy_point(point)

print(point is point2)  # False

# Аналогічно реалізуй функцію copy_triangle, яка копіює переданий трикутник, тобто повертає незалежний від надрукованого на дошці трикутник:

point = Point(x=1, y=1)
triangle = Triangle(
   first_point=Point(x=0, y=0),
   second_point=Point(x=1, y=3),
   third_point=Point(x=5, y=5)
)
copied_triangle = copy_triangle(triangle)

print(triangle is copied_triangle)  # False
print(triangle.first_point is copied_triangle.first_point)  # False

# Зауваж, що print(point) та print(triangle) повинні виглядати ось так:

point = Point(x=1, y=1)
print(point)  # Point(1, 1)

triangle = Triangle(
   first_point=Point(x=0, y=0),
   second_point=Point(x=1, y=3),
   third_point=Point(x=5, y=5)
)
print(triangle)  # Triangle out of (0, 0), (1, 3) ,(5, 5)