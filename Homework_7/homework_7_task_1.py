# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100). Выведите на
# экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

gap = [random.randint(-100, 100) for i in range(10)]
print(f"Исходный список: {gap}")


def bubble_sort(lst):
    n = 1

    while n < len(lst):
        sorted = True

        for i in range(len(lst) - n):

            if gap[i] < gap[i + 1]:
                gap[i], gap[i + 1] = gap[i + 1], gap[i]
                sorted = False

        if sorted:
            break

        n += 1

    print(f"Отсортированный список по убыванию: {gap}")


bubble_sort(gap)
