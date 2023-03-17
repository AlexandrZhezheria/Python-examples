# Реалізуй клас RockBand, який зберігатиме інформацію про музичну групу. Метод __init__ класу повинен приймати два
# параметри та зберегти їх у відповідні атрибути:
# name - назва групи
# members - список учасників групи

class RockBand:
    def __init__(self, name: str, members: list) -> None:
        self.name = name
        self.members = members

    def add_new_member(self, new_member: str) -> None:
        if new_member in self.members:
            print(f"{new_member} is already in the band!")
        else:
            self.members.append(new_member)

    def __add__(self, other: "RockBand") -> "RockBand":
        united_name = f"{self.name} {other.name} United"
        united_members = list(set(self.members + other.members))
        united_band = RockBand(united_name, united_members)
        return united_band

# from __future__ import annotations
#
#
# class RockBand:
#     def __init__(self, name: str, members: list) -> None:
#         self.name = name
#         self.members = members
#
#     def add_new_member(self, new_member: str) -> None:
#         if new_member not in self.members:
#             self.members.append(new_member)
#         else:
#             print(f"{new_member} is already in the band!")
#
#     def __add__(self, other: RockBand) -> RockBand:
#         members = []
#         members.extend(self.members)
#         for member in other.members:
#             if member not in members:
#                 members.append(member)
#         band_name = f"{self.name} {other.name} United"
#         return RockBand(name=band_name, members=members)
#
#     def __iadd__(self, other: RockBand) -> None:
#         for member in other.members:
#             if member not in self.members:
#                 self.members.append(member)



# Приклад ініціалізації екземпляра цього класу:
the_beatles = RockBand(
  "The Beatles",
  ["John Lennon", "Paul McCartney", "George Harrison"]
)
# У класі RockBand має бути метод add_new_member, який приймає рядок new_member - нового учасника групи.
# Якщо такий учасник з таким ім'ям вже є, то метод має виводити рядок про помилку у форматі {new_member} is already in the band!.
# Інакше учасник має бути доданий до списку members
# the_beatles.add_new_member("Ringo Starr")
# the_beatles.add_new_member("John Lennon") # 'John Lennon already in the band'
# Групи часто об'єднуються в одну, і клас RockBand теж повинен підтримувати цю можливість. Реалізуйте магічний метод __add__.
# В результаті складання двох груп має виходити група:
# назва якої дорівнює {name1} {name2} United, де name1 - це назва першої групи, а name2 - назва другої групи
# а список учасників отримується шляхом об'єднання учасників обох груп. Зверніть увагу, що якщо учасник є в обох групах
# до об'єднання, він повинен бути вказаний в об'єднаній групі лише один раз!

first_band = RockBand("First", ["Ivan", "Sergey"])
second_band = RockBand("Second", ["Sergey", "Max"])
united = first_band + second_band
print(united.name, united.members) # "First Second United" ["Ivan", "Sergey", "Max"]

