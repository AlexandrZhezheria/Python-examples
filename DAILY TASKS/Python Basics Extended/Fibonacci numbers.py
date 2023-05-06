# Fibonacci numbers – це послідовність, де кожне число є сумою двох попередніх, починаючи з 0 та 1.
# Тобі треба написати функцію fibonacci_number, яка приймає номер числа у послідовності Фібоначчі і повертає його значення.
# Приклади:
# fibonacci_number(2) == 1 # F(1) + F(0) = 1 + 0 = 1
# fibonacci_number(3) == 2 # F(2) + F(1) = 1 + 1 = 2
# fibonacci_number(7) == 13 # F(6) + F(5) = 13

def fibonacci_number(num_index: int) -> int:
    previous_num, next_num = 0, 1
    for _ in range(num_index):
        previous_num, next_num = next_num, previous_num + next_num
    return previous_num
