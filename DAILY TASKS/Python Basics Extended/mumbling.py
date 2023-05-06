# На цей раз ні історії, ні теорії. У наведених нижче прикладах показано, як повинна працювати функція mumbling.
# Приклади:
# mumbling("abcd") -> "A-Bb-Ccc-Dddd"
# mumbling("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# mumbling("cwAt") -> "C-Ww-Aaa-Tttt"
# Параметр в mumbling є рядком, який містить лише літери a..z та A..Z.

def mumbling(string: str) -> str:
    # створюємо порожній список для зберігання нових літер
    new_letters = []

    # ітеруємося по кожній літері в рядку та додаємо нову літеру до списку
    for i in range(len(string)):
        # першу літеру робимо великою, всі наступні - маленькими
        new_letters.append(string[i].upper() + string[i].lower() * i)

    # збираємо рядок, розділяючи літери дефісами
    return "-".join(new_letters)
