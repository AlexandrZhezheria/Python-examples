# Пример декоратора с параметрами:
def typed(type_):
    def real_decorator(function):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f"Тип должен быть {type_}")
            return function(*args)

        return wrapper

    return real_decorator


@typed(int)
def calculate(a: int, b: int, c: int) -> int:
    return a + b + c


@typed(str)
def convert(a: str, b: str) -> str:
    return a + b


if __name__ == "__main__":
    # calculate = typed_int(calculate)
    # calculate = typed(int)(calculate)
    print(calculate(1, 2, 3))
    print("123", "Hello")
