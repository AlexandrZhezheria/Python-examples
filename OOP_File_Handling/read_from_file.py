# Дано файл, який містить багаторядковий текст без розділових знаків (слова відокремлюються пробілами та переносом рядків).
#
# Тобі потрібно знайти слова, що починаються з «w» або «W».
#
# Поверни їх у нижньому регістрі у вигляді відсортованого списку.
#
# Якщо файл не містить потрібних слів, поверни порожній список.
#
# Приклади:
#
# "Width world Wide web"
# Result: ["web", "wide", "width", "world"]
#
# "WWW Four-bedroom farmhouse in the countryside Wave All of the four double bedrooms are en suite"
# Result: ["wave", "www"]

def read_from_file(file_name: str) -> list[str]:
    def read_from_file(file_name: str) -> list[str]:
        with open(file_name, "r") as f:
            text = f.read()
            text = text.replace("\n", " ")
            words = text.split(" ")
            words_starting_with_w = []
            for word in words:
                if word.startswith(("w", "W")):
                    words_starting_with_w.append(word.lower())
        return sorted(words_starting_with_w)
