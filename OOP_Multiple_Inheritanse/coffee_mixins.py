# Міксини дуже часто використовуються для того, щоб перевизначити вже існуючий метод батьківського класу.
# В тебе є клас Espresso, його метод __init__ створює властивість cup_with_coffee. У цього класу є такі методи:
# add_coffee
# add_water
# add_sugar
# add_milk
# Ці методи можуть додавати каву, воду, цукор, молоко відповідно. Також у Espresso є метод make_coffee -
# який викликає усі попередні методи і повертає cup_with_coffee.
# coffee = Espresso().make_coffee()
# coffee == ['Coffee', 'Hot water', 'Sugar']
# # за замовчанням в еспресо не входить молоко
# Але що як тобі потрібно американо (подвійна порція води), або ти б хотів еспресо без кофеїну?
# Кращий спосіб – це написати міксини, які будуть перевизначати якийсь з методів
# add_coffee, add_water, add_sugar, add_milk і додавати їх в якості батьків.
# Напиши такі міксини:
# CaffeineFreeMixin - додає каву без кофеїну
# DoubleWaterMixin - додає подвійну порцію води
# NoSugarMixin - не буде додавати цукор
# MilkMixin - додає молоко
# Міксини не повинні перевизначати метод make_coffee. Використовуючи ці міксини і Espresso в правильному порядку в наслідуванні, напиши такі класи
# Americano
# coffee = Americano().make_coffee()
# coffee == ['Coffee', 'Hot water x2', 'Sugar']
# CaffeineFreeEspresso
# coffee = CaffeineFreeEspresso().make_coffee()
# coffee == ['Caffeine free coffee', 'Hot water', 'Sugar']
# NoSugarMilkEspresso
# coffee = NoSugarMilkEspresso().make_coffee()
# coffee == ['Coffee', 'Hot water', 'Milk']
# CaffeineFreeNoSugarMilkAmericano
# coffee = CaffeineFreeNoSugarMilkAmericano().make_coffee()
# coffee == ['Caffeine free coffee', 'Hot water x2', 'Milk']
# Тіла цих класів повинні складатися тільки з виразу pass.

class Espresso:
    def __init__(self) -> None:
        self.cup_with_coffee = []

    def add_coffee(self) -> None:
        self.cup_with_coffee.append("Coffee")

    def add_water(self) -> None:
        self.cup_with_coffee.append("Hot water")

    def add_sugar(self) -> None:
        self.cup_with_coffee.append("Sugar")

    def add_milk(self) -> None:
        """
        No milk provided in espresso
        """

    def make_coffee(self) -> list:
        self.add_coffee()
        self.add_water()
        self.add_sugar()
        self.add_milk()
        return self.cup_with_coffee


class CaffeineFreeMixin:
    def add_coffee(self) -> None:
        self.cup_with_coffee.append("Caffeine free coffee")


class DoubleWaterMixin:
    def add_water(self) -> None:
        self.cup_with_coffee.append("Hot water x2")


class NoSugarMixin:
    def add_sugar(self) -> None:
        """
        No sugar added
        """


class MilkMixin:
    def add_milk(self) -> None:
        self.cup_with_coffee.append("Milk")


class Americano(DoubleWaterMixin, Espresso):
    pass


class CaffeineFreeEspresso(CaffeineFreeMixin, Espresso):
    pass


class NoSugarMilkEspresso(NoSugarMixin, MilkMixin, Espresso):
    pass


class CaffeineFreeNoSugarMilkAmericano(CaffeineFreeMixin, NoSugarMixin, MilkMixin, DoubleWaterMixin, Espresso):
    pass
