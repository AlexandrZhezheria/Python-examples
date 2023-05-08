# Напиши функцію count_primes, яка приймає ціле число number >= 0 та повертає кількість простих чисел, які менші за number.
# Приклад 1:
# count_primes(10) # returns 4 - there are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# count_primes(0) # returns 0
# count_primes(1) # returns 0


def count_primes(number: int) -> int:
    if number < 2:
        return 0

    is_prime = [True] * number
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(number ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, number, i):
                is_prime[j] = False

    return sum(is_prime)
