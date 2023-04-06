# У тебе є змінна jewels, яка містить дорогоцінні камені, та змінна stones, у якій знаходяться усі камені.
# Напиши функцію jewels_and_stones, яка повертає кількість jewels, що містяться в stones.
# Літери чутливі до регістру (наприклад, a вважається типом каменю, відмінним від A).
# Всі символи в jewels є унікальними.

def jewels_and_stones(jewels: str, stones: str) -> int:
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count

# Приклади:
# jewels_and_stones(jewels="aA", stones="aAAbbbb") == 3
# jewels_and_stones(jewels="z", stones="ZZ") == 0
# jewels_and_stones(jewels="abcde", stones="abcd") == 4
print(jewels_and_stones(jewels="aA", stones="aAAbbbb"))
print(jewels_and_stones(jewels="z", stones="ZZ"))
print(jewels_and_stones(jewels="abcde", stones="abcd"))
