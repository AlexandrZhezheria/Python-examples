# Напиши функцію fix_parentheses, яка приймає string і повертає рядок із відновленими круглими дужками,
# щоб усі круглі дужки, що відкриваються або закриваються, мали відповідні аналоги.
# Результат має бути мінімальної довжини. Не додавай непотрібні дужки. string має різну довжину і містить лише "(" та/або ")".
# Приклад:
# fix_parentheses("(") # повертає "()"
# fix_parentheses(")") # повертає "()"
# fix_parentheses("()") # повертає "()"
# fix_parentheses("(()()(") # повертає "(()()())"


def fix_parentheses(string: str) -> str:
    left = 0
    right = 0
    for symbol in string:
        right += (symbol == "(") - (symbol == ")")
        if right < 0:
            left, right = left + 1, 0
    return "(" * left + string + ")" * right
