# Напиши функцію square_color, яка повертає колір заданого квадрата на звичайній шаховій дошці 8x8:
#
# Шахова дошка
#
# Приклади:
#
# Square_color("a", 8) # повертає "white"
# Square_color("b", 2) # повертає "black"
# Square_color("f", 5) # повертає "white"

def square_color(string: str, rank: int) -> str:
    letters = "abcdefgh"
    if letters.index(string) % 2 == rank % 2:
        return "white"
    else:
        return "black"


print(square_color("a", 8))
print(square_color("b", 2))
print(square_color("f", 5))
