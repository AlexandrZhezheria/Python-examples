def count_segments(side_lengths):
    segments = [1000, 750, 500, 250]  # Довжини доступних відрізків
    counts = [0, 0, 0, 0]  # Ініціалізація лічильників для кожної довжини

    for side_length in side_lengths:
        remaining_length = side_length
        side_counts = [0, 0, 0, 0]  # Лічильники для поточної сторони

        for i, segment_length in enumerate(segments):
            count = remaining_length // segment_length  # Обчислення кількості відрізків даної довжини
            side_counts[i] = count  # Запис кількості в відповідний лічильник
            remaining_length -= count * segment_length  # Віднімання довжини використаних відрізків від загальної довжини

        counts = [counts[i] + side_counts[i] for i in range(len(counts))]  # Додавання лічильників поточної сторони до загальних лічильників

        remaining_half = remaining_length / 2  # Оставшаяся довжина, поділена на два

        print("Кількість відрізків 1000мм:", side_counts[0])
        print("Кількість відрізків 750мм:", side_counts[1])
        print("Кількість відрізків 500мм:", side_counts[2])
        print("Кількість відрізків 250мм:", side_counts[3])
        print("Залишкова довжина, поділена на два:", remaining_half)
        print()

    return counts

# Приклад використання функції
side_lengths = [1475, 780, 1274, 300]  # Довжини кожної сторони периметра
segment_counts = count_segments(side_lengths)

# Виведення результатів на екран
print("Загальна кількість відрізків 1000мм:", segment_counts[0])
print("Загальна кількість відрізків 750мм:", segment_counts[1])
print("Загальна кількість відрізків 500мм:", segment_counts[2])
print("Загальна кількість відрізків 250мм:", segment_counts[3])


