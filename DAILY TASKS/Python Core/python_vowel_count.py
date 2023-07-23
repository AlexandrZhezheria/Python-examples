# Створи функцію python_vowel_count, яка поверне кількість голосних букв у рядку. Вважатимемо,
# що тільки a, e, i, o, u є голосними (y не вважається голосною).
# Рядок складається тільки із символів нижнього регістру та/або пробілів.
# Приклади:
# vowel_count("aei ou") == 5
# vowel_count("a") == 1
# vowel_count("ya") == 1
# vowel_count("dgfhrt") == 0
# vowel_count("") == 0

def vowel_count(sentence: str) -> int:
    # Починаємо з нуля голосних букв
    count = 0
    # Перебираємо кожен символ рядка
    for char in sentence:
        # Перевіряємо, чи є символ голосною буквою
        if char in "aeiou":
            count += 1
    return count
