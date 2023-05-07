# Напиши функцію intersection_of_2, яка приймає списки nums1 та nums2 та повертає список, що містить числа, які є в обох списках.
# Кожен елемент у результаті повинен бути унікальним та сортуватися у порядку зростання.
# Приклади:
# intersection_of_2(nums1=[1, 2], nums2=[3, 4]) == []
# intersection_of_2(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [4, 9]
# intersection_of_2(nums1=[1, 2, 2, 1], nums2=[2, 1]) == [1, 2]


def intersection_of_two(nums1: list, nums2: list) -> list:
    set1 = set(nums1)
    set2 = set(nums2)
    return sorted(list(set1 & set2))
