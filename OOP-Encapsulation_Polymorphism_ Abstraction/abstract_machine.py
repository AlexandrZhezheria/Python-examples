# Створи абстрактний клас Machine який містить абстрактні методи do_work та stop_work. Тіла цих методів повинні містити тільки вираз pass
# Створи клас Truck, Bulldozer, Excavator, які будуть наслідуватись від Machine
# В цих класах перевизнач метод do_work так, що при виклику буде виводитися повідомлення про те,
# що певна машина почала працювати: {machine_name} starts working
# Також перевизнач stop_work так, що при виклику буде виводитись повідомлення про те, що певна машина припинила роботу: {machine_name} stopped working
# Створи функцію build, яка створює екземпляри класів Truck, Bulldozer, Excavator, починає роботу кожної машини і потім припиняє
# build()
# Truck starts working
# Bulldozer starts working
# Excavator starts working
# Truck stopped working
# Bulldozer stopped working
# Excavator stopped working

# Абстрактний клас повинен наслідуватись від класу ABC з модуля abc. Методи можна зробити абстрактними за допомогою декоратора abstractmethod з модуля abc

from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def stop_work(self):
        pass


class Truck(Machine):
    def do_work(self):
        print("Truck starts working")

    def stop_work(self):
        print("Truck stopped working")


class Bulldozer(Machine):
    def do_work(self):
        print("Bulldozer starts working")

    def stop_work(self):
        print("Bulldozer stopped working")


class Excavator(Machine):
    def do_work(self):
        print("Excavator starts working")

    def stop_work(self):
        print("Excavator stopped working")


def build():
    machines = [Truck(), Bulldozer(), Excavator()]
    for machine in machines:
        machine.do_work()
    for machine in machines:
        machine.stop_work()


build()
