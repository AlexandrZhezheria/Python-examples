# Decorators
# Декораторы — это элегантный способ расширить функциональность исходных функций без изменения их исходного кода.
#
# Введение
# Декоратор — это шаблон проектирования в Python, который позволяет программистам изменять поведение функции или метода.
# Вы можете использовать декораторы для обертывания функций, чтобы расширить их поведение, не изменяя их.
# Обычно они вызываются перед определением функции, которую вы хотите украсить.
# Функции в Python — граждане первого класса. Это означает, что они поддерживают такие операции,
# как передача в качестве аргумента, возврат из функции, изменение и присвоение переменной.
# Давайте создадим функцию, которая вычисляет процент от числа:

def calculate_percentage(sum_of_money, percentage):
    return sum_of_money * percentage / 100

# Как уже упоминалось, функция также может генерировать другую функцию. Ниже мы покажем это на примере:
def taxes(percentage):
    def calculate_taxes(sum_of_money):
        return sum_of_money * percentage / 100

    return calculate_taxes


# Taxes — 5%
taxes_5 = taxes(5)

# Taxes — 10%
taxes_10 = taxes(10)

print(taxes_5(1000))  # 50.0
print(taxes_5(4000))  # 200.0
print(taxes_5(6500))  # 325.0

print(taxes_10(1000))  # 100.0
print(taxes_10(4000))  # 400.0
print(taxes_10(6500))  # 650.0

# Этот пример показывает, что если мы знаем, что нам нужно вычислить 5% или 10% налогов из разных сумм несколько раз,
# мы можем написать этот процент один раз с помощью замыкания и использовать его много раз.
# Обратите внимание: вложенной функции разрешен доступ к внешней области объемлющей функции. Это одна из концепций декораторов:

def taxes(sum_of_money):
    months = 9
    def calculate_taxes(percentage):
        return sum_of_money * percentage / 100 * months
    return calculate_taxes

# Вместе с определением декоратора мы должны отправить функцию в качестве параметра:
def taxes(func):
    def calculate_taxes(salary, percentage):
        taxes_value = salary * percentage / 100
        return func(taxes_value)

    return calculate_taxes


def message_taxes(calculated_taxes):
    print(f"Taxes amount - {calculated_taxes}")


taxes_calculation = taxes(message_taxes)
taxes_calculation(1000, 5)  # Taxes amount - 50.0

# Syntax
# Декораторы используются для изменения поведения функции. Функции принимаются в качестве аргумента в другую функцию,
# а затем вызываются внутри функции-оболочки.
# Мы можем использовать символ @ с именем функции-декоратора и поместить его над определением декорируемой функции. Например:
def taxes(func):
    pass


# First realization
@calculate_taxes
def message_taxes(taxes):
    print(f"Taxes amount - {taxes}")


# Second realization
def message_taxes(taxes):
    print(f"Taxes amount - {taxes}")


inner = taxes(message_taxes)

# Здесь обе реализации делают то же самое. Первый — это просто «синтаксический сахар» для реализации декораторов,
# он выглядит проще для чтения. Подсказка: обычно вызывается вложенная функция-оболочка.

# Decorators with Parameters
# Иногда нам может понадобиться определить декоратор, который принимает параметры. Чтобы добавить параметры,
# мы пишем их в скобках с определением функции и используем внутри декоратора так же, как параметры внутри простой функции.
# Решим задачу, аналогичную примеру с налогами. Например, давайте напишем декоратор, который принимает количество лет в качестве параметра.
# А затем рассчитывает сумму прибыли от депозита через это количество лет, с вводом суммы и процента.
# Для решения этой задачи воспользуемся формулами сложных процентов An = A0 * (1 + p/100) ^ n, где p — процент, n — количество лет,
# A0 — начальная сумма денег:

def calculate_profit(years):
    def decorate(func):
        def profit(amount, percentage):
            output = amount
            for _ in range(years):
                output *= (1 + percentage / 100)
            return func(output - amount)

        return profit

    return decorate


@calculate_profit(5)
def message_taxes(calculated_profit):
    print(f"Profit amount - {calculated_profit}")


print(message_taxes(1000, 5))  # Profit amount - 276.281

# Wrapper Problems
# Рассмотрим пример. Мы определили функции __doc__ и __name__ в декораторе и function.
# Функция использует декоратор, вызывает функции __doc__ и __name__ и возвращает значения декоратора:

def decorator_func(func):
    """Decorator  doc-string"""


def wrapper(*args, **kwargs):
    func(*args, **kwargs)


return wrapper


@decorator_func
def some_func(arg):
    """Function  doc-string"""


pass

print(some_func.__name__)  # wrapper
print(some_func.__doc__)  # Decorator doc-string

# Чтобы избежать такого поведения декоратора, используйте декоратор functools.wraps.
# Обертки Functools обновят декоратор атрибутами декорированной функции:
from functools import wraps


def decorator_func(func):
    """Decorator doc-string"""'


@wraps(func)
def wrapper(*args, **kwargs):
    func(*args, **kwargs)


return wrapper


@decorator_func
def some_func(arg):
    """Function doc-string"""


pass

print(some_func.__name__)  # some_func
print(some_func.__doc__)  # Function doc-string

# Обратите внимание: рекомендуется использовать декоратор functools.wraps.

# Decorator’s Execution
# Иногда возникает необходимость использовать несколько декораторов для одной и той же функции. Рассмотрим пример:
def add_div(func: Callable) -> Callable:
   def wrapper(*args, **kwargs):
       return f"<div>{func(*args, **kwargs)}</div>"
   return wrapper


def add_p(func: Callable) -> Callable:
   def wrapper(*args, **kwargs):
       return f"<p>{func(*args, **kwargs)}</p>"
   return wrapper


@add_div
@add_p
def print_text(text: str) -> str:
   return text


print(print_text("Hello!"))

# Возникает логичный вопрос: что будет напечатано, <div><p>Hello!</p></div> или <p><div>Hello!</div><p>?
# Чтобы найти ответ, вспомните, что декоратор — это синтаксический сахар. Эти две записи эквивалентны:
def decorator(func: Callable) -> Callable:
    pass


# First realization
@decorator
def some_func() -> None:
    pass


# Second realization
def some_func() -> None:
    pass


some_func = decorator(some_func)

# Итак, в нашем случае запись может выглядеть так:
add_div(add_p(print_text("Hello!")))
# И наш вывод будет иметь такой вид:
<div><p>Hello!</p></div>

# Но работать с декораторами не так просто, как может показаться. Их можно оценивать в разные моменты выполнения:
# когда интерпретатор Python оценивает само определение декорированного метода или когда декорированный метод вызывается.
# И порядок декораторов в этих двух случаях разный.
# Давайте посмотрим, как это работает:
def add_div(func: Callable) -> Callable:
   print("add_div function defined")

   def wrapper(*args, **kwargs):
       print("add_div function executed")
       return f"<div>{func(*args, **kwargs)}</div>"

   return wrapper


def add_p(func: Callable) -> Callable:
   print("add_p function defined")

   def wrapper(*args, **kwargs):
       print("add_p function executed")
       return f"<p>{func(*args, **kwargs)}</p>"

   return wrapper


@add_div
@add_p
def print_text(text: str) -> str:
   return text


print(print_text("Hello!"))

# Вывод следующий:
add_p function defined
add_div function defined
add_div function executed
add_p function executed
<div><p>Hello!</p></div>

# Таким образом, когда интерпретатор оценивает определение декорированного метода, декораторы оцениваются снизу вверх.
# Также это может быть сверху вниз, когда интерпретатор вызывает декорированный метод.
#
# Применение
# Ранее мы отмечали, что декораторы привыкли разрешать расширение существующей функции без модификации исходной функции.
# Рассмотрим несколько примеров наиболее распространенных случаев использования декораторов.
#
# Сроки
# Иногда возникает необходимость проверить время выполнения конкретной функции или фрагмента кода.
# Вы можете легко сделать это, найдя разницу во времени между концом функции и началом.
# Но что, если вам нужно проверить длительность нескольких функций? Тогда правильнее будет написать один декоратор и оборачивать в него функции.
# Давайте создадим такой декоратор и проверим, как он работает с функциями:
import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function runtime: {round(end_time-start_time, 4)}s")
        return function
    return wrapper


@timer
def count_range(n):
    count = 0
    for number in range(n):
         count += number
    return count


count_range(100)	# Function runtime: 0.0s
count_range(500)	# Function runtime: 0.0001s
count_range(30000)	# Function runtime: 0.0033s

Спать
# Также иногда встречаются задачи, когда необходимо, чтобы функция запускалась не сразу, а через какой-то интервал.
# Если вам нужно постоянно откладывать выполнение каких-то действий, то лучше использовать декоратор:
import functools
import time


def sleeping(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        current_time = time.localtime()
        print(f"Started function sleeping at {time.strftime('%H:%M:%S', current_time)}")
        time.sleep(3)
        current_time = time.localtime()
        print(f"Ended function sleeping at {time.strftime('%H:%M:%S", current_time)}')
        return func(*args, **kwargs)
    return wrapper


@sleeping
def count_range(n):
    count = 0
    for number in range(n):
         count += number
    return count


count_range(100)	# Started function sleeping at 08:27:34
            # Ended function sleeping at 08:27:37
# Пользователь вошел в систему
# Также декораторы проверяют, зарегистрирован ли пользователь в системе. Это обычно используется в веб-приложениях,
# поэтому сейчас мы не будем рассматривать пример.
