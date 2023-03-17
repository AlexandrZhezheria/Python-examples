# Напиши функцію dice_game, яка буде використовувати генератор dice_player та симулювати гру в кості довжиною в n_rounds раундів.
# Функція має створити двох гравців за допомогою генератора dice_player.
# Далі кожен раунд брати з них наступне випадкове число та підраховувати загальний рахунок.
# Якщо в когось з гравців випало більше число, то він отримує одне очко. Якщо випало однакове значення, то очко не отримує ніхто.
# Значення кидків кожного з гравців мають бути виведені через пробіл.


import random
from typing import Generator


def dice_player(n_rounds: int) -> Generator[int, None, None]:
    for i in range(n_rounds):
        yield random.randint(1, 6)


def dice_game(n_rounds: int) -> str:
    player1 = dice_player(n_rounds)
    player2 = dice_player(n_rounds)
    player1_score = 0
    player2_score = 0

    for i in range(n_rounds):
        p1_roll = next(player1)
        p2_roll = next(player2)
        print(p1_roll, p2_roll)

        if p1_roll > p2_roll:
            player1_score += 1
        elif p2_roll > p1_roll:
            player2_score += 1

    if player1_score > player2_score:
        return "First"
    elif player2_score > player1_score:
        return "Second"
    else:
        return "Draw"

# Функція має повернути:

# "First" - якщо переміг перший гравець
# "Second" - якщо переміг другий гравець
# "Draw" - якщо була нічия
# Приклад однієї з можливих ігор:

dice_game_result = dice_game(5)
# 5 3
# 1 1
# 5 2
# 6 3
# 1 2
# dice_game_result == "First"

# Важливо: Для коректного тестування перший гравець завжди має кидати кубик першим