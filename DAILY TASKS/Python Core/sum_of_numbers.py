# Напиши функцію sum_of_numbers, яка приймає два цілих числа first_number і second_number
# (вони можуть бути як від'ємними, так і додатними) та знаходить суму всіх цілих чисел між ними
# (first_number і second_number також входять до проміжку).
# Якщо два числа рівні, то поверни first_number або second_number.
# Примітка: first_number та second_number не є впорядкованими значеннями.
# Приклади:
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1, оскільки обидва числа є однаковими)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

def sum_of_numbers(first_number: int, second_number: int) -> int:
    if first_number > second_number:
        first_number, second_number = second_number, first_number
    return sum(range(first_number, second_number + 1))
