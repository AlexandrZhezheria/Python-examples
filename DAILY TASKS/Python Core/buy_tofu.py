# Напиши функцію buy_tofu яка приймає рядок box з предметами всередині цієї box та cost - вартість тофу,
# функція повинна відсортувати усі монети в box та повернути список у такому форматі:
# [count_of_mon_coins_in_box, count_of_monme_coins_in_box, sum_of_all_coins_value_in_box, minimum_number_of_coins_needed_for_tofu]
# Примітки:
# Монети мають такі номінали:
# monme = 60
# mon = 1
# Визначте мінімальну кількість монет для оплати тофу.
# Ви повинні платити лише монетами, без здачі.
# Якщо у вас немає необхідної кількості монет, поверніть “leaving the market”.
# Якщо вартість тофу вища, ніж ваша загальна сума грошей, також поверніть leaving the market.
# Приклади:
# cost = 5
# box = "mon monme"
# buy_tofu(cost, box)  # returns "leaving the market"
# cost = 122
# box = "monme pie mon mon apple monme"
# buy_tofu(cost, box)  # returns [2,2,122,4]
# cost = 674
# box = "mon mon mon"
# buy_tofu(cost, box)  # returns "leaving the market"


def buy_tofu(cost: int, box: str) -> list or str:
    # write your code here
    pass
