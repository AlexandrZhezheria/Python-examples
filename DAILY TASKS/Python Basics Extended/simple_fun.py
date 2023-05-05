# Дана послідовність цілих чисел, у якій всі елементи зустрічаються тричі,
# за винятком одного елемента-одинака (назвемо його x) та одного парного елемента (назвемо його y).
# Твоє завдання – написати функцію simple_fun, яка приймає список чисел і повертає ціле число x * x * y.

def simple_fun(num_list: list) -> int:
    single = 0
    pair = 0
    for element in num_list:
        if num_list.count(element) == 1:
            single = element**2
        elif num_list.count(element) == 2:
            pair = element
    return single * pair

# Приклади:

print(simple_fun([1, 1, 1, 2, 2, 3]))  # 3 * 3 * 2 = 18

print(simple_fun([6, 5, 4, 100, 6, 5, 4, 100, 6, 5, 4, 200]))  # 200 * 200 * 100 = 4000000




