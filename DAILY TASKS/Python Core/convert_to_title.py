# Напиши функцію convert_to_title, яка приймає позитивне число num та повертає заголовок num колонки, на аркуші Excel.
# Приклади:
# convert_to_title(1) # повертає "A" - заголовок першої колонки в Excel
# convert_to_title(2) # повертає "B"
# convert_to_title(28) # повертає "AB"
# convert_to_title(701) # повертає "ZY"

def convert_to_title(num: int) -> str:
    capitals = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
    result = []
    while num > 0:
        result.append(capitals[(num - 1) % 26])
        num = (num - 1) // 26
    result.reverse()
    return "".join(result)
