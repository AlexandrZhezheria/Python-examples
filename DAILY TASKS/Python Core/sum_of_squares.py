# На кресленні нижче ми маємо частину трикутника Паскаля,
#          1
#         1 1
#        1 2 1
#       1 3 3 1
#      1 4 6 4 1
#     1 5 10 10 5 1
#    1 6 15 20 15 6 1
#   1 7 21 35 35 21 7 1
# горизонтальні лінії пронумеровані від нуля (з вершини).
# Ми хочемо обчислити суму квадратів біноміальних коефіцієнтів на заданій горизонтальній лінії за допомогою функції, яка називається sum_of_squares.
# Чи можете ви написати програму, яка обчислює sum_of_squares(number), де number — номер горизонтальної лінії?
# Функція приймає number (з: number>= 0) як параметр і певартає суму квадратів біноміальних коефіцієнтів у рядку number.
# Приклади:
# sum_of_squares(0) => 1
# sum_of_squares(1) => 2
# sum_of_squares(4) => 70
# sum_of_squares(50) => 100891344545564193334812497256


def sum_of_squares(number: int) -> int:
    # Handle the special case of the 0th row
    if number == 0:
        return 1

    # If the number is negative, return 0
    if number < 0:
        return 0

    # Compute the coefficients for the given row
    row = [1]
    for i in range(1, number + 1):
        row.append(row[-1] * (number - i + 1) // i)

    # Compute the sum of squares of the coefficients
    return sum(x ** 2 for x in row)


print(sum_of_squares(0))
print(sum_of_squares(1))
print(sum_of_squares(4))
print(sum_of_squares(50))