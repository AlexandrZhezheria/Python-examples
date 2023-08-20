# Напиши функцію palindromic_substring, яка приймає рядок s, і повертає найдовший паліндромний підрядок в s.
# Примітки:
# 1 <= len(s) <= 1000
# s складається тільки з цифр та англійських букв
# Приклади:
# palindromic_substring("babad")  # повертає "bab" - "aba" також є допустимою відповіддю
# palindromic_substring("cbbd")  # повертає - "bb"

def expand_around_center(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


def palindromic_substring(s: str) -> str:
    longest_palindrome = ""

    for i in range(len(s)):
        palindrome1 = expand_around_center(s, i, i)
        palindrome2 = expand_around_center(s, i, i + 1)

        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome
