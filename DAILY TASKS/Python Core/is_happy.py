# Напиши алгоритм який визначає, чи є числом number щасливим.
# Щасливе число — це число, яке визначається таким чином:
# number буде будь-яке позитивне число, заміни це число сумой квадратів його цифр
# Повторюй процес до тих пір, поки число не стане рівним 1, або ж воно буде нескінченно повторюватися в циклі й ніколи не стане 1.
# Ті числа, для яких цей процес закінчується на 1 - щасливі.
# Повертай True, якщо v — щасливе число, і False якщо ні.
# Помітка: - 1 <= number <= 2147483647
# Приклади:

is_happy(19)  # повертає True -
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1
is_happy(2)  # повертає False


def is_happy(number: int) -> bool:
    def get_next_number(n: int) -> int:
        return sum(int(digit) ** 2 for digit in str(n))

    slow: int = number
    fast: int = get_next_number(number)

    while fast != 1 and slow != fast:
        slow = get_next_number(slow)
        fast = get_next_number(get_next_number(fast))

    return fast == 1
