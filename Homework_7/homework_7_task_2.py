# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


import random

size = 10
array = [random.uniform(0, 50) for i in range(size)]
print(f"Случайный массив в промежутке [0; 50){array}")


def merge_sorting(x):
    if len(x) < 2:
        return x
    left = merge_sorting(x[:len(x) // 2])
    right = merge_sorting(x[len(x) // 2:len(x)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            x[k] = left[i]
            i = i + 1
        else:
            x[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        x[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        x[k] = right[j]
        j = j + 1
        k = k + 1
    return x


print(f"Сортировка по возрастанию: {merge_sorting(array)}")
