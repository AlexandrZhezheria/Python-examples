# Ти, напевно, знаєш про систему «лайків» із Facebook та інших мереж. Люди можуть «лайкати» повідомлення у блогах, фотографії і т.д.
# Твоя мета - написати функцію who_likes_it, яка приймає масив, що містить імена людей, яким сподобалась публікація. Функція повинна повернути текст, як показано у прикладах.
# Примітка: Для 4 або більше імен число в рядку and 2 others просто збільшується.
# Приклади:
# who_likes_it([]) == "no one likes this"
# who_likes_it(["Peter"]) == "Peter likes this"
# who_likes_it(["Jacob", "Alex"]) == "Jacob and Alex like this"
# who_likes_it(["Max", "John", "Mark"]) == "Max, John and Mark like this"
# who_likes_it(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"

def who_likes_it(names: list) -> str:
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"
