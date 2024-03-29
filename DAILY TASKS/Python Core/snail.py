# Напиши функцію snail, яка приймає список matrix n x n і повертає новий список з елементами matrix,
# починаючи із зовнішніх та закінчуючи середніми, переміщаючись за годинниковою стрілкою.
# Приклад:
# matrix = [[1,2,3],
#           [8,9,4],
#           [7,6,5]]
# snail(matrix) # повертає [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ПРИМІТКА: 0x0 (порожня матриця) представляється як пустий список усередині списку [[]].


def snail(matrix: list) -> list:
    result = []
    while matrix:
        # Візьмемо верхній ряд матриці і додамо його до результату
        result += matrix.pop(0)
        if matrix and matrix[0]:
            # Візьмемо правий стовпець матриці і додамо його до результату
            for row in matrix:
                result.append(row.pop())
            # Візьмемо нижній ряд матриці (у зворотньому порядку) і додамо його до результату
            result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                # Візьмемо лівий стовпець матриці (у зворотньому порядку) і додамо його до результату
                for row in matrix[::-1]:
                    result.append(row.pop(0))
    return result
