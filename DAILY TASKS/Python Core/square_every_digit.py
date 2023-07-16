# У цьому завданні тобі треба написати функцію square_every_digit, яка підносить кожну цифру числа до квадратного степеня і об’єднує їх.
# Приклад:
# square_every_digit(9119) == 811181

def square_every_digit(number: int) -> int:
    number = str(number)
    modified_num = ""
    for char in number:
        modified_num += str(int(char) ** 2)
    return int(modified_num)
