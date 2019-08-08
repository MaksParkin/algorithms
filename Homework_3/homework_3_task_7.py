from random import random

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.


elem_num = 10
elem = []
for i in range(elem_num):
    elem.append(int(random() * 100))
    print(f"{elem[i]}", end=" ")
print()

if elem[0] > elem[1]:
    min_1 = 0
    min_2 = 1
else:
    min_1 = 1
    min_2 = 0

for i in range(2, elem_num):
    if elem[i] < elem[min_1]:
        x = min_1
        min_1 = i
        if elem[x] < elem[min_2]:
            min_2 = x
    elif elem[i] < elem[min_2]:
        min_2 = i

print(f"Порядковый номер первого наименьшего: {min_1 + 1}\nЗначение: {elem[min_1]}\n\n"
      f"Порядковый номер второго наименьшего: {min_2 + 1}\nЗначение: {elem[min_2]}")
