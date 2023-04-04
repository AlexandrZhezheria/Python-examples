# У цьому завданні тобі буде дано рядок, в якому можуть бути присутніми як великі, так і малі літери. Тобі потрібно написати функцію fix_string_case, яка перетворює рядок або тільки на нижній, або на верхній регістр залежно від того, яка кількість літер конкретного регістру переважає у рядку.
# Якщо рядок містить однакову кількість великих і малих літер, перетвори рядок на нижній регістр.

def fix_string_case(word: str) -> str:
    lower_count = 0
    upper_count = 0
    for i in range(len(word)):
        if word[i].islower():
            lower_count += 1
        elif word[i].isupper():
            upper_count += 1
    if lower_count < upper_count:
        return word.upper()
    return word.lower()

fix_string_case("coDe")
fix_string_case("CODe")
fix_string_case("coDE")
# Приклади:
# fix_string_case("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# fix_string_case("CODe") = "CODE". Uppercase characters > lowercase. Change only the "e" to uppercase.
# fix_string_case("coDE") = "code". Uppercase == lowercase. Change all to lowercase.

