# Напиши функцію two_to_one, яка приймає два рядки та повертає новий відсортований рядок,
# що містить унікальні літери з обох переданих рядків.
# Приклад:
# two_to_one(first_string="abcde", second_string="ABCDE") == "ABCDEabcde"
# two_to_one(first_string="xyaabbbccccdefww", second_string="xxxxyyyyabklmopq") == "abcdefklmopqwxy"

def two_to_one(first_str: str, second_str: str) -> str:
    # об'єднуємо два рядки
    combined_str = first_str + second_str
    # зберігаємо лише унікальні літери та сортуємо рядок за зростанням
    unique_sorted_str = "".join(sorted(set(combined_str)))
    return unique_sorted_str
