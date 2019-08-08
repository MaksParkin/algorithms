from random import random

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


elem_num = 10
x = [0] * elem_num
for i in range(elem_num):
    x[i] = int(random() * 50)
    print(f"{x[i]}", end=' ')
print()

min_id = 0
max_id = 0
for i in range(1, elem_num):
    if x[i] < x[min_id]:
        min_id = i
    elif x[i] > x[max_id]:
        max_id = i
print(f"Минимальный элемент: {x[min_id]}\nМаксимальных элемент: {x[max_id]}")

if min_id > max_id:
    min_id, max_id = max_id, min_id

sum = 0
for i in range(min_id + 1, max_id):
    sum += x[i]
print(f"Сумма всех элементов мажду {x[min_id]} и {x[max_id]}: {sum}")
