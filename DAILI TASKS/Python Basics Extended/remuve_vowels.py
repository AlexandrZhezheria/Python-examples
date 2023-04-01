# Тролі атакують твій розділ коментарів!
# Поширений спосіб впоратися з цією ситуацією — видалити всі голосні літери з коментарів тролів, нейтралізуючи загрозу.
# Твоє завдання – написати функцію disemvowel_trolls, яка приймає рядок і повертає новий рядок, у якому видалені всі голосні.
# Примітка: у цьому завданні літера у не вважається голосною.
# Приклади:
# disemvowel_trolls("Delete all vowels!") == "Dlt ll vwls!"
# disemvowel_trolls("QWERTY") == "QWRTY"

def disemvowel_trolls(s: str) -> str:
    vowels = "aeiouAEIOU"
    return "".join(c for c in s if c not in vowels)

# розвязок ментора:
def disemvowel_trolls(sentence: str) -> str:
    for char in "aeiouAEIOU":
        sentence = sentence.replace(char, "")
    return sentence
