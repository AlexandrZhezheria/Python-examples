# У цьому завданні тобі буде дано рядок, в якому можуть бути присутніми як великі, так і малі літери. Тобі потрібно написати функцію fix_string_case, яка перетворює рядок або тільки на нижній, або на верхній регістр залежно від того, яка кількість літер конкретного регістру переважає у рядку.
# Якщо рядок містить однакову кількість великих і малих літер, перетвори рядок на нижній регістр.

def fix_string_case(word: str) -> str:
    uppercase_count = 0
    lowercase_count = 0

    # Рахуємо кількість великих і малих літер у рядку
    for c in word:
        if c.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1

    # Перевіряємо, якого регістру в рядку більше
    if uppercase_count > lowercase_count:
        return word.upper()
    elif uppercase_count == lowercase_count:
        return word.lower()
    else:
        return word.lower()

fix_string_case("coDe")
fix_string_case("CODe")
fix_string_case("coDE")
# Приклади:
# fix_string_case("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# fix_string_case("CODe") = "CODE". Uppercase characters > lowercase. Change only the "e" to uppercase.
# fix_string_case("coDE") = "code". Uppercase == lowercase. Change all to lowercase.
