# Потворне число – це додатне ціле число, прості множники якого обмежені 2, 3 та 5.
# Напиши функцію ugly_numbers, яка приймає ціле число num і повертає True, якщо num – потворне число.
# Приклади:
# ugly_numbers(6) == True # 6 = 2 * 3
# ugly_numbers(1) == True # 1 не містить простих множників, тому задовольняє умові
# ugly_numbers(14) == False # 14 – не потворне число, оскільки воно містить простий множник 7


def ugly_numbers(num: int) -> bool:
    for p in 2, 3, 5:
        while num % p == 0 < num:
            num /= p
    return num == 1