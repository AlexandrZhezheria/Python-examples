# Напиши функцію make_readable, яка приймає невід'ємне число seconds та повертає час у читабельному форматі (HH:MM:SS)
# Примітки:
# HH = години, підбиті до 2 цифр, діапазон: 00 - 99
# MM = хвилини, підбиті до 2 цифр, діапазон: 00 – 59
# SS = секунди, підбиті до 2 цифр, діапазон: 00 – 59
# Максимальний час ніколи не перевищує 359999 секунд (99:59:59)
# Приклади:
# make_readable(0)  # повертає "00:00:00"
# make_readable(5)  # повертає "00:00:05"
# make_readable(60)  # повертає "00:01:00"
# make_readable(359999)  # повертає "99:59:59"

def make_readable(seconds: int) -> str:
    if seconds < 0 or seconds > 359999:
        raise ValueError("Input seconds must be in the range 0-359999")

    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
