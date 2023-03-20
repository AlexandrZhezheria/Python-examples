# Напишіть клас ListStatistics, що підраховував би декілька значень для масиву чисел.
# Його ініціалізатор повинен приймати непорожній список чисел numbers та записувати його в приватний аттрибут self.__numbers.
# Реалізуйте метод calculate_statistics, що повинен повертати словник з наступними ключами:

class ListStatistics:
    class ListStatistics:
        def __init__(self, numbers: int) -> int:
            self.__numbers = numbers

        def calculate_statistics(self) -> int:
            return {
                "min_value": self.__get_min_value(),
                "max_value": self.__get_max_value(),
                "average": self.__get_average(),
                "median": self.__get_median()
            }

        def __get_min_value(self) -> int:
            return min(self.__numbers)

        def __get_max_value(self) -> int:
            return max(self.__numbers)

        def __get_average(self) -> int:
            return sum(self.__numbers) / len(self.__numbers)

        def __get_median(self) -> int:
            sorted_numbers = sorted(self.__numbers)
            length = len(self.__numbers)
            if length % 2 == 0:
                return (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
            else:
                return sorted_numbers[length // 2]

# "min_value" - найменше число у списку
# "max_value" - найбільше число у списку
# "average" - середнє арифметичне чисел
# "median" - медіанне значення

# Приклади:
# list_statistics = ListStatistics([1, 2, 3])
# list_statistics.calculate_statistics() == {
#     "min_value": 1,
#     "max_value": 3,
#     "average": 2,
#     "median": 2,
# }
#
# list_statistics = ListStatistics([10, 10, 20, 30])
# list_statistics.calculate_statistics() == {
#     "min_value": 10,
#     "max_value": 30,
#     "average": 17.5,
#     "median": 15,
# }

# Щоб порахувати кожну з цих величин, створіть такі приватні методи:

# __get_min_value - метод, який повертає мінімально число
# __get_max_value - метод, який повертає максимальне число
# __get_average - метод, який повертає середнє арифметичне чисел
# __get_median - метод, який повертає медіану для списку
# У методі calculate_statistics викличте їх, щоб сформувати відповідь.
# Примітка: Медіана списку чисел - число, яке знаходиться посередині цього списку, якщо його впорядкувати за зростанням.
# Наприклад, медіаною списку [11, 9, 3, 5, 5] є число 5, оскільки воно стоїть посередині цього списку після його впорядкування: [3, 5, 5, 9, 11].
# Якщо в списку парна кількість елементів, число посередині не може бути визначено однозначно:
# тоді медіана обчислюється як середнє двох сусідніх значень (наприклад, медіану набору [1, 3, 5, 7] приймають рівною (3 + 5) / 2 = 4).