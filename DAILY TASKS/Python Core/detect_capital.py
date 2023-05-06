# Напиши функцію detect_capital, яка повертає True, якщо взятий рядок word задовольняє одному з наступних критеріїв:
# Усі літери в слові – великі (USA).
# Усі літери в слові – малі (python).
# Тільки перша літера слова є великою (Google).
# Приклади:
# detect_capital("USA") is True
# detect_capital("FlaG") is False
# detect_capital("python") is True

def detect_capital(word: str) -> bool:
    if word.isupper() or word.islower():
        return True
    elif word[0].isupper() and word[1:].islower():
        return True
    else:
        return False
