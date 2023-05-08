# У тебе є список цілих чисел непарної довжини, де всі елементи містять дублікати, окрім одного.
# Напиши функцію find_the_stray, яка повертає число без пари.
# Приклади:
# find_the_stray([1, 1, 2]) == 2
# find_the_stray([17, 17, 3, 17, 17, 17, 17]) == 3


def find_the_stray(num_list: list) -> int:
    for i in num_list:
        if num_list.count(i) == 1:
            return i
