# Ти працюєш шкільним вчителем. Щоб полегшити собі роботу з точками на координатній площині, ти вирішив створити відповідний клас
# Напиши клас Point. Його метод __init__ приймає і зберігає x, y координати точки. Всі створені екземпляри повинні
# зберігатись в списку points - атрибуті класа Point.
# Клас Point повинен надавати такі методи:
# distance_to_origin - повертає відстань від точки до початку координат
# distance_to_point - приймає точку point і повертає відстань від поточної точки до point
# distance_to_x_axis - повертає відстань до осі Х
# distance_to_y_axis - повертає відстань до осі Y

from __future__ import annotations


class Point:
    points = []

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.__class__.points.append(self)

    def distance_to_origin(self) -> float:
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)

    def distance_to_point(self, point: Point) -> float:
        return round(
            ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2
        )

    def distance_to_x_axis(self) -> int:
        return abs(self.y)

    def distance_to_y_axis(self) -> int:
        return abs(self.x)

    def find_closest_point(self) -> Point:
        closest_point = None
        closest_distance = None
        for point in self.__class__.points:
            if point is not self:
                if closest_distance is None:
                    closest_distance = self.distance_to_point(point)
                    closest_point = point
                elif self.distance_to_point(point) < closest_distance:
                    closest_distance = self.distance_to_point(point)
                    closest_point = point
        return closest_point




# Приклад:
point = Point(3, 4)

point.distance_to_origin() == 5

point_2 = Point(-5, -1)

point.distance_to_point(point_2) == 9.43
point.distance_to_x_axis == 4
point.distance_to_y_axis == 3

find_closest_point - повертає
найближчу
точку
до
поточної
серед
інших
створених
точок, якщо
інших
точок
немає - повертає
None
point = Point(3, 4)
point_2 = Point(-5, -1)
point_3 = Point(4, 4)
point_4 = Point(1, 1)

closest_point = point.find_closest_point()

(closest_point.x, closest_point.y) == (4, 4)
closest_point is point_3  # True

# Якщо результат методу - число з плаваючою точкою, округлити до другого знаку
# всі створені методи повинні мати анотації
