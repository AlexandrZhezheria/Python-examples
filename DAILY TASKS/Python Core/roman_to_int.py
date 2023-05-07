# Римські цифри представлені сімома різними символами:
# "I" – 1
# "V" – 5
# "X" – 10
# "L" – 50
# "C" – 100
# "D" – 500
# "M" – 1000
# Римські цифри зазвичай пишуться зліва – направо від більшого числа до меншого.
# Проте цифра чотири не дорівнює IIII. Натомість, число чотири пишеться як IV, бо одиниця передує п'ятірці, ми віднімаємо її і отримуємо чотири.
# Той же принцип застосовується до числа дев'ять, яке пишеться як IX.
# Є шість випадків, коли використовується віднімання:
# "I" знаходиться перед "V" (5) і "X" (10), щоб вийшло 4 і 9.
# "X" знаходиться перед "L" (50) і "C" (100), щоб вийшло 40 і 90.
# "C" знаходиться перед "D" (500) і "M" (1000), щоб вийшло 400 і 900.
# Напиши функцію roman_to_int, яка перетворює рядок з римськими цифрами в ціле число.
# Приклади:
# roman_to_int("III") == 3
# roman_to_int("LVIII") == 58
# roman_to_int("MCMXCIV") == 1994


def roman_to_int(roman: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    num = 0
    roman = (
        roman.replace("IV", "IIII")
        .replace("IX", "VIIII")
        .replace("XL", "XXXX")
        .replace("XC", "LXXXX")
        .replace("CD", "CCCC")
        .replace("CM", "DCCCC")
    )
    for char in roman:
        num += translations[char]
    return num

print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))