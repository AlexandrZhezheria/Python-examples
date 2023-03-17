# В тебе є функція greeter, яка приймає імʼя і повертає строку з привітанням.
# Напиши декоратор html_tag, який приймає строку tag. Він повинен обгортати результат обгорнутої функції так, як це показано в прикладі.
# Також повинно працювати послідовне декорування с декількома декораторами html_tag.


from typing import Callable, Any


def greeter(name: str) -> str:
    return f"Hello, {name}!"


def html_tag(tag: str) -> Callable:
    def inner(func: Callable) -> Any:
        def wrapper(*args, **kwargs) -> str:
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        return wrapper

    return inner

# Приклад:

@html_tag('div')
def greeter(name: str) -> str:
    return f"Hello, {name}!"

greeter('Alex') == "<div>Hello, Alex!</div>"

@html_tag('p')
@html_tag('a')
def greeter(name: str) -> str:
    return f"Hello, {name}!"

greeter('Maxim') == "<p><a>Hello, Maxim!</a></p>"