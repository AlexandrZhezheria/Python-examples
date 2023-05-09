# Напиши функцію calculate, яка виконуватиме додавання та віднімання заданого string.
# Повернене значення також має бути рядком. Рядок string завжди не порожній.
# Приклад:
# calculate("0plus1") # повертає "1"
# calculate("0minus25") # повертає "-25"
# calculate("1plus2plus3plus4") # повертає "10"


def calculate(string: str) -> str:
    return str(
        sum(int(char) for char in string.replace("minus", "plus-").split("plus"))
    )
