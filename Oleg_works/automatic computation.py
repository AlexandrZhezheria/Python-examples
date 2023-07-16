def count_segments(total_length):
    segments = [1000, 750, 500, 250]  # Длины доступных отрезков
    counts = [0, 0, 0, 0]  # Инициализация счетчиков для каждой длины

    for i, segment_length in enumerate(segments):
        count = total_length // segment_length  # Вычисление количества отрезков данной длины
        counts[i] = count  # Запись количества в соответствующий счетчик
        total_length -= count * segment_length  # Вычитание длины использованных отрезков из общей длины

    remaining_length = total_length  # Оставшаяся длина после вычета целых отрезков
    remaining_half = remaining_length / 2  # Оставшаяся длина, поделенная на два

    # if remaining_length < 250:  # Проверка, что оставшаяся длина не менее 250 мм
    #     remaining_half = 0

    return counts, remaining_half

# Пример использования функции
total_length = 15740  # Заданная общая длина
segment_counts, remaining_half = count_segments(total_length)

# Вывод результатов на экран
print("Количество деталей 1000мм:",  segment_counts[0])
print("Количество деталей 750мм:", segment_counts[1])
print("Количество деталей 500мм:", segment_counts[2])
print("Количество деталей 250мм:", segment_counts[3])
print("Оставшаяся длина, поделенная на два:", remaining_half)
