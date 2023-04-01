# Уяви себе вчителем геометрії.
# Ти малюєш на дошці одну точку з координатами х та у та просиш учнів «скопіювати» собі цю точку в зошит. Після цього ти домальовуєш ще 2 точки та поєднуєш їх у трикутник.
# Звісно ж, ти просиш учнів скопіювати собі тепер увесь трикутник до зошита, щоб вони могли далі розв'язувати задачу.
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: float) -> bool:
        # Check if `other` is an instance of `Point`
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def copy(self) -> Point:
        # Create a new `Point` object with the same `x` and `y` values
        return Point(self.x, self.y)


class Triangle:
    def __init__(self, first_point: Point, second_point: Point, third_point: Point) -> None:
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point

    def __repr__(self) -> str:
        return f"Triangle out of {self.first_point}, {self.second_point}, {self.third_point}"

    def __eq__(self, other: float) -> bool:
        # Check if `other` is an instance of `Triangle`
        if isinstance(other, Triangle):
            return (
                    self.first_point == other.first_point and
                    self.second_point == other.second_point and
                    self.third_point == other.third_point
            )
        return False

    def copy(self) -> Triangle:
        # Create a new `Triangle` object with copies of the three `Point` objects
        return Triangle(
            first_point=self.first_point.copy(),
            second_point=self.second_point.copy(),
            third_point=self.third_point.copy()
        )


def copy_point(point: Point) -> Point:
    # Call the `copy()` method of `Point` to create a new `Point` object
    return point.copy()


def copy_triangle(triangle: Triangle) -> Triangle:
    # Call the `copy()` method of `Triangle` to create a new `Triangle` object
    return triangle.copy()


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