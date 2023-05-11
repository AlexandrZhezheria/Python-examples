# Дано рядок random_string і ціле число amount_of_symbols, напишіть функцію reverse_random_string,
# яка перевертає перші amount_of_symbols для кожних 2 * amount_of_symbols, рахуючи з початку рядка.
# Якщо рядок random_string менше amount_of_symbols , переверніть весь рядок.
# Якщо менше 2 * amount_of_symbols але більше або дорівнює amount_of_symbols ,
# то перший amount_of_symbols міняється місцями з першим символом у рядку, а решта залишаються без змін.
# Приклад 1:
# Input: random_string = "abcdefg", amount_of_symbols = 2
# Output: "bacdfeg"
# Приклад 2:
# Input: random_string = "abcd", amount_of_symbols = 2
# Output: "bacd"
# Приклад 3:
# Input: random_string = "abcdefghijk", amount_of_symbols = 3
# Output: "cbadefihgjk"
# Приклад 4:
# Input: random_string = "abcdefg", amount_of_symbols = 10
# Output: "gfedcba"
# Обмеження:
# 1 <= len(random_string)
# random_string містить в собі тільки букви латинського алфавіту в нижньому регістрі.
# 1 <= amount_of_symbols


def reverse_random_string(random_string: str, amount_of_symbols: int) -> str:
    if len(random_string) < amount_of_symbols:
        return random_string[::-1]

    if len(random_string) < 2 * amount_of_symbols:
        return random_string[:amount_of_symbols][::-1] + random_string[amount_of_symbols:]

    reversed_string = ""
    for i in range(0, len(random_string), 2 * amount_of_symbols):
        substr = random_string[i:i + amount_of_symbols][::-1]
        reversed_string += substr + random_string[i + amount_of_symbols:i + 2 * amount_of_symbols]

    return reversed_string
