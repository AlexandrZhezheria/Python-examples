# У твоєму ресторані почали працювати нові касири. Вони вміють приймати замовлення, але не вміють писати слова з великої літери та не вміють користуватися пробілом! Усі створювані ними «замовлення» виглядають приблизно так: "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza" Але вони хочуть отримувати замовлення у вигляді красивого чистого рядка з пробілами та великими літерами, наприклад: "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
#
# Напиши функцію get_order, яка приймає рядок order як аргумент і повертає рядок з більш чітким порядком, з пробілами та великими літерами.
# Примітки:
#
# Рядок на виході може містити дублікати, наприклад "Chicken Pizza Pizza"
# Персонал кухні очікує, що страви будуть розташовані у тому самому порядку, в якому вони вказані в меню.
# Пункти меню досить прості, пункт не може бути частиною іншого пункту:
# Burger
# Fries
# Chicken
# Pizza
# Sandwich
# Onionrings
# Milkshake
# Coke

def get_order(order: str) -> str:
    menu = {
        "Burger": 0,
        "Fries": 0,
        "Chicken": 0,
        "Pizza": 0,
        "Sandwich": 0,
        "Onionrings": 0,
        "Milkshake": 0,
        "Coke": 0
    }

    # Перетворюємо рядок в список страв та додаємо до словника
    for item in menu.keys():
        count = order.count(item.lower())
        menu[item] = count

    # Створюємо рядок з пробілами та великими літерами
    result = ""
    for item in menu.keys():
        if menu[item] > 0:
            result += (item + " ") * menu[item]

    print(result.strip())
    return result.strip()

# Розвязок ментора
def get_order(order: str) -> str:
    menu = [
        "burger",
        "fries",
        "chicken",
        "pizza",
        "sandwich",
        "onionrings",
        "milkshake",
        "coke",
    ]
    clean_order = ""
    for meal in menu:
        clean_order += (meal.capitalize() + " ") * order.count(meal)
    return clean_order[:-1]

# Приклад:
get_order("burgersandwich") # повертає "Burger Sandwich"
get_order("cokefriessandwichpizzaburger") # повертає "Burger Fries Pizza Sandwich Coke"
get_order("pizzachickenfriesburgercokemilkshakefriessandwich") # повертає "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"
get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza") # повертає "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
