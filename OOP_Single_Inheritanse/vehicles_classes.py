# Настав час використовувати потужність наслідування для того, щоб уникати дублювання коду.
# Програміст, що вочевидь не знає цієї можливості мови, реалізував два класи: Car та Train з однаковим методом go.
# Такий стиль коду нас не влаштує. Щоб уникнути дублювання коду, напиши батьківський клас Vehicle, та винеси туди спільну функцію go.
# Щоб отримати доступ до неї з класів Car та Train вкажи для них клас Vehicle як батьківський.
# Зверни увагу, що після рефакторингу в класах Car та Train повинна залишитися тільки реалізація їх власних методів wash та buy_ticket.

class Car:
    def wash(self) -> None:
        print("Washing the car...")

    def go(self, city: str) -> None:
        print(f"Go to {city}")


class Train:
    def buy_ticket(self) -> None:
        print("Buying the ticket...")

    def go(self, city: str) -> None:
        print(f"Go to {city}")

# Приклад:

car = Car()
car.wash() # "Washing the car..."
car.go("Kyiv") # "Go to Kyiv"

train = Train()
train.buy_ticket() # "Buying the ticket..."
train.go("Lviv") # "Go to Lviv"