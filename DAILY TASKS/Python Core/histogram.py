# 6-гранний кубик кидають кілька разів, потім результати будують у вигляді гістограми на основі символів #.
# Напиши функцію histogram, яка приймає result - список частот значень кубика і повертає рядок, що представляє гістограму,
# рядок має той самий формат, що і приклад.
# Приклад:
# histogram([7,3,10,1,0,5]) # повертає

# 6|##### 5
# 5|
# 4|# 1
# 3|########## 10
# 2|### 3
# 1|####### 7


def histogram(results: list) -> str:
    # Find the maximum frequency value for all dice values
    max_freq = max(results)
    if max_freq == 0:
        # Handle the case where all frequency values are 0
        return "6|\n5|\n4|\n3|\n2|\n1|\n"
    # Build the histogram for each dice value
    histogram_str = ""
    for value in range(6, 0, -1):
        freq = results[value - 1]
        if freq == 0:
            # Add a line for the case where the frequency is 0
            histogram_str += f"{value}|\n"
            continue
        # Calculate the number of "#" characters
        num_hashes = "#" * freq
        # Build the histogram string with "#" characters and frequency
        histogram_str += f"{value}|{num_hashes} {freq}\n"
    return histogram_str





print(histogram([7, 3, 10, 1, 0, 5]))