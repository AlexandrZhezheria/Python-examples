# Напиши клас Matrix, який приймає двомірний масив matrix розміром N x N. Метод __init__ повинен зберігати цей масив у
# властивості self.matrix.
# Клас Matrix повинен мати чотири методи:
# get_diagonal(): повертає діагональ матриці у вигляді списку
# get_counter_diagonal(): повертає зворотню діагональ матриці у вигляді списку
# rotate_rows(number): обертає рядки матриці number разів.
# rotate_columns(number): обертає стовпці матриці number разів.
# Зверніть увагу: потрібно змінити атрибут self.matrix у методах rotate_rows та rotate_columns.
class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list:
        return [self.matrix[i][i] for i in range(len(self.matrix))]

    def get_counter_diagonal(self) -> list:
        return [self.matrix[i][-i - 1] for i in range(len(self.matrix))]

    def rotate_rows(self, number: int) -> None:
        if not self.matrix:
            return
        num = number % len(self.matrix)
        self.matrix = self.matrix[num:] + self.matrix[:num]

    def rotate_columns(self, number: int) -> None:
        if not self.matrix:
            return
        num = number % len(self.matrix)
        for i in range(len(self.matrix)):
            self.matrix[i] = self.matrix[i][num:] + self.matrix[i][:num]

# Приклад:

matrix_inst = Matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
matrix_inst.get_diagonal()  # [1, 5, 9]
matrix_inst.get_counter_diagonal()  # [3, 5, 7]
matrix_inst.rotate_rows(1)
# matrix_inst.matrix == [
#     [4, 5, 6],
#     [7, 8, 9],
#     [1, 2, 3]
# ]
# Перший рядок став останнім

matrix_inst.rotate_columns(1)
# matrix_inst.matrix == [
#     [5, 6, 4],
#     [8, 9, 7],
#     [2, 3, 1]
# ]
# Перший стовпець став останнім