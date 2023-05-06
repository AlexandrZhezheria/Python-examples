# Напиши функцію shortest_step, яка приймає число та повертає найменшу кількість кроків, які потрібно пройти від 1 до цього числа.
# Функція може виконувати лише такі операції:
# Додати 1
# Помножити на 2
# Приклади:
# shortest_step(3) == 2
# # 1st step: 1 + 1 = 2
# # 2nd step: 2 + 1 = 3
#
# shortest_step(12) == 4
# # 1st step: 1 + 1 = 2
# # 2nd step: 2 + 1 = 3
# # 3rd step: 3 * 2 = 6
# # 4th step: 6 * 2 = 12

def shortest_step(goal_num: int) -> int:
    steps_count = 0
    while goal_num > 1:
        if not goal_num % 2 == 0:
            goal_num -= 1
            steps_count += 1
        else:
            goal_num /= 2
            steps_count += 1
    return steps_count
