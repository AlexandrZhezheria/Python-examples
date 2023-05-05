# Ти полюбляєш швидку їзду. Але, щоб вибрати машину, ти спочатку повинен відфільтрувати їх так, що серед них не буде машини
# з потужністю менше бажаної.
# Напиши функцію powerful_cars, яка приймає число minimal_hp і список brand_cars, де кожний елемент це список машин
# певного бренду, в якому кожний елемент це словник з елементами "name" та "HP". Функція повинна повертати ідентичну
# структуру даних, але тільки з машинами, в яких потужність не менше minimal_hp.
# Функція повинна містити тільки конструкцію return. Використовуй list comprehension всередині іншого list comprehension.


def powerful_cars(brand_cars: list, minimal_hp: int) -> list:
    return [[car for car in cars if car["HP"] >= minimal_hp] for cars in brand_cars]

# Приклад:
brand_cars = [
    [{"name": "Ferrari_F430", "HP": 483},
     {"name": "Ferrari_360", "HP": 395},
     {"name": "Ferrari_488", "HP": 661}],
    [{"name": "Lamborghini_Aventador", "HP": 690},
     {"name": "Lamborghini_Gallardo", "HP": 560}]
]
minimal_hp = 661
powerful_cars(brand_cars, minimal_hp) == [
    [{"name": "Ferrari_488", "HP": 661}],
    [{"name": "Lamborghini_Aventador", "HP": 690}]
]