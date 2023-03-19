# І знову рефакторинг! На цей раз адмін магазину велосипедів попросив тебе оптимізувати код одного з його сервісів.
# Перед тобою два класи MountainBike та RoadBike, у яких абсолютно однакові поля та оголошений статичний метод from_dict,
# що створює екземпляр відповідного класу за словником.
# Очевидно, що цей код можна суттєво покращити. Для цього створи клас Bike, що буде батьківським для MountainBike та RoadBike.
# Винеси в цей клас метод from_dict так, щоб він коректно працював для дочірніх класів.
# Таким чином у класах MountainBike та RoadBike залишаться тільки методи __init__. Але їхнє тіло теж можна оптимізувати!
# Якщо всі атрибути (brand, model, max_speed) будуть збережені у класі Bike, то у методах __init__ дочірніх класів
# буде достатньо викликати метод __init__ у super() і всі потрібні значення запишуться в атрибути екземпляра класу.

from __future__ import annotations


class MountainBike:
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    @staticmethod
    def from_dict(bike_dict: dict) -> MountainBike:
        return MountainBike(
            brand=bike_dict["brand"],
            model=bike_dict["model"],
            max_speed=bike_dict["max_speed"],
        )


class RoadBike:
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    @staticmethod
    def from_dict(bike_dict: dict) -> RoadBike:
        return RoadBike(
            brand=bike_dict["brand"],
            model=bike_dict["model"],
            max_speed=bike_dict["max_speed"],
        )

# Приклад:

mountain_bike = MountainBike.from_dict({
  "model": "C2000",
  "brand": "Civia",
  "max_speed": 35,
})
isinstance(mountain_bike, MountainBike) is True
mountain_bike.brand == "Civia"
mountain_bike.model == "C2000"
mountain_bike.max_speed == 35