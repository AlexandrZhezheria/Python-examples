# Напиши функцію capitals_first, яка повертає рядок, де всі слова, які починаються з великих літер,
# знаходяться попереду, а ті, що з малих – у кінці.
# Порядок розташування слів з великих та малих літер повинен відповідати порядку їх появи в оригінальному рядку.
# Приклади:
# capitals_first("academy Mate") == "Mate academy"
# capitals_first("one Two three Four") == "Two Four one three"

def capitals_first(sentence: str) -> str:
    words = sentence.split()
    upper_words = []
    lower_words = []
    for word in words:
        if word[0].isupper():
            upper_words.append(word)
        else:
            lower_words.append(word)
    return " ".join(upper_words + lower_words)
