# Ти завжди мріяв відвідати Париж, але, щоб вибрати в якому місяці ти туди відправишся, ти повинен бути впевнений,
# що середня температура в цьому місяці не буде нижче бажаної.
# Напиши функцію average_temperature, яка приймає словник months з місяцями і середньою температурою та число temperature.
# Ця функція повинна повернути словник з місяцями, середня температура яких більша за temperature.
# Функція повинна містити тільки інструкцію return. Використовуй dict comprehension.


def average_temperature(months: dict, temperature: int) -> dict:
    return {
        month: avg_temp for month, avg_temp in months.items()
        if avg_temp > temperature
    }

# return {month: temp for month, temp in months.items() if temp > temperature}


# Приклад:
months = {'Dec': -4.9, 'Jan': -2.2, 'Feb': 2.1}
temperature = 5
average_temperature(months, temperature) # == {}
# Нема місяців з середньою температурою більше 5

months = {'Jun': 18, 'Jul': 23.8, 'Aug': 22.9}
temperature = 20
average_temperature(months, temperature) # == {'Jul': 23.8, 'Aug': 22.9}
# Два місяці з середньою температурою більше 20