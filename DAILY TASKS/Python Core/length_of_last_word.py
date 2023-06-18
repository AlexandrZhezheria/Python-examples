# Напиши функцію length_of_last_word, яка приймає рядок string, що складається зі слів та пробілів,
# і повертає довжину останнього слова у рядку. Слово - це максимальний підрядок, що складається тільки із буквених символів.
#
# Примітки:
#
# 1 <= len(string) <= 1000
# string складається тільки з англійських літер та пробілів " "
# У `sstring буде хоча б одне слово
# Приклади:
#
# length_of_last_word("Hello World")  # повертає 5 - Останнє слово "World" має довжину 5
# length_of_last_word("   fly me   to   the moon  ")  # повертає 4 - Останнє слово "moon" має довжину 4
# length_of_last_word("luffy досі джойбою")  # повертає 6 - Останнє слово "joyboy" має довжину 6

def length_of_last_word(string: str) -> int:
    words = string.split()
    last_word = words[-1]
    return len(last_word)
