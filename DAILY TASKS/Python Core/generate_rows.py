# Напиши функцію generate_rows, яка приймає позитивне ціле число rows і повертає список рядків трикутника Паскаля від першого до rows.
# Примітки:
# 0 < rows <= 10
# У трикутнику Паскаля кожне число є сумою двох чисел безпосередньо над ним, як показано:
# Приклади:
# generate_rows(5)  # повертає [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# generate_rows(1)  # повертає [[1]]


def generate_rows(rows: int) -> list:
    pascal = [[1] * (i + 1) for i in range(rows)]
    for i in range(rows):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    return pascal
