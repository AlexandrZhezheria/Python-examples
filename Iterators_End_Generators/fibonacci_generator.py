# Числа Фібоначчі - це числова послідовність, у якій перші два елементи дорівнюють нулю та одиниці,
# а кожен наступний дорівнює сумі двох попередніх.

def fibonacci_generator(n: int) -> int:
    prev = 0
    current = 1
    count = 0
    while count < n:
        yield prev
        prev, current = current, prev + current
        count += 1


# F₀ = 0,
# F₁ = 1,
# Fᵢ = Fᵢ₋₁ + Fᵢ₋₂
# Ось перші елементи цієї послідовності: 0, 1, 1, 2, 3, 5, 8, 13...

# Напишіть генератор fibonacci_generator, що приймає число n і рахує перші n чисел Фібоначчі.

# Приклади:

fib_generator = fibonacci_generator(4)
print(next(fib_generator)) # 0 - Число Фібоначчі з номером 0
print(next(fib_generator)) # 1 - Число Фібоначчі з номером 1
print(next(fib_generator)) # 1 - Число Фібоначчі з номером 2
# обчислюється як сума двох попередніх: 1 + 0 = 1
print(next(fib_generator)) # 2 - Число Фібоначчі з номером 3
# обчислюється як сума двох попередніх: 1 + 1 = 2
print(next(fib_generator)) # StopIteration exception - генератор повинен порахувати лише n перших чисел

fib_generator = fibonacci_generator(6)
for fib_number in fib_generator:
    print(fib_number)
# 0
# 1
# 1 (1 + 0)
# 2 (1 + 1)
# 3 (2 + 1)
# 5 (3 + 2)