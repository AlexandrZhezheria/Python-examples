# Напиши функцію message_people, яка приймає список імен people, створює і повертає функцію print_message.
# Внутрішня функція приймає строку message і в залежності від того, чому дорівнює message ("hello"/"meeting"/"bye")
# виводить результати, які показані в прикладі, вона не повинна нічого повертати.


from typing import List, Callable


def message_people(people: List[str]) -> Callable[[str], None]:
    def print_message(message: str) -> None:
        if message == "hello":
            print(f"Hello, {", ".join(people)}, nice to see you!")
        elif message == "meeting":
            print(f"{", ".join(people)}, we have a meeting in an hour, don"t be late!")
        elif message == "bye":
            print(f"Bye {", ".join(people)}, see you tomorrow!")
    return print_message

# Приклад:
mes_people = message_people(["Alex", "Robert", "Tom"])
mes_people("hello")
# Hello, Alex, Robert, Tom, nice to see you!
mes_people("meeting")
# Alex, Robert, Tom, we have a meeting in an hour, don"t be late!
mes_people("bye")
# Bye Alex, Robert, Tom, see you tomorrow!